#!/usr/bin/env python3
"""
List every release on the same label as a given Deezer album.

Usage:
    python deezlabel.py https://www.deezer.com/en/album/254918272
    python deezlabel.py https://www.deezer.com/en/album/254918272 --strict
    python deezlabel.py https://www.deezer.com/en/album/254918272 --by-date

Output (one release per line):
    YYYY-MM-DD  Artist - Album title  https://www.deezer.com/album/ID

Sorted by artist, then release date. --by-date sorts by release date only.

Albums whose tracks are by more than one artist are shown as "Various Artists".

Assisted by Claude
"""

import argparse
import re
import sys
import time

import requests

API = "https://api.deezer.com"
ALBUM_RE = re.compile(r"/album/(\d+)")
VARIOUS_ARTISTS = "Various Artists"
REQUEST_DELAY = 0.12  # stay under Deezer's ~50 requests / 5 s limit

session = requests.Session()
session.headers["User-Agent"] = "deezer-label-lister/1.0"


class DeezerError(Exception):
    pass


def get_json(url, params=None, retries=3):
    """GET a URL and return parsed JSON, raising DeezerError on failure."""
    for attempt in range(retries + 1):
        time.sleep(REQUEST_DELAY)
        try:
            resp = session.get(url, params=params, timeout=20)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as e:
            raise DeezerError(str(e)) from e
        except ValueError as e:
            raise DeezerError(f"Invalid JSON from {url}") from e

        # Deezer reports errors with HTTP 200 and an "error" object in the body.
        error = data.get("error") if isinstance(data, dict) else None
        if not error:
            return data

        # Code 4 = "Quota limit exceeded": wait and try again.
        if error.get("code") == 4 and attempt < retries:
            time.sleep(5)
            continue
        raise DeezerError(f"Deezer API error: {error.get('message', error)}")


def get_paged(url, params=None):
    """Yield every item from a paginated Deezer endpoint."""
    page = get_json(url, params=params)
    while True:
        yield from page.get("data", [])
        if not page.get("next"):
            break
        page = get_json(page["next"])  # "next" already contains the params


def resolve_album_id(url):
    """Extract the album ID from a Deezer URL (or accept a bare ID).

    Follows redirects for short share links (e.g. link.deezer.com/...).
    """
    url = url.strip()
    if url.isdigit():
        return url

    m = ALBUM_RE.search(url)
    if not m:
        # Possibly a short/share link: follow redirects, check the final URL.
        try:
            final_url = session.get(url, timeout=20).url
        except requests.RequestException as e:
            raise DeezerError(f"Could not open URL: {url}") from e
        m = ALBUM_RE.search(final_url)
        if not m:
            raise DeezerError(f"No album ID found in URL: {url}")
    return m.group(1)


def get_album(album_id):
    return get_json(f"{API}/album/{album_id}")


def search_label(label):
    """Yield every album returned by a label search."""
    # Double quotes inside the label would break the query syntax.
    query = f'label:"{label.replace(chr(34), "")}"'
    return get_paged(f"{API}/search/album", params={"q": query, "limit": 100})


def album_artist(album):
    """Return the album's artist, or "Various Artists" if tracks differ.

    The artist Deezer gives is often just the artist of the first track,
    so for multi-track releases we check the artist of every track.
    """
    first_artist = album.get("artist", {}).get("name", "Unknown artist")
    nb_tracks = album.get("nb_tracks", 0)
    if nb_tracks <= 1:
        return first_artist  # a one-track release can't have mixed artists

    # The full album object usually embeds the track list; only make an
    # extra request if it's missing or incomplete.
    tracks = album.get("tracks", {}).get("data", [])
    if len(tracks) < nb_tracks:
        tracks = get_paged(f"{API}/album/{album['id']}/tracks",
                           params={"limit": 100})

    artist_ids = set()
    for track in tracks:
        artist_ids.add(track.get("artist", {}).get("id"))
        if len(artist_ids) > 1:
            return VARIOUS_ARTISTS  # no need to look at the remaining tracks
    return first_artist


def date_key(release_date):
    """Sort key for a release date; missing dates sort last."""
    if not release_date or release_date.startswith("0000"):
        return "9999-99-99"
    return release_date


def main():
    parser = argparse.ArgumentParser(
        description="List all Deezer releases on the same label as a given album."
    )
    parser.add_argument("url", help="Deezer album URL (or just the album ID)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Keep only releases whose label matches exactly",
    )
    parser.add_argument(
        "--by-date", "--by-id",
        dest="by_date",
        action="store_true",
        help="Sort by release date only, ignoring artist name",
    )
    args = parser.parse_args()

    # Avoid crashes on consoles that can't display some characters.
    sys.stdout.reconfigure(errors="replace")

    try:
        album_id = resolve_album_id(args.url)
        label = (get_album(album_id).get("label") or "").strip()
        if not label:
            print(f"Album {album_id} has no label information.", file=sys.stderr)
            return 1
        print(f"Label: {label}\n", file=sys.stderr)

        # Collect everything first so we can work out the column widths.
        seen_ids = set()
        for item in search_label(label):
            item_id = item["id"]
            if item_id in seen_ids:
                continue
            seen_ids.add(item_id)

        if not seen_ids:
            print("No releases found.", file=sys.stderr)
            return 0

        i = 1
        rows = []
        for item_id in seen_ids:
            print(f"\rGetting releases {i * 100 // len(seen_ids):3d}%", end="", file=sys.stderr, flush=True)
            # The search results lack the release date, so fetch the full
            # album. This also gives us the label and (usually) the tracks.
            album = get_album(item_id)

            if args.strict:
                item_label = (album.get("label") or "").strip()
                if item_label.casefold() != label.casefold():
                    continue

            artist = album_artist(album)
            title = album.get("title") or item.get("title", "Unknown title")
            link = album.get("link") or f"https://www.deezer.com/album/{item_id}"
            release_date = album.get("release_date") or ""
            rows.append((artist, title, link, item_id, release_date))
            i += 1

        artist_width = max(len(artist) for artist, _, _, _, _ in rows)
        title_width = max(len(title) for _, title, _, _, _ in rows)

        # Sort by date (ID breaks ties), optionally grouped by artist first.
        if args.by_date:
            rows.sort(key=lambda row: (date_key(row[4]), row[3]))
        else:
            rows.sort(key=lambda row: (row[0].casefold(),
                                       date_key(row[4]), row[3]))

        print("\n")
        for artist, title, link, _, release_date in rows:
            print(f"{artist:<{artist_width}} {title:<{title_width}} {link}")

        return 0

    except DeezerError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
