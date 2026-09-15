# deezlabel

Simple script to find the label a particular Deezer album/track is on and print 
a list of all other albums on the service from the same label.

Mostly Claude's work with a little sanity checking by me.

#### Example

```
rez@laptop:~/deezlabel$ ./deezlabel.py https://www.deezer.com/en/album/434472657 
Label: Reggae Library

Admiral Bailey        - Super Clash                                                      https://www.deezer.com/album/399139217
Aidonia               - Y2K Dancehall Gold (Punnany Riddim)                              https://www.deezer.com/album/923376511
Al Campbell           - Reggae Dancehall Riddim: Run Down The World                      https://www.deezer.com/album/543805982
Alton Ellis           - Jamaican Rock                                                    https://www.deezer.com/album/353333427
Alton Ellis           - Reggae Trio                                                      https://www.deezer.com/album/355222087
Alton Ellis           - Here I Am - Reggae Got Soul                                      https://www.deezer.com/album/359576277
Alton Ellis           - Love to Share                                                    https://www.deezer.com/album/362304517
Augustus Pablo        - The Early Years                                                  https://www.deezer.com/album/372971107
Augustus Pablo        - Great Reggae Musicians                                           https://www.deezer.com/album/1028388312
Barrington Levy       - Sister Debby                                                     https://www.deezer.com/album/353308627
Barrington Levy       - Making Tracks                                                    https://www.deezer.com/album/362302907
Barrington Levy       - Barrington Levy Meets Cocoa Tea                                  https://www.deezer.com/album/406854047
Barrington Levy       - Reggae Dancehall Riddim: Teach The Youths                        https://www.deezer.com/album/433861527
Barrington Levy       - Now This Is An Anthem                                            https://www.deezer.com/album/562040342
Barrington Levy       - Mr Robber Man                                                    https://www.deezer.com/album/927726281
Beenie Man            - Reggae Dancehall Riddim: Baby Doll                               https://www.deezer.com/album/375489097
Beenie Man            - Dancehall Generals:                                              https://www.deezer.com/album/415176737
Beenie Man            - Dancehall Riddim: Rush                                           https://www.deezer.com/album/520879492
Beenie Man            - Dancehall 420                                                    https://www.deezer.com/album/559318022
Beenie Man            - Most Wanted Riddim                                               https://www.deezer.com/album/797672371
Beenie Man            - Antz Nest Riddim                                                 https://www.deezer.com/album/797720171
Beenie Man            - Razor Blade Riddim                                               https://www.deezer.com/album/799033241
Beenie Man            - Somebody (Step Father Riddim)                                    https://www.deezer.com/album/911580671
Beenie Man            - Your Bad Luck (Hurricane Riddim)                                 https://www.deezer.com/album/914876531
Beenie Man            - Dem No Know Badness                                              https://www.deezer.com/album/920026061
Beenie Man            - Y2K Dancehall Gold (Paranoid Riddim)                             https://www.deezer.com/album/930448371
Beenie Man            - Hit With Music                                                   https://www.deezer.com/album/938914951
Beenie Man            - 100 Dollar Bag                                                   https://www.deezer.com/album/943218051
Beenie Man            - Good Jamaica - Impact Riddim                                     https://www.deezer.com/album/956843651
Beenie Man            - Bandi Legs (Raw)                                                 https://www.deezer.com/album/961119861
Beenie Man            - Y2K Dancehall Gold: Rapid Burst                                  https://www.deezer.com/album/966367801
Beenie Man            - Y2K Acoustic Dancehall Gold: Soul Food Riddim                    https://www.deezer.com/album/987491151
Beenie Man            - Ganja Farm (Problem Riddim)                                      https://www.deezer.com/album/993567461
Beenie Man            - Dancehall 00's                                                   https://www.deezer.com/album/1002491031
Beenie Man            - Y2K Dancehall: Problem Riddim                                    https://www.deezer.com/album/1002785781
Beenie Man            - Oh La La La - Caribbean Riddim (2026 Remaster)                   https://www.deezer.com/album/1004379851
Beenie Man            - Tata Fool                                                        https://www.deezer.com/album/1035536832
Beres Hammond         - La La La                                                         https://www.deezer.com/album/73209632
Beres Hammond         - Reggae Generals:                                                 https://www.deezer.com/album/413517657
Beres Hammond         - Soul                                                             https://www.deezer.com/album/624888521
Beres Hammond         - REGGAE ICONS: Beres Hammond                                      https://www.deezer.com/album/634574981
Beres Hammond         - Irie & Mellow                                                    https://www.deezer.com/album/689754471
Beres Hammond         - Sweet Reggae Music                                               https://www.deezer.com/album/690917051
Beres Hammond         - Beres Hammond: Remastered Edition                                https://www.deezer.com/album/705662361
Beres Hammond         - Love Is Stronger                                                 https://www.deezer.com/album/932570561
Beres Hammond         - What A Night (2026 Remaster)                                     https://www.deezer.com/album/956802011
Beres Hammond         - Fight To Defend It (Love Is Not A Gamble Riddim)                 https://www.deezer.com/album/962835501
Beres Hammond         - Dancing Beauty                                                   https://www.deezer.com/album/993447821
Black Uhuru           - Reggae Stream                                                    https://www.deezer.com/album/355218817
Boris Gardiner        - I Wanna Wake Up With You                                         https://www.deezer.com/album/677465751
Boris Gardiner        - Sweet Reggae Music                                               https://www.deezer.com/album/690496051
Boris Gardiner        - I Wanna Wake Up With You                                         https://www.deezer.com/album/998253731
Bounty Killer         - Dancehall Riddim: Candle Wax                                     https://www.deezer.com/album/551782192
Bounty Killer         - Revolution, Pt. 3 (2024 Remaster)                                https://www.deezer.com/album/560207382
Bounty Killer         - Dancehall Riddim: Overdose                                       https://www.deezer.com/album/695068411
Bounty Killer         - Killer For All Seasons (Raw)                                     https://www.deezer.com/album/961120131
Bounty Killer         - Y2K Dancehall Gold: Acid Riddim                                  https://www.deezer.com/album/982298891
Bounty Killer         - Try Again - Caribbean Riddim (2026 Remaster)                     https://www.deezer.com/album/1007017241
Bounty Killer         - Pot Of Gold Production: Recording Sessions                       https://www.deezer.com/album/1020418181
Brian & Tony Gold     - Tekisha                                                          https://www.deezer.com/album/845232132
Buju Banton           - Reggae Dancehall Riddim: Scorcher                                https://www.deezer.com/album/374885647
Buju Banton           - Dancehall Riddim: Anthem                                         https://www.deezer.com/album/384910907
Buju Banton           - Dancehall Riddim: Nookie 2K6                                     https://www.deezer.com/album/412713957
Buju Banton           - Dancehall Riddim: Wha Do Dem                                     https://www.deezer.com/album/414434187
Buju Banton           - Dancehall Riddim: Callaloo Bed                                   https://www.deezer.com/album/558752812
Buju Banton           - John John Dancehall Riddims: Anthrax                             https://www.deezer.com/album/597265382
Buju Banton           - John John Dancehall Riddims: G String                            https://www.deezer.com/album/603561972
Buju Banton           - Tony Kelly Presents: Dancehall Vibes                             https://www.deezer.com/album/635549501
Buju Banton           - Tony Kelly Presents: Dancehall Vibes                             https://www.deezer.com/album/694146721
Buju Banton           - Reggae Riddim: One In Ten                                        https://www.deezer.com/album/695469481
Buju Banton           - Dancehall Riddim: Candle Wax (Sped Up)                           https://www.deezer.com/album/704271071
Buju Banton           - Rapid Burst Riddim                                               https://www.deezer.com/album/768578721
Buju Banton           - Baba Boom Riddim                                                 https://www.deezer.com/album/782962171
Buju Banton           - More Dancehall: Ruckus Riddim                                    https://www.deezer.com/album/784649191
Buju Banton           - Escalade Riddim                                                  https://www.deezer.com/album/794340291
Buju Banton           - Everybody Knows (Soul Food Riddim)                               https://www.deezer.com/album/914974761
Buju Banton           - Not Sure (Rapid Burst Riddim)                                    https://www.deezer.com/album/922687191
Busy Signal           - John John Presents: Dancehall Party                              https://www.deezer.com/album/559298372
Capleton              - Gash                                                             https://www.deezer.com/album/74843542
Capleton              - Reggae Dancehall Riddim                                          https://www.deezer.com/album/413880587
Capleton              - Dancehall Generals:                                              https://www.deezer.com/album/415189547
Capleton              - More Dancehall: Hurricane Riddim                                 https://www.deezer.com/album/787963251
Capleton              - Zion                                                             https://www.deezer.com/album/938914961
Capleton              - Y2K Dancehall Roots: Belview Riddim                              https://www.deezer.com/album/945318721
Capleton              - Tek It Off - X5 Riddim (2026 Remaster)                           https://www.deezer.com/album/1035496202
Cassandra             - Reggae Stream                                                    https://www.deezer.com/album/356961117
Cassandra             - Queens of Lovers Rock                                            https://www.deezer.com/album/384942947
Chaka Demus           - Super Clash                                                      https://www.deezer.com/album/430872717
Clement Irie          - Follow Me                                                        https://www.deezer.com/album/774550901
Cocoa Tea             - Authorized (Remastered Edition)                                  https://www.deezer.com/album/726111561
Cocoa Tea             - Mr Cocoa Tea                                                     https://www.deezer.com/album/792123281
Cocoa Tea             - Room In My Father's House                                        https://www.deezer.com/album/799547451
Cocoa Tea             - Gussie Clarke's Master Collection                                https://www.deezer.com/album/824165031
Cocoa Tea             - No More Walls (Season 3)                                         https://www.deezer.com/album/860473942
Cocoa Tea             - Mikey Bennett's Poison Riddim                                    https://www.deezer.com/album/896753792
Cocoa Tea             - Gussie Clarkes: Holding On Riddim                                https://www.deezer.com/album/903229402
Cocoa Tea             - Gussie Clarkes: Fatal Attraction - Dancehall Style               https://www.deezer.com/album/903748692
Cocoa Tea             - Camouflage (Don't Test Me Riddim)                                https://www.deezer.com/album/915947251
Culture               - Babylon Can't Study                                              https://www.deezer.com/album/707079561
Culture               - Culture At Work                                                  https://www.deezer.com/album/746100601
Culture               - Nuff Crisis                                                      https://www.deezer.com/album/839368732
Cutty Ranks           - From Mi Heart                                                    https://www.deezer.com/album/67090022
Cutty Ranks           - Mikey Bennett's: The Gangster Riddim                             https://www.deezer.com/album/700708291
Cutty Ranks           - The Going Is Rough                                               https://www.deezer.com/album/767203771
Cutty Ranks           - Dancehall Dons                                                   https://www.deezer.com/album/1047919812
Dean Fraser           - Dub 'N' Sax                                                      https://www.deezer.com/album/634568031
Dean Fraser           - Fever                                                            https://www.deezer.com/album/685542031
Dean Fraser           - Reggae Instrumentalists                                          https://www.deezer.com/album/693364351
Dean Fraser           - Moonlight                                                        https://www.deezer.com/album/892971132
Deborahe Glasgow      - Deborahe Glasgow (Remastered Edition)                            https://www.deezer.com/album/730545801
Dennis Brown          - Inseparable: Remastered Edition                                  https://www.deezer.com/album/689759131
Dennis Brown          - No More Walls (Season 2)                                         https://www.deezer.com/album/856813122
Dirtsman              - Hot This Year                                                    https://www.deezer.com/album/1014177521
Earl Cunningham       - Reggae Trio                                                      https://www.deezer.com/album/384939577
Elephant Man          - Look (2024 Remaster)                                             https://www.deezer.com/album/625710111
Elephant Man          - More Dancehall: Jiggy (Jiggy Riddim)                             https://www.deezer.com/album/914876521
Eric Donaldson        - Trouble In Afrika                                                https://www.deezer.com/album/834302052
Fantan Mojah          - Nuh Trust Yuh (Love Is A Gamble Riddim)                          https://www.deezer.com/album/977678471
Frankie Paul          - Timeless                                                         https://www.deezer.com/album/454663605
Frankie Paul          - Reaching Out                                                     https://www.deezer.com/album/707079621
Freddie McGregor      - Rumours (Remastered Edition)                                     https://www.deezer.com/album/730186791
Freddie McGregor      - Legit                                                            https://www.deezer.com/album/732616091
Freddie McGregor      - Gussie Clarke's Master Collection                                https://www.deezer.com/album/797834281
General Degree        - Home Work - Anything For You Riddim                              https://www.deezer.com/album/1035514902
Gregory Isaacs        - Double Dose - Gregory Isaacs & Sugar Minott                      https://www.deezer.com/album/348964287
Gregory Isaacs        - Reggae Riddim: Declaration of Rights                             https://www.deezer.com/album/375487417
Gregory Isaacs        - Reggae Trio                                                      https://www.deezer.com/album/543806842
Gregory Isaacs        - Gussie Clarke Classics                                           https://www.deezer.com/album/633434291
Gregory Isaacs        - Mikey Bennett Presents: The Lover Man Riddim                     https://www.deezer.com/album/634563381
Gregory Isaacs        - Red Rose For Gregory (Remastered Edition)                        https://www.deezer.com/album/723406821
Gregory Isaacs        - No Contest (Remastered Edition)                                  https://www.deezer.com/album/723706641
Gregory Isaacs        - Judge Not                                                        https://www.deezer.com/album/732618161
Gregory Isaacs        - Sound On Fire Riddim                                             https://www.deezer.com/album/761469821
Gregory Isaacs        - Reggae Dancehall Riddim: Kross Fever                             https://www.deezer.com/album/781120191
Gregory Isaacs        - The Best Of Gregory Isaacs                                       https://www.deezer.com/album/790537991
Gregory Isaacs        - Gussie Clarke's Rumours Riddim                                   https://www.deezer.com/album/837106302
Gregory Isaacs        - Gussie Clarkes: Mind Yuh Dis - Rude Bwoy Style                   https://www.deezer.com/album/902119302
Gregory Isaacs        - Jealousy (2025 Remaster)                                         https://www.deezer.com/album/920964751
Gregory Isaacs        - Love Songs: The Gussie Clarke Years                              https://www.deezer.com/album/942050031
Gregory Isaacs        - Gussie Clarke's Collaborations (Continuous Mix)                  https://www.deezer.com/album/982824491
Gregory Isaacs        - Permanent Lover                                                  https://www.deezer.com/album/1048479672
Gussie Clarke         - Gussie Clarke Presents:                                          https://www.deezer.com/album/631544751
Gussie Clarke         - Gussie Clarke's: Dread At The Controls Dub (Remastered Edition)  https://www.deezer.com/album/707079581
Gussie Clarke         - Black Foundation Dub                                             https://www.deezer.com/album/723450741
Gussie Clarke         - Gussie Clarke's - Mouth Of The Wicked                            https://www.deezer.com/album/741040961
Half Pint             - Reggae Trio                                                      https://www.deezer.com/album/359890537
Harold Butler         - Great Reggae Musicians                                           https://www.deezer.com/album/702726961
Heptics               - Lovers Rock Gold: Heptics                                        https://www.deezer.com/album/315850827
Home T                - Pirates Anthem (2025 Remastered)                                 https://www.deezer.com/album/716427091
Hopeton Lindo         - Hopeton Lindo Meets Robert Ffrench                               https://www.deezer.com/album/739365711
Horace Andy           - Every Day People                                                 https://www.deezer.com/album/62655872
Horace Andy           - Exclusively                                                      https://www.deezer.com/album/73210602
Horace Andy           - Gussie Clarke Reggae Masters                                     https://www.deezer.com/album/723451451
Horace Andy           - Skylarking (Skylarking Riddim)                                   https://www.deezer.com/album/946294761
Horace Andy           - Y2K Reggae Gold: Skylarking Riddim                               https://www.deezer.com/album/977663861
I-Octane              - The Most High Live (Satta Rebirth Riddim)                        https://www.deezer.com/album/926370781
I-Roy                 - The Lyrics Man                                                   https://www.deezer.com/album/452863685
I-Roy                 - Gussie Clarke's: The Outstanding                                 https://www.deezer.com/album/760080681
Ian Dury              - Lord Upminster                                                   https://www.deezer.com/album/703100601
J.C. Lodge            - Can't Get Over Losing You (2025 Remaster)                        https://www.deezer.com/album/665650321
J.C. Lodge            - Gussie Clarke's Ladies                                           https://www.deezer.com/album/679876181
J.C. Lodge            - Irie & Mellow                                                    https://www.deezer.com/album/711246401
J.C. Lodge            - I Believe In You (Remastered Edition)                            https://www.deezer.com/album/727357681
Jah Cure              - Reggae Riddim: Praises                                           https://www.deezer.com/album/374885597
Jah Cure              - Gideon Riddim                                                    https://www.deezer.com/album/767317861
Joe Higgs             - Family (Remastered Edition)                                      https://www.deezer.com/album/707252401
John Holt             - Stealing Stealing                                                https://www.deezer.com/album/901949132
Joseph Benaiah        - Reggae Lovers                                                    https://www.deezer.com/album/693366581
Junior Delgado        - Roadblock                                                        https://www.deezer.com/album/807458881
Junior English        - In Loving You (Vocal & Dub)                                      https://www.deezer.com/album/539773982
Junior English        - Lovers Rock Legend                                               https://www.deezer.com/album/557165332
Junior Reid           - Fresh Air                                                        https://www.deezer.com/album/782863891
Kumar Fyah            - Behold I Come                                                    https://www.deezer.com/album/921746261
Lexxus                - Cute Song (Puppy Water Riddim)                                   https://www.deezer.com/album/914974871
Lexxus                - Look How Long (Problem Riddim)                                   https://www.deezer.com/album/993952631
Louisa Mark           - Lovers Rock Gold: Louisa Mark                                    https://www.deezer.com/album/353212997
Louisa Mark           - Breakout (deluxe)                                                https://www.deezer.com/album/360132397
Louisa Mark           - 6 Sixth Street                                                   https://www.deezer.com/album/405218097
Louisa Mark           - Queens Of Lovers Rock                                            https://www.deezer.com/album/926988391
Mad Cobra             - 8 Ball Riddim                                                    https://www.deezer.com/album/782274511
Maxi Priest           - Merry Go Round (Shine Riddim)                                    https://www.deezer.com/album/996075191
Maxi Priest           - Y2K Reggae: Shine Riddim                                         https://www.deezer.com/album/1018317381
Michael Palmer        - Star Performer                                                   https://www.deezer.com/album/360172297
Mighty Diamonds       - Trouble Backstage                                                https://www.deezer.com/album/631314271
Mighty Diamonds       - The Roots Is There (Deluxe Edition)                              https://www.deezer.com/album/695720171
Mighty Diamonds       - Mighty Diamonds (Remastered Edition)                             https://www.deezer.com/album/727357021
Mighty Diamonds       - The Real Enemy (Remastered Edition)                              https://www.deezer.com/album/737685401
Mighty Diamonds       - Idlers Corner (2025 Remaster)                                    https://www.deezer.com/album/914974921
Mykal Rose            - Quick Fi Shoot                                                   https://www.deezer.com/album/520075642
Nicodemus             - Mr Fabulous                                                      https://www.deezer.com/album/399443767
Ninjaman              - Superstar                                                        https://www.deezer.com/album/399443777
Notch                 - Nuttin Nuh Go So (2025 Remaster)                                 https://www.deezer.com/album/797815081
Owen Gray             - Reggae Stream - Owen Gray                                        https://www.deezer.com/album/353205867
Owen Gray             - Reggae Trio                                                      https://www.deezer.com/album/384099577
Owen Gray             - Dreams                                                           https://www.deezer.com/album/807014831
Pablo Gad             - Reggae Trio                                                      https://www.deezer.com/album/353426877
Paulette Walker       - Lovers Rock Gold: Paulette Walker                                https://www.deezer.com/album/348437017
Peter Chemist         - Dub Prescription                                                 https://www.deezer.com/album/360017587
Peter Chemist         - 1999 Dub                                                         https://www.deezer.com/album/373789277
Peter Hunnigale       - Mr Vibes                                                         https://www.deezer.com/album/373758257
Pinchers              - Can't Take the Pressure                                          https://www.deezer.com/album/360067677
Prince Phillip Smart  - Dubplates & Raw Rhythms From King Tubbys Studio 73 - 76          https://www.deezer.com/album/703714191
Professor Nuts        - Satan Strong (Problem Riddim)                                    https://www.deezer.com/album/996061341
Queen Ifrica          - Wonderful Feelings - Soul Mate Riddim (2026 Remaster)            https://www.deezer.com/album/1036443632
RDX                   - Wibble Wabble                                                    https://www.deezer.com/album/767203141
Richie Spice          - Upside Down (Soul Food Riddim)                                   https://www.deezer.com/album/946504851
Richie Spice          - Now & Forever (Pretty Looks Riddim)                              https://www.deezer.com/album/982048901
Roman Stewart         - Ruling & Controlling                                             https://www.deezer.com/album/454663615
Sammy Levi            - Love Is The Message                                              https://www.deezer.com/album/559039742
Sanchez               - REGGAE ICONS: Sanchez                                            https://www.deezer.com/album/593640252
Sanchez               - Falling In Love                                                  https://www.deezer.com/album/942753251
Sasha                 - Tony "CD" Kelly Presents: Dancehall Love (Remastered 2024)       https://www.deezer.com/album/540949602
Sean Paul             - More Dancehall: The Flip Riddim                                  https://www.deezer.com/album/788526291
Sean Paul             - More Dancehall: Headache Riddim                                  https://www.deezer.com/album/795248881
Shabba Ranks          - Golden Touch (2025 Remastered)                                   https://www.deezer.com/album/700406851
Shabba Ranks          - Mikey Bennett's: Golden Touch Riddim                             https://www.deezer.com/album/700706851
Shabba Ranks          - Mr. Maximum (The Remixes)                                        https://www.deezer.com/album/722562991
Shabba Ranks          - Twin Spin                                                        https://www.deezer.com/album/774551441
Shabba Ranks          - Lively Up Yourself                                               https://www.deezer.com/album/834296392
Shabba Ranks          - Every Time You Go Away Riddim                                    https://www.deezer.com/album/836066972
Shabba Ranks          - Pirates Anthem (Long Stream 2025 Remaster)                       https://www.deezer.com/album/922687441
Shabba Ranks          - Twice My Age Riddim                                              https://www.deezer.com/album/923464001
Shabba Ranks          - Turn It Down (2025 Remaster)                                     https://www.deezer.com/album/936696831
Shabba Ranks          - Don't Test Me                                                    https://www.deezer.com/album/939732341
Shabba Ranks          - Show Me What You Got (Platinum Riddim)                           https://www.deezer.com/album/992630721
Shelly Thunder        - Small Horsewoman                                                 https://www.deezer.com/album/406079377
Shelly Thunder        - Reggae Dancehall Riddim: The Exit                                https://www.deezer.com/album/433860837
Shelly Thunder        - Reggae Dancehall Riddim: Kuff                                    https://www.deezer.com/album/434472657
Shinehead             - Rough & Rugged                                                   https://www.deezer.com/album/362325267
Singing Melody        - Original                                                         https://www.deezer.com/album/794120241
Sizzla                - Reggae Generals:                                                 https://www.deezer.com/album/413886657
Sizzla                - Reggae Dancehall Riddim: Signs                                   https://www.deezer.com/album/545404262
Sizzla                - Conscious Reggae                                                 https://www.deezer.com/album/559704782
Sizzla                - Say You Love Me - X5 Riddim (2026 Remaster)                      https://www.deezer.com/album/1035496422
Sly & Robbie          - Dub Masters                                                      https://www.deezer.com/album/448145895
Soljie                - Rebel Soldier                                                    https://www.deezer.com/album/362308317
Sonia Ferguson        - Lovers Rock Gold                                                 https://www.deezer.com/album/353237977
Sonia Ferguson        - Magic Lady                                                       https://www.deezer.com/album/851730752
Spice                 - John John Dancehall Riddims: The Mix                             https://www.deezer.com/album/607852932
Spice                 - Mi Nuh Like Dat                                                  https://www.deezer.com/album/938915181
Spragga Benz          - Anything For You Riddim                                          https://www.deezer.com/album/1046752002
Sugar Belly           - The Return of the Sugar Belly                                    https://www.deezer.com/album/353417227
Sugar Minott          - Kings of Lovers Rock                                             https://www.deezer.com/album/353217917
Sugar Minott          - Inna Reggae Dance Hall                                           https://www.deezer.com/album/355192837
Sugar Minott          - Sufferer's Choice                                                https://www.deezer.com/album/360168587
Sugar Minott          - Witty Hifi                                                       https://www.deezer.com/album/544700382
Sugar Minott          - Reggae Generals: Sugar Minott                                    https://www.deezer.com/album/635586441
Tanto Metro & Devonte - Tony "CD" Kelly Presents: Dancehall Vibes                        https://www.deezer.com/album/551872342
Tanya Stephens        - A We A Spend (Scream Riddim)                                     https://www.deezer.com/album/959348781
Tappa Zukie           - Man Ah Warrior                                                   https://www.deezer.com/album/348411457
Tappa Zukie           - Reggae Stream                                                    https://www.deezer.com/album/353429697
Tappa Zukie           - Reggae Trio                                                      https://www.deezer.com/album/353717877
Tarrus Riley          - John John Reggae Riddims: Fuss & Fight                           https://www.deezer.com/album/635493821
Tarrus Riley          - John John Reggae Riddims: Inna Rub A Dub Style                   https://www.deezer.com/album/774551651
Tarrus Riley          - John John Reggae Riddims: Zion Gate                              https://www.deezer.com/album/800272911
Tarrus Riley          - Whispers (Shine Riddim)                                          https://www.deezer.com/album/996417461
Tenor Saw             - Fever                                                            https://www.deezer.com/album/348962847
Tenor Saw             - Reggae Trio                                                      https://www.deezer.com/album/353223667
Tenor Saw             - Dub Fever                                                        https://www.deezer.com/album/353316877
Tenor Saw             - Clash                                                            https://www.deezer.com/album/406854127
Tenor Saw             - Super Clash                                                      https://www.deezer.com/album/425975587
Tenor Saw             - Now This Is An Anthem, Vol. 2                                    https://www.deezer.com/album/1039669722
Terror Fabulous       - Dancehall Generals:                                              https://www.deezer.com/album/418084227
Terror Fabulous       - John John Dancehall Riddims: Peanie Peanie                       https://www.deezer.com/album/603527512
Terror Fabulous       - Dancehall Dons                                                   https://www.deezer.com/album/1033938002
Tetrack               - Reggae Groups: Tetrack                                           https://www.deezer.com/album/701843001
Tony Tuff             - Tuff Selection                                                   https://www.deezer.com/album/65801932
Tony Tuff             - Ketch A Fire                                                     https://www.deezer.com/album/702727081
Tony Tuff             - Girl I've Got To Get You (2026 Remaster)                         https://www.deezer.com/album/996535681
Tony Tuff             - A Love I Can Feel                                                https://www.deezer.com/album/1002785771
Trevor Walters        - Lovers Rock Gold: Trevor Walters                                 https://www.deezer.com/album/348410027
Various Artists       - The Best Lovers Rock Songs                                       https://www.deezer.com/album/353285707
Various Artists       - Gussie Clarke's Reggae Dancehall Collaborations                  https://www.deezer.com/album/910931741
Various Artists       - Gussie Clarke's Reggae Dancehall Collaborations, Vol. 2          https://www.deezer.com/album/1033490612
Various Artists       - Roots & Culture                                                  https://www.deezer.com/album/1046127072
Vybz Kartel           - Dancehall Riddim: G String                                       https://www.deezer.com/album/520995612
Vybz Kartel           - John John Dancehall Riddims: Target                              https://www.deezer.com/album/607850652
Vybz Kartel           - John John Dancehall Riddims: Cash Register                       https://www.deezer.com/album/639725401
Vybz Kartel           - Dancehall Riddim: Assault Rifle                                  https://www.deezer.com/album/695469841
Vybz Kartel           - Furnace Riddim                                                   https://www.deezer.com/album/781691381
Vybz Kartel           - More Dancehall: Scream Riddim                                    https://www.deezer.com/album/784649391
Vybz Kartel           - A John John Masterpiece                                          https://www.deezer.com/album/794238901
Vybz Kartel           - Puff It (Step Father Riddim)                                     https://www.deezer.com/album/911665391
Vybz Kartel           - Good Like Gold (Step Father Riddim)                              https://www.deezer.com/album/911666101
Vybz Kartel           - Baby Father (Uptown Riddim)                                      https://www.deezer.com/album/911666171
Vybz Kartel           - Y2K Dancehall Gold (Step Father Riddim)                          https://www.deezer.com/album/923979541
Vybz Kartel           - Y2K Dancehall Gold (Uptown Riddim)                               https://www.deezer.com/album/923981441
Vybz Kartel           - War Start                                                        https://www.deezer.com/album/939080001
Vybz Kartel           - Y2K Dancehall Gold: Belview Riddim                               https://www.deezer.com/album/945457701
Vybz Kartel           - Friend Of Mine (Scream Riddim)                                   https://www.deezer.com/album/960350611
Vybz Kartel           - Cruising (Ruckus Riddim)                                         https://www.deezer.com/album/961281941
Vybz Kartel           - Badda Dan Dem                                                    https://www.deezer.com/album/962884901
Vybz Kartel           - Y2K Dancehall Gold: Kasablanca Riddim                            https://www.deezer.com/album/983049891
Vybz Kartel           - More Dancehall: Ruckus Riddim - The Sequel                       https://www.deezer.com/album/998275501
Wayne Wade            - Willie Lindo Presents: Love Bump Riddim (2025 Remaster)          https://www.deezer.com/album/674221891
Wayne Wade            - I Love You Too Much                                              https://www.deezer.com/album/690917991
Wayne Wonder          - Anything Goes (Remastered 2024)                                  https://www.deezer.com/album/555780222
Webby Jay             - Reggae Stream                                                    https://www.deezer.com/album/353404127
Willie Lindo          - Reggae Machine                                                   https://www.deezer.com/album/693361631
Yami Bolo             - Reggae Trio                                                      https://www.deezer.com/album/416282167
```
