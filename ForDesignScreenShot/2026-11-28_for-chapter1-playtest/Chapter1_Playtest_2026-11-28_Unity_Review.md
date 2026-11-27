# Chapter I playtest fixes

November 28, 2026 · The Fairy Hills · Windows Editor, Unity 6000.3.24f1

Implemented the three items in the November 28 playtest brief. The actual Editor played the mouse and keyboard routes. The linked recordings include game audio and continue at least 11 seconds after Village control returns.

## 1. MainMenu to prologue

Start fades the complete menu and its looping music over 0.5 seconds. A full-screen black overlay covers the asynchronous load. Once the prologue starts its scheduled score, BG01, its text and the right-hand hint fade in together over 1.0 second. The existing 1.5-second gain ramp, 0.85 music gain and 30.6-second score timeline carry through. BG01 receives about 3.6 seconds at full brightness before its natural page dissolve begins.

| Run | Start | Opaque black in the recording | BG01 fully visible | Result |
| --- | ---: | --- | ---: | --- |
| 1280 × 720, mouse | 2.000 s | 2.667–2.875 s | 3.917 s | Five natural pages, Chapter I cover and one Village load |
| 1920 × 1080, keyboard | 2.000 s | 2.458–2.708 s | 3.708 s | Held Enter and early Esc were consumed. A fresh B advanced BG01. Esc from OP03 reached the cover and one Village load. |

Times are from the 24 fps recordings. The frame check found consecutive fully black frames covering the scene swap at both sizes, followed by a gradual rise into BG01. There was no flash or intermediate scene frame in the recorded transitions. Across both full routes the monitor found a render camera and one active listener on every sampled handoff frame. A repeat Start pointer attempt hit the black overlay. After Enter was released, B performed the first ordinary page advance. The 720p mouse run continued without turning a page manually, to verify the uninterrupted v9 timeline and cover-to-Village handoff. [720p mouse and natural playback](References/Chapter1_Playtest_2026-11-28/Mouse_start_1280.mp4) · [1080p keyboard and Esc](References/Chapter1_Playtest_2026-11-28/Keyboard_start_1920.mp4)

A separate runtime check stood in for a missing prologue route by changing the Start target temporarily in memory. Start took the existing Village fallback. Holding D through the fade left Niamh at x = 3.500. Releasing it cleared the input gate, and another D moved her. The black camera covered the load while Core created the real camera and listener. Three sampled fallback frames had no active listener under black, before Village playback started.

## 2. Four caption adjustments

The red marks were aligned to the Game View artwork. BG01 moved vertically only. All four captions retain their previous left alignment, copy, manual line breaks and type sizes. OP01 and parts of OP02 extend to the right of their hand-drawn placement guides to retain the original word lengths. The caption areas and the hint remained distinct. TMP reported no overflow at either resolution.

| Page | Anchor min (x, y) | Anchor max (x, y) | Size and lines | 1280 × 720 | 1920 × 1080 |
| --- | --- | --- | --- | --- | --- |
| BG01 | (0.713, 0.320) | (0.942, 0.466) | 33.8, 3 lines | [BG01](References/Chapter1_Playtest_2026-11-28/BG01_1280.png) | [BG01](References/Chapter1_Playtest_2026-11-28/BG01_1920.png) |
| OP01 | (0.655, 0.063) | (0.965, 0.188) | 36 rendered, 2 lines | [OP01](References/Chapter1_Playtest_2026-11-28/OP01_1280.png) | [OP01](References/Chapter1_Playtest_2026-11-28/OP01_1920.png) |
| OP02 | (0.665, 0.310) | (0.931, 0.459) | 36, 3 lines | [OP02](References/Chapter1_Playtest_2026-11-28/OP02_1280.png) | [OP02](References/Chapter1_Playtest_2026-11-28/OP02_1920.png) |
| OP03 | (0.697, 0.301) | (0.941, 0.450) | 36, 3 lines | [OP03](References/Chapter1_Playtest_2026-11-28/OP03_1280.png) | [OP03](References/Chapter1_Playtest_2026-11-28/OP03_1920.png) |

