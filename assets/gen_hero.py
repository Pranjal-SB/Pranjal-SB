#!/usr/bin/env python3
"""Generate self-hosted SVGs for the profile README — dot-matrix system.
No remote deps, no animation (GitHub strips it), system fonts only.
Writes: hero.svg, examdb.svg, h_*.svg (headings), btn_*.svg (link pills).
Run: python assets/gen_hero.py
"""
from pathlib import Path

# --- palette ---
BG    = "#1c1917"
PANEL = "#211e1c"
CYAN  = "#0891b2"
TEXT  = "#c7d5d5"
MUTED = "#8b8b8b"
WHITE = "#ffffff"
DIM   = "#2a2725"
AMBER = "#f59e0b"
EMERALD = "#34d399"
VIOLET = "#a78bfa"
MONO  = "'JetBrains Mono','Courier New',monospace"

# --- 5x7 dot-matrix font, full uppercase ---
FONT = {
    "A": ["01110","10001","10001","11111","10001","10001","10001"],
    "B": ["11110","10001","10001","11110","10001","10001","11110"],
    "C": ["01110","10001","10000","10000","10000","10001","01110"],
    "D": ["11100","10010","10001","10001","10001","10010","11100"],
    "E": ["11111","10000","10000","11110","10000","10000","11111"],
    "F": ["11111","10000","10000","11110","10000","10000","10000"],
    "G": ["01110","10001","10000","10111","10001","10001","01111"],
    "H": ["10001","10001","10001","11111","10001","10001","10001"],
    "I": ["11111","00100","00100","00100","00100","00100","11111"],
    "J": ["00111","00010","00010","00010","00010","10010","01100"],
    "K": ["10001","10010","10100","11000","10100","10010","10001"],
    "L": ["10000","10000","10000","10000","10000","10000","11111"],
    "M": ["10001","11011","10101","10101","10001","10001","10001"],
    "N": ["10001","11001","10101","10011","10001","10001","10001"],
    "O": ["01110","10001","10001","10001","10001","10001","01110"],
    "P": ["11110","10001","10001","11110","10000","10000","10000"],
    "Q": ["01110","10001","10001","10001","10101","10010","01101"],
    "R": ["11110","10001","10001","11110","10100","10010","10001"],
    "S": ["01111","10000","10000","01110","00001","00001","11110"],
    "T": ["11111","00100","00100","00100","00100","00100","00100"],
    "U": ["10001","10001","10001","10001","10001","10001","01110"],
    "V": ["10001","10001","10001","10001","10001","01010","00100"],
    "W": ["10001","10001","10001","10101","10101","11011","10001"],
    "X": ["10001","10001","01010","00100","01010","10001","10001"],
    "Y": ["10001","10001","01010","00100","00100","00100","00100"],
    "Z": ["11111","00001","00010","00100","01000","10000","11111"],
    " ": ["00000","00000","00000","00000","00000","00000","00000"],
}


def dot_word(word, x0, y0, gap, r, on=CYAN, off=None):
    """Render WORD as dot-matrix circles. off=None hides empty dots."""
    out, pitch = [], 6 * gap  # 5 cols + 1 blank between letters
    for li, ch in enumerate(word):
        rows = FONT[ch]
        lx = x0 + li * pitch
        for ry, row in enumerate(rows):
            for cx, bit in enumerate(row):
                cxp, cyp = lx + cx * gap, y0 + ry * gap
                if bit == "1":
                    out.append(f'<circle cx="{cxp}" cy="{cyp}" r="{r}" fill="{on}"/>')
                elif off:
                    out.append(f'<circle cx="{cxp}" cy="{cyp}" r="2" fill="{off}"/>')
    width = len(word) * pitch - gap
    return "\n".join(out), width


