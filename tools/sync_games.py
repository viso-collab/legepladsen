#!/usr/bin/env python3
"""Henter de nyeste versioner af spillene fra deres egne repos ind i games/.

Musefelt har ikke sit eget repo og ligger kun her. Regnekanonen ligger i
gangetabel-kanonen. Piggy Smash hedder
Splinter Gulch i sit eget repo og omdøbes, når den kopieres hertil.

Brug:  python3 tools/sync_games.py            (repo-versionen, med online og leaderboard)
       python3 tools/sync_games.py --artifact DIR
       (laver også en udgave af Kart Kaos til claude.ai-artefakten, hvor
        Supabase og PeerJS er slået fra, fordi artefakter blokerer dem)
"""
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/viso-collab/{repo}/main/index.html"


def fetch(repo):
    with urllib.request.urlopen(RAW.format(repo=repo), timeout=30) as r:
        return r.read().decode("utf-8")


def swap(text, old, new, count=1):
    n = text.count(old)
    if n != count:
        sys.exit(f"Forventede {count} forekomst(er) af {old[:60]!r}, fandt {n}. Er spillet ændret?")
    return text.replace(old, new)


def piggy_smash(src):
    src = swap(src, "<title>Splinter Gulch</title>", "<title>Piggy Smash</title>")
    src = swap(src, '<div class="brand">Splinter Gulch<small>', '<div class="brand">Piggy Smash<small>')
    return src


def kart_kaos_for_artifact(src):
    """claude.ai-artefakter blokerer fetch til andre domæner og WebRTC, så
    leaderboard og online slås fra, og navnet gemmes kun lokalt."""
    src = swap(src, '<script src="https://unpkg.com/peerjs@1.5.4/dist/peerjs.min.js"></script>\n', "")
    src = swap(src, "const SUPABASE_URL = 'https://cfruuywuhybbivijpudb.supabase.co';", "const SUPABASE_URL = '';")
    src = swap(src, "if (!lbOn()) $('lbNote').textContent = 'Leaderboardet er ikke sat op endnu.';",
               "if (!lbOn()) $('lbNote').textContent = 'Leaderboardet findes kun i GitHub-versionen: viso-collab.github.io/kaos-karts';")
    src = swap(src, "if (!roomApi) { $('onlineCount').textContent = 'Online kunne ikke indlæses. Tjek internetforbindelsen og genindlæs siden.'; return; }",
               "if (!roomApi) { $('onlineCount').textContent = 'Online virker kun i GitHub-versionen: viso-collab.github.io/kaos-karts'; return; }")
    src = swap(src, "note.textContent = 'Online virker kun, når du er logget ind på claude.ai og har adgang til spillet.'",
               "note.textContent = 'Online virker kun i GitHub-versionen: viso-collab.github.io/kaos-karts'")
    src = swap(src, "<p class=\"hint2\">Alle med linket kan spille online. Online er kun rigtige mennesker, ingen bots.</p>",
               "<p class=\"hint2\">Spil online på viso-collab.github.io/kaos-karts.</p>")
    return src


def main():
    games = ROOT / "games"
    pig = piggy_smash(fetch("splinter-gulch"))
    kart = fetch("kaos-karts")
    regne = fetch("gangetabel-kanonen")
    (games / "piggy-smash.html").write_text(pig, encoding="utf-8")
    (games / "kart-kaos.html").write_text(kart, encoding="utf-8")
    (games / "regnekanonen.html").write_text(regne, encoding="utf-8")
    print("Opdaterede games/piggy-smash.html, games/kart-kaos.html og games/regnekanonen.html")
    if "--artifact" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--artifact") + 1])
        (out / "games").mkdir(parents=True, exist_ok=True)
        (out / "games" / "piggy-smash.html").write_text(pig, encoding="utf-8")
        (out / "games" / "kart-kaos.html").write_text(kart_kaos_for_artifact(kart), encoding="utf-8")
        (out / "games" / "regnekanonen.html").write_text(regne, encoding="utf-8")
        print(f"Artefakt-udgaver skrevet til {out}/games")


if __name__ == "__main__":
    main()
