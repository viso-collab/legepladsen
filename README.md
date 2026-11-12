# Legepladsen

Tre små browserspil samlet på én side.

| Spil | Fil | Styring |
|---|---|---|
| **Musefelt**: seks interaktive lærreder (ildfluer, fisk, kometer, bobleplast …) | `games/musefelt.html` | Mus eller touch |
| **Piggy Smash**: smash sparegrise, find kister og lås evner op (på engelsk) | `games/piggy-smash.html` | Mus eller touch |
| **Kart Kaos**: arenakamp i 3D-karts mod bots | `games/kart-kaos.html` | Tastatur |

## Kør lokalt

Der er ingen build. Start en statisk server i mappen:

```sh
python3 -m http.server 8000
```

Åbn derefter http://localhost:8000. Hvert spil kan også åbnes direkte via sin egen HTML-fil.

## Noter

- Fremskridt og rekorder gemmes i browserens `localStorage`.
- Kart Kaos' online-lobby bruger claude.ai's artifact-runtime (`window.claude.use('room')`). Udenfor claude.ai viser menuen "Online er ikke tilgængeligt her", og man spiller mod bots.
- Kart Kaos henter three.js r128 fra cdnjs.
