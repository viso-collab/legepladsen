# Legepladsen

Tre små browserspil samlet på én side.

| Spil | Fil | Styring |
|---|---|---|
| **Musefelt**: seks interaktive lærreder (ildfluer, fisk, kometer, bobleplast …) | `games/musefelt.html` | Mus eller touch |
| **Piggy Smash**: smash sparegrise, find våben i kister og byg et skill tree (på engelsk) | `games/piggy-smash.html` | Mus eller touch |
| **Kart Kaos**: arenakamp i 3D-karts mod bots eller online, med leaderboard | `games/kart-kaos.html` | Tastatur |

## Kør lokalt

Der er ingen build. Start en statisk server i mappen:

```sh
python3 -m http.server 8000
```

Åbn derefter http://localhost:8000. Hvert spil kan også åbnes direkte via sin egen HTML-fil.

## Opdatér spillene

Piggy Smash og Kart Kaos udvikles i deres egne repos ([splinter-gulch](https://github.com/viso-collab/splinter-gulch) og [kaos-karts](https://github.com/viso-collab/kaos-karts)). Hent de nyeste versioner hertil med:

```sh
python3 tools/sync_games.py
```

Scriptet omdøber Splinter Gulch til Piggy Smash. Med `--artifact DIR` laver det også den udgave af Kart Kaos, der bruges i claude.ai-artefakten, hvor online og leaderboard er slået fra.

## Noter

- Fremskridt og rekorder gemmes i browserens `localStorage`.
- Kart Kaos bruger PeerJS til online-lobbyer og Supabase til navne og leaderboard. Begge dele virker, når siden ligger på en almindelig webadresse (fx GitHub Pages), men ikke inde i en claude.ai-artefakt.
- Kart Kaos henter three.js r128 fra cdnjs.
