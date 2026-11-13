# Legepladsen

Fem små browserspil samlet på én side.

| Spil | Fil | Styring |
|---|---|---|
| **Musefelt**: seks interaktive lærreder (ildfluer, fisk, kometer, bobleplast …) | `games/musefelt.html` | Mus eller touch |
| **Piggy Smash**: smash sparegrise, find våben i kister og byg et skill tree (på engelsk) | `games/piggy-smash.html` | Mus eller touch |
| **Kart Kaos**: arenakamp i 3D-karts mod bots eller online, med leaderboard | `games/kart-kaos.html` | Tastatur |
| **Regnekanonen**: skyd kuglen med det rigtige svar i 20 levels plus, minus og lidt gange, med uglen Professor Hu (7–8 år) | `games/regnekanonen.html` | Mus eller touch |
| **Tumult**: platform-kampspil med 8 figurer, 1v1 og 2v2, mod CPU eller online (på engelsk) | [viso-collab.github.io/tumult](https://viso-collab.github.io/tumult/) | Tastatur eller controller |

## Kør lokalt

Der er ingen build. Start en statisk server i mappen:

```sh
python3 -m http.server 8000
```

Åbn derefter http://localhost:8000. Hvert spil kan også åbnes direkte via sin egen HTML-fil.

## Opdatér spillene

Piggy Smash, Kart Kaos og Regnekanonen udvikles i deres egne repos ([splinter-gulch](https://github.com/viso-collab/splinter-gulch), [kaos-karts](https://github.com/viso-collab/kaos-karts) og [gangetabel-kanonen](https://github.com/viso-collab/gangetabel-kanonen)). Hent de nyeste versioner hertil med:

```sh
python3 tools/sync_games.py
```

Scriptet omdøber Splinter Gulch til Piggy Smash. Med `--artifact DIR` laver det også den udgave af Kart Kaos, der bruges i claude.ai-artefakten, hvor online og leaderboard er slået fra.

## Noter

- Fremskridt og rekorder gemmes i browserens `localStorage`.
- Kart Kaos bruger PeerJS til online-lobbyer og Supabase til navne og leaderboard. Begge dele virker, når siden ligger på en almindelig webadresse (fx GitHub Pages), men ikke inde i en claude.ai-artefakt.
- Kart Kaos henter three.js r128 fra cdnjs.
- Tumult ligger ikke i `games/`. Kortet åbner [viso-collab.github.io/tumult](https://viso-collab.github.io/tumult/) direkte, så Legepladsen altid viser den nyeste version, og online virker. Det kræver internet, også når siden køres lokalt.
