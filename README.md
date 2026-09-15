# deezlabel

Simple script to find the label a particular Deezer album/track is on and print 
a list of all other albums on the service from the same label.

Mostly Claude's work with a little sanity checking by me.  It's a little slow as
each album needs to be checked to see if it is single-artist or compilation, for
some reason Deezer no longer seem to reflect that in a simple way without going
through the tracks on each one.

#### Example

```
rez@laptop:~/deezlabel$ ./deezlabel.py https://www.deezer.com/en/album/434472657 
Label: Reggae Library

Alton Ellis          - Jamaican Rock                                                    https://www.deezer.com/album/353333427
Alton Ellis          - Here I Am - Reggae Got Soul                                      https://www.deezer.com/album/359576277
Alton Ellis          - Love to Share                                                    https://www.deezer.com/album/362304517
Augustus Pablo       - The Early Years                                                  https://www.deezer.com/album/372971107
Barrington Levy      - Sister Debby                                                     https://www.deezer.com/album/353308627
Barrington Levy      - Making Tracks                                                    https://www.deezer.com/album/362302907
Barrington Levy      - Mr Robber Man                                                    https://www.deezer.com/album/927726281
Beenie Man           - Dancehall Generals:                                              https://www.deezer.com/album/415176737
Beenie Man           - Somebody (Step Father Riddim)                                    https://www.deezer.com/album/911580671
Beenie Man           - Your Bad Luck (Hurricane Riddim)                                 https://www.deezer.com/album/914876531
Beenie Man           - Dem No Know Badness                                              https://www.deezer.com/album/920026061
Beenie Man           - Hit With Music                                                   https://www.deezer.com/album/938914951
Beenie Man           - 100 Dollar Bag                                                   https://www.deezer.com/album/943218051
Beenie Man           - Good Jamaica - Impact Riddim                                     https://www.deezer.com/album/956843651
Beenie Man           - Bandi Legs (Raw)                                                 https://www.deezer.com/album/961119861
Beenie Man           - Ganja Farm (Problem Riddim)                                      https://www.deezer.com/album/993567461
Beenie Man           - Oh La La La - Caribbean Riddim (2026 Remaster)                   https://www.deezer.com/album/1004379851
Beenie Man           - Tata Fool                                                        https://www.deezer.com/album/1035536832
Beres Hammond        - La La La                                                         https://www.deezer.com/album/73209632
Beres Hammond        - Soul                                                             https://www.deezer.com/album/624888521
Beres Hammond        - REGGAE ICONS: Beres Hammond                                      https://www.deezer.com/album/634574981
Beres Hammond        - Beres Hammond: Remastered Edition                                https://www.deezer.com/album/705662361
Beres Hammond        - Love Is Stronger                                                 https://www.deezer.com/album/932570561
Beres Hammond        - What A Night (2026 Remaster)                                     https://www.deezer.com/album/956802011
Beres Hammond        - Fight To Defend It (Love Is Not A Gamble Riddim)                 https://www.deezer.com/album/962835501
Beres Hammond        - Dancing Beauty                                                   https://www.deezer.com/album/993447821
Boris Gardiner       - I Wanna Wake Up With You                                         https://www.deezer.com/album/677465751
Boris Gardiner       - I Wanna Wake Up With You                                         https://www.deezer.com/album/998253731
Bounty Killer        - Revolution, Pt. 3 (2024 Remaster)                                https://www.deezer.com/album/560207382
Bounty Killer        - Killer For All Seasons (Raw)                                     https://www.deezer.com/album/961120131
Bounty Killer        - Try Again - Caribbean Riddim (2026 Remaster)                     https://www.deezer.com/album/1007017241
Bounty Killer        - Pot Of Gold Production: Recording Sessions                       https://www.deezer.com/album/1020418181
Brian & Tony Gold    - Tekisha                                                          https://www.deezer.com/album/845232132
Buju Banton          - Everybody Knows (Soul Food Riddim)                               https://www.deezer.com/album/914974761
Buju Banton          - Not Sure (Rapid Burst Riddim)                                    https://www.deezer.com/album/922687191
Capleton             - Gash                                                             https://www.deezer.com/album/74843542
Capleton             - Dancehall Generals:                                              https://www.deezer.com/album/415189547
Capleton             - Zion                                                             https://www.deezer.com/album/938914961
Capleton             - Tek It Off - X5 Riddim (2026 Remaster)                           https://www.deezer.com/album/1035496202
Clement Irie         - Follow Me                                                        https://www.deezer.com/album/774550901
Cocoa Tea            - Authorized (Remastered Edition)                                  https://www.deezer.com/album/726111561
Cocoa Tea            - Mr Cocoa Tea                                                     https://www.deezer.com/album/792123281
Cocoa Tea            - No More Walls (Season 3)                                         https://www.deezer.com/album/860473942
Cocoa Tea            - Camouflage (Don't Test Me Riddim)                                https://www.deezer.com/album/915947251
Culture              - Babylon Can't Study                                              https://www.deezer.com/album/707079561
Culture              - Culture At Work                                                  https://www.deezer.com/album/746100601
Culture              - Nuff Crisis                                                      https://www.deezer.com/album/839368732
Cutty Ranks          - From Mi Heart                                                    https://www.deezer.com/album/67090022
Dean Fraser          - Dub 'N' Sax                                                      https://www.deezer.com/album/634568031
Dean Fraser          - Fever                                                            https://www.deezer.com/album/685542031
Dean Fraser          - Moonlight                                                        https://www.deezer.com/album/892971132
Dennis Brown         - Inseparable: Remastered Edition                                  https://www.deezer.com/album/689759131
Dirtsman             - Hot This Year                                                    https://www.deezer.com/album/1014177521
Elephant Man         - Look (2024 Remaster)                                             https://www.deezer.com/album/625710111
Eric Donaldson       - Trouble In Afrika                                                https://www.deezer.com/album/834302052
Fantan Mojah         - Nuh Trust Yuh (Love Is A Gamble Riddim)                          https://www.deezer.com/album/977678471
Frankie Paul         - Timeless                                                         https://www.deezer.com/album/454663605
Frankie Paul         - Reaching Out                                                     https://www.deezer.com/album/707079621
Freddie McGregor     - Rumours (Remastered Edition)                                     https://www.deezer.com/album/730186791
General Degree       - Home Work - Anything For You Riddim                              https://www.deezer.com/album/1035514902
Gregory Isaacs       - The Best Of Gregory Isaacs                                       https://www.deezer.com/album/790537991
Gregory Isaacs       - Jealousy (2025 Remaster)                                         https://www.deezer.com/album/920964751
Gregory Isaacs       - Love Songs: The Gussie Clarke Years                              https://www.deezer.com/album/942050031
Gregory Isaacs       - Gussie Clarke's Collaborations (Continuous Mix)                  https://www.deezer.com/album/982824491
Gregory Isaacs       - Permanent Lover                                                  https://www.deezer.com/album/1048479672
Gussie Clarke        - Gussie Clarke Presents:                                          https://www.deezer.com/album/631544751
Gussie Clarke        - Gussie Clarke's: Dread At The Controls Dub (Remastered Edition)  https://www.deezer.com/album/707079581
Gussie Clarke        - Black Foundation Dub                                             https://www.deezer.com/album/723450741
Gussie Clarke        - Gussie Clarke's - Mouth Of The Wicked                            https://www.deezer.com/album/741040961
Harold Butler        - Great Reggae Musicians                                           https://www.deezer.com/album/702726961
Heptics              - Lovers Rock Gold: Heptics                                        https://www.deezer.com/album/315850827
Horace Andy          - Every Day People                                                 https://www.deezer.com/album/62655872
Horace Andy          - Exclusively                                                      https://www.deezer.com/album/73210602
Horace Andy          - Skylarking (Skylarking Riddim)                                   https://www.deezer.com/album/946294761
I-Octane             - The Most High Live (Satta Rebirth Riddim)                        https://www.deezer.com/album/926370781
I-Roy                - The Lyrics Man                                                   https://www.deezer.com/album/452863685
I-Roy                - Gussie Clarke's: The Outstanding                                 https://www.deezer.com/album/760080681
Ian Dury             - Lord Upminster                                                   https://www.deezer.com/album/703100601
J.C. Lodge           - Can't Get Over Losing You (2025 Remaster)                        https://www.deezer.com/album/665650321
J.C. Lodge           - I Believe In You (Remastered Edition)                            https://www.deezer.com/album/727357681
Joe Higgs            - Family (Remastered Edition)                                      https://www.deezer.com/album/707252401
John Holt            - Stealing Stealing                                                https://www.deezer.com/album/901949132
Junior Delgado       - Roadblock                                                        https://www.deezer.com/album/807458881
Junior English       - In Loving You (Vocal & Dub)                                      https://www.deezer.com/album/539773982
Junior English       - Lovers Rock Legend                                               https://www.deezer.com/album/557165332
Kumar Fyah           - Behold I Come                                                    https://www.deezer.com/album/921746261
Lexxus               - Cute Song (Puppy Water Riddim)                                   https://www.deezer.com/album/914974871
Lexxus               - Look How Long (Problem Riddim)                                   https://www.deezer.com/album/993952631
Louisa Mark          - Lovers Rock Gold: Louisa Mark                                    https://www.deezer.com/album/353212997
Louisa Mark          - Breakout (deluxe)                                                https://www.deezer.com/album/360132397
Louisa Mark          - 6 Sixth Street                                                   https://www.deezer.com/album/405218097
Maxi Priest          - Merry Go Round (Shine Riddim)                                    https://www.deezer.com/album/996075191
Michael Palmer       - Star Performer                                                   https://www.deezer.com/album/360172297
Mighty Diamonds      - Mighty Diamonds (Remastered Edition)                             https://www.deezer.com/album/727357021
Mighty Diamonds      - The Real Enemy (Remastered Edition)                              https://www.deezer.com/album/737685401
Mighty Diamonds      - Idlers Corner (2025 Remaster)                                    https://www.deezer.com/album/914974921
Mykal Rose           - Quick Fi Shoot                                                   https://www.deezer.com/album/520075642
Nicodemus            - Mr Fabulous                                                      https://www.deezer.com/album/399443767
Ninjaman             - Superstar                                                        https://www.deezer.com/album/399443777
Notch                - Nuttin Nuh Go So (2025 Remaster)                                 https://www.deezer.com/album/797815081
Owen Gray            - Reggae Stream - Owen Gray                                        https://www.deezer.com/album/353205867
Owen Gray            - Dreams                                                           https://www.deezer.com/album/807014831
Paulette Walker      - Lovers Rock Gold: Paulette Walker                                https://www.deezer.com/album/348437017
Peter Chemist        - Dub Prescription                                                 https://www.deezer.com/album/360017587
Pinchers             - Can't Take the Pressure                                          https://www.deezer.com/album/360067677
Prince Phillip Smart - Dubplates & Raw Rhythms From King Tubbys Studio 73 - 76          https://www.deezer.com/album/703714191
Professor Nuts       - Satan Strong (Problem Riddim)                                    https://www.deezer.com/album/996061341
Queen Ifrica         - Wonderful Feelings - Soul Mate Riddim (2026 Remaster)            https://www.deezer.com/album/1036443632
Richie Spice         - Upside Down (Soul Food Riddim)                                   https://www.deezer.com/album/946504851
Richie Spice         - Now & Forever (Pretty Looks Riddim)                              https://www.deezer.com/album/982048901
Roman Stewart        - Ruling & Controlling                                             https://www.deezer.com/album/454663615
Sammy Levi           - Love Is The Message                                              https://www.deezer.com/album/559039742
Sanchez              - REGGAE ICONS: Sanchez                                            https://www.deezer.com/album/593640252
Sanchez              - Falling In Love                                                  https://www.deezer.com/album/942753251
Shabba Ranks         - Golden Touch (2025 Remastered)                                   https://www.deezer.com/album/700406851
Shabba Ranks         - Mr. Maximum (The Remixes)                                        https://www.deezer.com/album/722562991
Shabba Ranks         - Lively Up Yourself                                               https://www.deezer.com/album/834296392
Shabba Ranks         - Pirates Anthem (Long Stream 2025 Remaster)                       https://www.deezer.com/album/922687441
Shabba Ranks         - Turn It Down (2025 Remaster)                                     https://www.deezer.com/album/936696831
Shabba Ranks         - Show Me What You Got (Platinum Riddim)                           https://www.deezer.com/album/992630721
Shelly Thunder       - Small Horsewoman                                                 https://www.deezer.com/album/406079377
Shinehead            - Rough & Rugged                                                   https://www.deezer.com/album/362325267
Singing Melody       - Original                                                         https://www.deezer.com/album/794120241
Sizzla               - Say You Love Me - X5 Riddim (2026 Remaster)                      https://www.deezer.com/album/1035496422
Soljie               - Rebel Soldier                                                    https://www.deezer.com/album/362308317
Sonia Ferguson       - Lovers Rock Gold                                                 https://www.deezer.com/album/353237977
Sonia Ferguson       - Magic Lady                                                       https://www.deezer.com/album/851730752
Spice                - Mi Nuh Like Dat                                                  https://www.deezer.com/album/938915181
Sugar Belly          - The Return of the Sugar Belly                                    https://www.deezer.com/album/353417227
Sugar Minott         - Inna Reggae Dance Hall                                           https://www.deezer.com/album/355192837
Sugar Minott         - Sufferer's Choice                                                https://www.deezer.com/album/360168587
Sugar Minott         - Reggae Generals: Sugar Minott                                    https://www.deezer.com/album/635586441
Tanya Stephens       - A We A Spend (Scream Riddim)                                     https://www.deezer.com/album/959348781
Tappa Zukie          - Man Ah Warrior                                                   https://www.deezer.com/album/348411457
Tappa Zukie          - Reggae Stream                                                    https://www.deezer.com/album/353429697
Tarrus Riley         - Whispers (Shine Riddim)                                          https://www.deezer.com/album/996417461
Tenor Saw            - Fever                                                            https://www.deezer.com/album/348962847
Tenor Saw            - Dub Fever                                                        https://www.deezer.com/album/353316877
Tony Tuff            - Tuff Selection                                                   https://www.deezer.com/album/65801932
Tony Tuff            - Ketch A Fire                                                     https://www.deezer.com/album/702727081
Tony Tuff            - Girl I've Got To Get You (2026 Remaster)                         https://www.deezer.com/album/996535681
Trevor Walters       - Lovers Rock Gold: Trevor Walters                                 https://www.deezer.com/album/348410027
Various Artists      - Double Dose - Gregory Isaacs & Sugar Minott                      https://www.deezer.com/album/348964287
Various Artists      - Kings of Lovers Rock                                             https://www.deezer.com/album/353217917
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/353223667
Various Artists      - The Best Lovers Rock Songs                                       https://www.deezer.com/album/353285707
Various Artists      - Reggae Stream                                                    https://www.deezer.com/album/353404127
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/353426877
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/353717877
Various Artists      - Reggae Stream                                                    https://www.deezer.com/album/355218817
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/355222087
Various Artists      - Reggae Stream                                                    https://www.deezer.com/album/356961117
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/359890537
Various Artists      - Mr Vibes                                                         https://www.deezer.com/album/373758257
Various Artists      - 1999 Dub                                                         https://www.deezer.com/album/373789277
Various Artists      - Reggae Riddim: Praises                                           https://www.deezer.com/album/374885597
Various Artists      - Reggae Dancehall Riddim: Scorcher                                https://www.deezer.com/album/374885647
Various Artists      - Reggae Riddim: Declaration of Rights                             https://www.deezer.com/album/375487417
Various Artists      - Reggae Dancehall Riddim: Baby Doll                               https://www.deezer.com/album/375489097
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/384099577
Various Artists      - Dancehall Riddim: Anthem                                         https://www.deezer.com/album/384910907
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/384939577
Various Artists      - Queens of Lovers Rock                                            https://www.deezer.com/album/384942947
Various Artists      - Super Clash                                                      https://www.deezer.com/album/399139217
Various Artists      - Barrington Levy Meets Cocoa Tea                                  https://www.deezer.com/album/406854047
Various Artists      - Clash                                                            https://www.deezer.com/album/406854127
Various Artists      - Dancehall Riddim: Nookie 2K6                                     https://www.deezer.com/album/412713957
Various Artists      - Reggae Generals:                                                 https://www.deezer.com/album/413517657
Various Artists      - Reggae Dancehall Riddim                                          https://www.deezer.com/album/413880587
Various Artists      - Reggae Generals:                                                 https://www.deezer.com/album/413886657
Various Artists      - Dancehall Riddim: Wha Do Dem                                     https://www.deezer.com/album/414434187
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/416282167
Various Artists      - Dancehall Generals:                                              https://www.deezer.com/album/418084227
Various Artists      - Super Clash                                                      https://www.deezer.com/album/425975587
Various Artists      - Super Clash                                                      https://www.deezer.com/album/430872717
Various Artists      - Reggae Dancehall Riddim: The Exit                                https://www.deezer.com/album/433860837
Various Artists      - Reggae Dancehall Riddim: Teach The Youths                        https://www.deezer.com/album/433861527
Various Artists      - Reggae Dancehall Riddim: Kuff                                    https://www.deezer.com/album/434472657
Various Artists      - Dub Masters                                                      https://www.deezer.com/album/448145895
Various Artists      - Dancehall Riddim: Rush                                           https://www.deezer.com/album/520879492
Various Artists      - Dancehall Riddim: G String                                       https://www.deezer.com/album/520995612
Various Artists      - Tony "CD" Kelly Presents: Dancehall Love (Remastered 2024)       https://www.deezer.com/album/540949602
Various Artists      - Reggae Dancehall Riddim: Run Down The World                      https://www.deezer.com/album/543805982
Various Artists      - Reggae Trio                                                      https://www.deezer.com/album/543806842
Various Artists      - Witty Hifi                                                       https://www.deezer.com/album/544700382
Various Artists      - Reggae Dancehall Riddim: Signs                                   https://www.deezer.com/album/545404262
Various Artists      - Dancehall Riddim: Candle Wax                                     https://www.deezer.com/album/551782192
Various Artists      - Tony "CD" Kelly Presents: Dancehall Vibes                        https://www.deezer.com/album/551872342
Various Artists      - Dancehall Riddim: Callaloo Bed                                   https://www.deezer.com/album/558752812
Various Artists      - John John Presents: Dancehall Party                              https://www.deezer.com/album/559298372
Various Artists      - Dancehall 420                                                    https://www.deezer.com/album/559318022
Various Artists      - Conscious Reggae                                                 https://www.deezer.com/album/559704782
Various Artists      - Now This Is An Anthem                                            https://www.deezer.com/album/562040342
Various Artists      - John John Dancehall Riddims: Anthrax                             https://www.deezer.com/album/597265382
Various Artists      - John John Dancehall Riddims: Peanie Peanie                       https://www.deezer.com/album/603527512
Various Artists      - John John Dancehall Riddims: G String                            https://www.deezer.com/album/603561972
Various Artists      - John John Dancehall Riddims: Target                              https://www.deezer.com/album/607850652
Various Artists      - John John Dancehall Riddims: The Mix                             https://www.deezer.com/album/607852932
Various Artists      - Trouble Backstage                                                https://www.deezer.com/album/631314271
Various Artists      - Gussie Clarke Classics                                           https://www.deezer.com/album/633434291
Various Artists      - Mikey Bennett Presents: The Lover Man Riddim                     https://www.deezer.com/album/634563381
Various Artists      - John John Reggae Riddims: Fuss & Fight                           https://www.deezer.com/album/635493821
Various Artists      - Tony Kelly Presents: Dancehall Vibes                             https://www.deezer.com/album/635549501
Various Artists      - John John Dancehall Riddims: Cash Register                       https://www.deezer.com/album/639725401
Various Artists      - Willie Lindo Presents: Love Bump Riddim (2025 Remaster)          https://www.deezer.com/album/674221891
Various Artists      - Gussie Clarke's Ladies                                           https://www.deezer.com/album/679876181
Various Artists      - Irie & Mellow                                                    https://www.deezer.com/album/689754471
Various Artists      - Sweet Reggae Music                                               https://www.deezer.com/album/690496051
Various Artists      - Sweet Reggae Music                                               https://www.deezer.com/album/690917051
Various Artists      - Reggae Instrumentalists                                          https://www.deezer.com/album/693364351
Various Artists      - Reggae Lovers                                                    https://www.deezer.com/album/693366581
Various Artists      - Tony Kelly Presents: Dancehall Vibes                             https://www.deezer.com/album/694146721
Various Artists      - Dancehall Riddim: Overdose                                       https://www.deezer.com/album/695068411
Various Artists      - Reggae Riddim: One In Ten                                        https://www.deezer.com/album/695469481
Various Artists      - Dancehall Riddim: Assault Rifle                                  https://www.deezer.com/album/695469841
Various Artists      - The Roots Is There (Deluxe Edition)                              https://www.deezer.com/album/695720171
Various Artists      - Mikey Bennett's: Golden Touch Riddim                             https://www.deezer.com/album/700706851
Various Artists      - Mikey Bennett's: The Gangster Riddim                             https://www.deezer.com/album/700708291
Various Artists      - Reggae Groups: Tetrack                                           https://www.deezer.com/album/701843001
Various Artists      - Dancehall Riddim: Candle Wax (Sped Up)                           https://www.deezer.com/album/704271071
Various Artists      - Irie & Mellow                                                    https://www.deezer.com/album/711246401
Various Artists      - Pirates Anthem (2025 Remastered)                                 https://www.deezer.com/album/716427091
Various Artists      - Red Rose For Gregory (Remastered Edition)                        https://www.deezer.com/album/723406821
Various Artists      - Gussie Clarke Reggae Masters                                     https://www.deezer.com/album/723451451
Various Artists      - No Contest (Remastered Edition)                                  https://www.deezer.com/album/723706641
Various Artists      - Deborahe Glasgow (Remastered Edition)                            https://www.deezer.com/album/730545801
Various Artists      - Legit                                                            https://www.deezer.com/album/732616091
Various Artists      - Judge Not                                                        https://www.deezer.com/album/732618161
Various Artists      - Hopeton Lindo Meets Robert Ffrench                               https://www.deezer.com/album/739365711
Various Artists      - Sound On Fire Riddim                                             https://www.deezer.com/album/761469821
Various Artists      - Wibble Wabble                                                    https://www.deezer.com/album/767203141
Various Artists      - The Going Is Rough                                               https://www.deezer.com/album/767203771
Various Artists      - Gideon Riddim                                                    https://www.deezer.com/album/767317861
Various Artists      - Rapid Burst Riddim                                               https://www.deezer.com/album/768578721
Various Artists      - Twin Spin                                                        https://www.deezer.com/album/774551441
Various Artists      - John John Reggae Riddims: Inna Rub A Dub Style                   https://www.deezer.com/album/774551651
Various Artists      - Reggae Dancehall Riddim: Kross Fever                             https://www.deezer.com/album/781120191
Various Artists      - Furnace Riddim                                                   https://www.deezer.com/album/781691381
Various Artists      - 8 Ball Riddim                                                    https://www.deezer.com/album/782274511
Various Artists      - Fresh Air                                                        https://www.deezer.com/album/782863891
Various Artists      - Baba Boom Riddim                                                 https://www.deezer.com/album/782962171
Various Artists      - More Dancehall: Ruckus Riddim                                    https://www.deezer.com/album/784649191
Various Artists      - More Dancehall: Scream Riddim                                    https://www.deezer.com/album/784649391
Various Artists      - More Dancehall: Hurricane Riddim                                 https://www.deezer.com/album/787963251
Various Artists      - More Dancehall: The Flip Riddim                                  https://www.deezer.com/album/788526291
Various Artists      - Escalade Riddim                                                  https://www.deezer.com/album/794340291
Various Artists      - More Dancehall: Headache Riddim                                  https://www.deezer.com/album/795248881
Various Artists      - Most Wanted Riddim                                               https://www.deezer.com/album/797672371
Various Artists      - Antz Nest Riddim                                                 https://www.deezer.com/album/797720171
Various Artists      - Gussie Clarke's Master Collection                                https://www.deezer.com/album/797834281
Various Artists      - Razor Blade Riddim                                               https://www.deezer.com/album/799033241
Various Artists      - Room In My Father's House                                        https://www.deezer.com/album/799547451
Various Artists      - John John Reggae Riddims: Zion Gate                              https://www.deezer.com/album/800272911
Various Artists      - Gussie Clarke's Master Collection                                https://www.deezer.com/album/824165031
Various Artists      - Every Time You Go Away Riddim                                    https://www.deezer.com/album/836066972
Various Artists      - Gussie Clarke's Rumours Riddim                                   https://www.deezer.com/album/837106302
Various Artists      - No More Walls (Season 2)                                         https://www.deezer.com/album/856813122
Various Artists      - Mikey Bennett's Poison Riddim                                    https://www.deezer.com/album/896753792
Various Artists      - Gussie Clarkes: Mind Yuh Dis - Rude Bwoy Style                   https://www.deezer.com/album/902119302
Various Artists      - Gussie Clarkes: Holding On Riddim                                https://www.deezer.com/album/903229402
Various Artists      - Gussie Clarkes: Fatal Attraction - Dancehall Style               https://www.deezer.com/album/903748692
Various Artists      - Gussie Clarke's Reggae Dancehall Collaborations                  https://www.deezer.com/album/910931741
Various Artists      - More Dancehall: Jiggy (Jiggy Riddim)                             https://www.deezer.com/album/914876521
Various Artists      - Y2K Dancehall Gold (Punnany Riddim)                              https://www.deezer.com/album/923376511
Various Artists      - Twice My Age Riddim                                              https://www.deezer.com/album/923464001
Various Artists      - Y2K Dancehall Gold (Step Father Riddim)                          https://www.deezer.com/album/923979541
Various Artists      - Y2K Dancehall Gold (Uptown Riddim)                               https://www.deezer.com/album/923981441
Various Artists      - Queens Of Lovers Rock                                            https://www.deezer.com/album/926988391
Various Artists      - Y2K Dancehall Gold (Paranoid Riddim)                             https://www.deezer.com/album/930448371
Various Artists      - Don't Test Me                                                    https://www.deezer.com/album/939732341
Various Artists      - Y2K Dancehall Roots: Belview Riddim                              https://www.deezer.com/album/945318721
Various Artists      - Y2K Dancehall Gold: Belview Riddim                               https://www.deezer.com/album/945457701
Various Artists      - Y2K Dancehall Gold: Rapid Burst                                  https://www.deezer.com/album/966367801
Various Artists      - Y2K Reggae Gold: Skylarking Riddim                               https://www.deezer.com/album/977663861
Various Artists      - Y2K Dancehall Gold: Acid Riddim                                  https://www.deezer.com/album/982298891
Various Artists      - Y2K Dancehall Gold: Kasablanca Riddim                            https://www.deezer.com/album/983049891
Various Artists      - Y2K Acoustic Dancehall Gold: Soul Food Riddim                    https://www.deezer.com/album/987491151
Various Artists      - More Dancehall: Ruckus Riddim - The Sequel                       https://www.deezer.com/album/998275501
Various Artists      - Dancehall 00's                                                   https://www.deezer.com/album/1002491031
Various Artists      - A Love I Can Feel                                                https://www.deezer.com/album/1002785771
Various Artists      - Y2K Dancehall: Problem Riddim                                    https://www.deezer.com/album/1002785781
Various Artists      - Y2K Reggae: Shine Riddim                                         https://www.deezer.com/album/1018317381
Various Artists      - Great Reggae Musicians                                           https://www.deezer.com/album/1028388312
Various Artists      - Gussie Clarke's Reggae Dancehall Collaborations, Vol. 2          https://www.deezer.com/album/1033490612
Various Artists      - Dancehall Dons                                                   https://www.deezer.com/album/1033938002
Various Artists      - Now This Is An Anthem, Vol. 2                                    https://www.deezer.com/album/1039669722
Various Artists      - Roots & Culture                                                  https://www.deezer.com/album/1046127072
Various Artists      - Anything For You Riddim                                          https://www.deezer.com/album/1046752002
Various Artists      - Dancehall Dons                                                   https://www.deezer.com/album/1047919812
Vybz Kartel          - A John John Masterpiece                                          https://www.deezer.com/album/794238901
Vybz Kartel          - Puff It (Step Father Riddim)                                     https://www.deezer.com/album/911665391
Vybz Kartel          - Good Like Gold (Step Father Riddim)                              https://www.deezer.com/album/911666101
Vybz Kartel          - Baby Father (Uptown Riddim)                                      https://www.deezer.com/album/911666171
Vybz Kartel          - War Start                                                        https://www.deezer.com/album/939080001
Vybz Kartel          - Friend Of Mine (Scream Riddim)                                   https://www.deezer.com/album/960350611
Vybz Kartel          - Cruising (Ruckus Riddim)                                         https://www.deezer.com/album/961281941
Vybz Kartel          - Badda Dan Dem                                                    https://www.deezer.com/album/962884901
Wayne Wade           - I Love You Too Much                                              https://www.deezer.com/album/690917991
Wayne Wonder         - Anything Goes (Remastered 2024)                                  https://www.deezer.com/album/555780222
Willie Lindo         - Reggae Machine                                                   https://www.deezer.com/album/693361631
```