def hero():
    W, H = 1200, 420
    body, ww = dot_word("PRANJAL", 0, 0, gap=20, r=7, off=DIM)
    ox, oy = (W - ww) / 2, 120
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Pranjal - backend-leaning full-stack builder">
<title>Pranjal - backend-leaning full-stack builder</title>
<rect width="{W}" height="{H}" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="15" fill="none" stroke="{DIM}" stroke-width="2"/>
<circle cx="48" cy="48" r="6" fill="{DIM}"/>
<circle cx="72" cy="48" r="6" fill="{DIM}"/>
<circle cx="96" cy="48" r="6" fill="{CYAN}"/>
<g transform="translate({ox},{oy})">
{body}
</g>
<text x="50%" y="330" text-anchor="middle" font-family="{MONO}" font-weight="700" font-size="26" fill="{TEXT}" letter-spacing="2">BACKEND-LEANING FULL-STACK BUILDER</text>
<text x="50%" y="370" text-anchor="middle" font-family="{MONO}" font-size="21" fill="{MUTED}" letter-spacing="1">APIS &#183; SCRAPERS &#183; WEB APPS &#8212; TypeScript &#183; Python &#183; learning Java</text>
</svg>'''


def examdb():
    W, H = 1200, 240
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="examdb.org - Indian entrance-exam dates, scraped and confidence-scored for freshness">
<title>examdb.org - Indian entrance-exam dates, scraped and confidence-scored</title>
<rect width="{W}" height="{H}" rx="16" fill="{PANEL}"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="15" fill="none" stroke="{DIM}" stroke-width="2"/>
<rect x="0" y="0" width="6" height="{H}" rx="3" fill="{CYAN}"/>
<text x="52" y="70" font-family="{MONO}" font-size="18" fill="{MUTED}" letter-spacing="4">CURRENTLY BUILDING</text>
<text x="50" y="128" font-family="{MONO}" font-weight="700" font-size="52" fill="{WHITE}">examdb<tspan fill="{CYAN}">.org</tspan></text>
<text x="52" y="172" font-family="{MONO}" font-size="22" fill="{TEXT}">Indian entrance-exam dates &#8212; scraped, then confidence-scored for freshness.</text>
<text x="52" y="208" font-family="{MONO}" font-size="17" fill="{MUTED}" letter-spacing="1">FastAPI &#183; Postgres &#183; Redis &#183; Docker</text>
<text x="{W-52}" y="128" text-anchor="end" font-family="{MONO}" font-size="20" fill="{CYAN}">visit &#8594;</text>
</svg>'''


def heading(word, accent=CYAN):
    """Left-aligned dot-matrix heading with a full-width baseline rule."""
    W, gap, r, pad = 1200, 11, 3.6, 4
    body, ww = dot_word(word, pad, 6, gap=gap, r=r, on=accent, off=None)
    H = 108
    ruleY = 90
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{word}">
<title>{word}</title>
<g>
{body}
</g>
<line x1="{pad}" y1="{ruleY}" x2="{ww+pad}" y2="{ruleY}" stroke="{accent}" stroke-width="2"/>
<line x1="{ww+pad+16}" y1="{ruleY}" x2="{W-pad}" y2="{ruleY}" stroke="{DIM}" stroke-width="2"/>
</svg>'''


def button(label, primary=True):
    """Rounded pill link button, self-hosted, no external logo."""
    fs = 26 if primary else 22
    H = 76 if primary else 60
    ch_w = fs * 0.62
    tw = len(label) * ch_w
    dot_x = 34 if primary else 28
    text_x = dot_x + (26 if primary else 20)
    W = int(text_x + tw + (34 if primary else 26))
    r = H / 2
    dotr = 7 if primary else 5
    txt_fill = TEXT if primary else MUTED
    dot_fill = CYAN if primary else MUTED
    stroke = CYAN if primary else DIM
    fill = PANEL if primary else BG
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">
<title>{label}</title>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
<circle cx="{dot_x}" cy="{H/2}" r="{dotr}" fill="{dot_fill}"/>
<text x="{text_x}" y="{H/2}" dominant-baseline="central" font-family="{MONO}" font-weight="600" font-size="{fs}" fill="{txt_fill}">{label}</text>
</svg>'''


# fn -> (word, accent) — color-coded section system
HEADINGS = {"h_whoami":   ("WHOAMI",   CYAN),
            "h_stack":    ("STACK",    AMBER),
            "h_activity": ("ACTIVITY", EMERALD),
            "h_connect":  ("CONNECT",  VIOLET)}
PRIMARY = ["Portfolio", "Blog", "examdb.org", "LinkedIn", "GitHub", "Mail"]
SECONDARY = ["Instagram", "Chess.com", "Spotify"]


def slug(s):
    return s.lower().replace(".", "").replace(" ", "")


if __name__ == "__main__":
    d = Path(__file__).parent
    (d / "hero.svg").write_text(hero(), encoding="utf-8")
    (d / "examdb.svg").write_text(examdb(), encoding="utf-8")
    for fn, (word, accent) in HEADINGS.items():
        (d / f"{fn}.svg").write_text(heading(word, accent), encoding="utf-8")
    for lbl in PRIMARY:
        (d / f"btn_{slug(lbl)}.svg").write_text(button(lbl, True), encoding="utf-8")
    for lbl in SECONDARY:
        (d / f"btn_{slug(lbl)}.svg").write_text(button(lbl, False), encoding="utf-8")
    print("wrote hero, examdb, headings, buttons")
