#!/usr/bin/env python3
"""
List every release on the same label as a given Deezer album.

Usage:
    python deezer_label.py https://www.deezer.com/en/album/254918272
    python deezer_label.py https://www.deezer.com/en/album/254918272 --strict

Output (one release per line):
    Artist - Album title  https://www.deezer.com/album/ID

Assisted by Claude
"""

import argparse
import re
import sys
import time

import requests

API = "https://api.deezer.com"
ALBUM_RE = re.compile(r"/album/(\d+)")

session = requests.Session()
session.headers["User-Agent"] = "deezer-label-lister/1.0"


class DeezerError(Exception):
    pass


def get_json(url, params=None, retries=3):
    """GET a URL and return parsed JSON, raising DeezerError on failure."""
    for attempt in range(retries + 1):
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
    """Yield every album returned by a label search, following pagination."""
    # Double quotes inside the label would break the query syntax.
    query = f'label:"{label.replace(chr(34), "")}"'
    page = get_json(f"{API}/search/album", params={"q": query, "limit": 100})
    while True:
        yield from page.get("data", [])
        if not page.get("next"):
            break
        page = get_json(page["next"])  # "next" already contains the params


def main():
    parser = argparse.ArgumentParser(
        description="List all Deezer releases on the same label as a given album."
    )
    parser.add_argument("url", help="Deezer album URL (or just the album ID)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fetch each result and keep only exact label matches "
             "(slower: one extra request per album)",
    )
    parser.add_argument(
        "--by-id",
        action="store_true",
        help="Sort by album ID only, ignoring artist name",
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
        rows = []
        seen_ids = set()
        for item in search_label(label):
            item_id = item["id"]
            if item_id in seen_ids:
                continue
            seen_ids.add(item_id)

            if args.strict:
                time.sleep(0.12)  # stay under Deezer's ~50 requests / 5 s limit
                item_label = (get_album(item_id).get("label") or "").strip()
                if item_label.casefold() != label.casefold():
                    continue

            artist = item.get("artist", {}).get("name", "Unknown artist")
            title = item.get("title", "Unknown title")
            link = item.get("link") or f"https://www.deezer.com/album/{item_id}"
            rows.append((artist, title, link, item_id))

        if not rows:
            print("No releases found.", file=sys.stderr)
            return 0

        artist_width = max(len(artist) for artist, _, _, _ in rows)
        title_width = max(len(title) for _, title, _, _ in rows)

        # Sort either just by ID, or by artist name and ID:
        if args.by_id:
            rows.sort(key=lambda row: row[3])
        else:
            rows.sort(key=lambda row: (row[0].casefold(), row[3]))

        for artist, title, link, _ in rows:
            print(f"{artist:<{artist_width}} - {title:<{title_width}}  {link}")

        return 0

    except DeezerError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