BG02 is included for comparison. [BG02 at 720p](References/Chapter1_Playtest_2026-11-28/BG02_1280.png) · [BG02 at 1080p](References/Chapter1_Playtest_2026-11-28/BG02_1920.png)

## 3. Village music

The untouched Village scene had Play On Awake enabled at 0.50, although the Chapter I builder already authored it off. The before run reproduced the reported dip. The source was already playing at 0.50 with the prologue listener active. The listener passed to Core and the prologue then set the same playing source to 0.00. In the recorded Unity mix, successive 50 ms windows went from about −19 to −49 dBFS across the drop.

The Village scene now matches the builder's Play On Awake setting. LevelBootstrap owns the start and fade. For a covered entry it waits for the reveal to request playback. It sets the volume to zero before starting the clip, then fades over the same interval as the picture. Standalone Village and additive level entry use the same one-second fade. The existing track and target of 0.50 carry through. The normal and Esc routes both showed a single source start, no volume reset after the start, and steady target gain after the fade.

| Event | Before clip | After clip |
| --- | ---: | ---: |
| Village first sampled | 5.292 s, playing at 0.50 | 5.208 s, stopped at 0.50 |
| First Village signal in the captured mix | Approx. 5.24 s | Approx. 5.46 s |
| Start of the volume dip or fade | 5.542 s, snaps to 0.00 during playback | 5.417 s, playback starts at 0.00 |
| Reaches 0.50 after fade | 6.958 s | 7.000 s |
| Controls restored | 7.000 s | 7.083 s |

Values are relative to each comparison clip, which starts as the cover appears. The first-signal figures are approximate 50 ms windows in the digital mix. They indicate the earliest easily measurable Village signal, which can precede the sampled frame that logged it. Both recordings used the same running Unity Editor, stereo 48 kHz mix, listener master 1.00 and capture settings. The fixed clip shows over 11 seconds at stable target gain after control returns. In-room speaker preference remains for the owner. [Before, with the dip](References/Chapter1_Playtest_2026-11-28/Village_before.mp4) · [After, with the fade](References/Chapter1_Playtest_2026-11-28/Village_after.mp4) · [Village spawn at 720p](References/Chapter1_Playtest_2026-11-28/Village_1280.png) · [Village spawn at 1080p](References/Chapter1_Playtest_2026-11-28/Village_1920.png)

| Other entry | Observed result |
| --- | --- |
| Direct load of Village | Core bootstrapped. Music started once at zero and reached 0.50 after 1.00 s. |
| Esc from prologue | The cover played. Music started once at zero and held 0.50. Niamh moved after the reveal. |
| Forest → Village | Invoked through the existing additive ChapterSceneLoader API. Music started once at zero and reached 0.50 after 1.00 s. The authored Forest exit returns to MainMenu. |
| MainMenu fallback with prologue unavailable | The Village took over after the covered load. Music started once at zero, reached 0.50 and held while input unlocked on release. |

## Files and verification

- `MainMenuController.cs` starts the new `MenuEntryFade.cs` overlay and gates repeat input. The overlay covers the existing fallback path.
- `OpeningSequencePlayer.cs` drives the BG01 reveal from the score clock and coordinates the covered Village reveal.
- `LevelBootstrap.cs` owns level music playback and the fade. `Ch1_S1_Village.unity` matches the builder through its serialized Play On Awake flag. The builder already writes false and required no edit.
- `Opening_Chapter1.asset` contains the four anchor changes. The local tracked-workspace checkpoint before edits is `235ec6a`.
- The project compiled successfully. These were scoped Play Mode checks in the actual Editor using the EventSystem Start button and injected Unity Input System keys. The Console included no-listener informational messages while a directly loaded level or the forced fallback waited for Core. The Editor also reported an account API timeout. The gameplay runs added no errors. Physical input, production builds and owner visual and speaker approval remain unverified. [Play Mode timing and audio observations](References/Chapter1_Playtest_2026-11-28/play_mode_observations.txt)
