"""Generate the profile README's SVG graphics (dark and light variants).

Run from the repository root:  python scripts/build_assets.py
Edit the data below (PROJECTS, ROLES, HIGHLIGHTS, PHRASES) and re-run; never edit the SVGs by hand.
"""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"

THEMES = {
    "dark": {
        "bg": "#0B111A", "panel": "#111A27", "border": "#223043", "text": "#E5EBF2",
        "muted": "#9BAABA", "accent": "#85A6FF", "accent_soft": "#1E2B44",
        "live": "#5EEAD4", "live_soft": "#0F2F2C", "chip": "#18243A",
    },
    "light": {
        "bg": "#FFFFFF", "panel": "#F6F8FB", "border": "#C8D2DA", "text": "#0F1A2A",
        "muted": "#4A596A", "accent": "#1D4ED8", "accent_soft": "#E3EAFD",
        "live": "#0F766E", "live_soft": "#DDF4F1", "chip": "#EDF1F4",
    },
}

PHRASES = [
    "Agentic AI with a human in the loop",
    "Retrieval systems that cite their sources",
    "Computer vision, from model to API",
    "Production ML that ships and stays up",
]

HIGHLIGHTS = [
    ("Live", "ChandleryOS in production", True),
    ("SIH 2024", "Smart India Hackathon finalist", False),
    ("<1%", "calibration error at TIFR", False),
    ("8.43", "CGPA, B.Tech ECE, KJSCE", False),
]

FEATURED = {
    "slug": "chandleryos",
    "tag": "LIVE IN PRODUCTION · CLIENT WORK",
    "title": "ChandleryOS · Tech Shipping",
    "desc": (
        "The operations system a Mumbai ship chandler now runs on. WhatsApp and email supply lists "
        "are read by AI into draft lines, priced with landed cost, margin and GST, then carried "
        "through quotation, purchase order, delivery and invoice, with a person approving every step."
    ),
    "flow": ["Inquiry", "AI reading", "Quotation", "Purchase", "Delivery", "Invoice"],
    "stack": ["Django", "HTMX", "PostgreSQL", "Claude API", "Django-Q2", "Render"],
    "result": "845 tests · 22-case AI eval suite · money maths never touched by AI",
}

PROJECTS = [
    {
        "slug": "medical-imaging", "tag": "AGENTIC AI · RAG",
        "title": "Multi-Agent Medical Imaging",
        "desc": "Agents that read chest X-rays, assess sepsis risk and answer medical questions, "
                "with guardrails and review by a medical professional.",
        "stack": ["LangGraph", "Qdrant", "FastAPI", "Docker"],
        "result": "Confidence-based handoffs to a human",
    },
    {
        "slug": "trading-sentinel", "tag": "QUANT · FULL STACK",
        "title": "Trading Sentinel",
        "desc": "An algorithmic-trading system with risk gates, paper trading by default, Telegram "
                "alerts and a backtester that replays real candle history.",
        "stack": ["FastAPI", "Node.js", "React", "Fyers"],
        "result": "Paper trading by default, risk gates first",
    },
    {
        "slug": "vigilpay", "tag": "FINTECH · HACKATHON",
        "title": "VigilPay",
        "desc": "Fraud prevention for Indian payments, with risk scoring that adapts to regional "
                "merchant trust and festival periods.",
        "stack": ["Next.js", "MongoDB", "Tailwind"],
        "result": "Smart India Hackathon 2024 finalist",
    },
    {
        "slug": "edge-detection", "tag": "COMPUTER VISION",
        "title": "Context-Aware Edge Detection",
        "desc": "An edge detector that adds transformer refinement and attention gates to a "
                "ResNet50 backbone.",
        "stack": ["PyTorch", "ResNet50", "Transformers"],
        "result": "Attention gates on a ResNet50 backbone",
    },
    {
        "slug": "hvac-forecasting", "tag": "TIME SERIES",
        "title": "HVAC Load Forecasting",
        "desc": "Forecasts cooling load in kWh from 46 weather, occupancy and zone features over "
                "48 time steps.",
        "stack": ["PatchTST", "TSai", "PyTorch"],
        "result": "46 features · 48-step horizon",
    },
    {
        "slug": "tifr-calibration", "tag": "RESEARCH · TIFR",
        "title": "TIFR Magnet Calibration",
        "desc": "Calibration of DC beamline magnets from my research internship, evaluated with "
                "leave-one-out cross-validation.",
        "stack": ["Python", "Physics-based regression"],
        "result": "Sub-1% calibration error",
    },
]

ROLES = [
    ("Jun 2025 – present", "AI/ML Engineer", "Tech Shipping OPC",
     "Built ChandleryOS, the company's operations system; maritime AI copilot, RAG, predictive ML", True),
    ("Jan – May 2026", "Research Intern", "TIFR",
     "DC beamline magnet calibration, sub-1% error", False),
    ("Dec 2024 – Jan 2025", "ML Intern", "Unified Mentor",
     "Predictive models and dashboards", False),
    ("Jun – Aug 2024", "Research Intern", "Skylark Realty",
     "HVAC load forecasting with PatchTST", False),
]


def e(text):
    return escape(text, {'"': "&quot;"})


def wrap(text, size, width, factor=0.53):
    """Greedy word wrap using an average glyph width estimate."""
    max_chars = int(width / (size * factor))
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if len(candidate) <= max_chars:
            line = candidate
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def text_width(text, size, factor=0.53):
    return len(text) * size * factor


def svg(width, height, title, body, style=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-labelledby="t">\n'
        f'<title id="t">{e(title)}</title>\n'
        f'<style>{style}</style>\n{body}\n</svg>\n'
    )


def chips(items, x, y, c, size=13):
    out, cx = [], x
    for item in items:
        w = text_width(item, size, 0.6) + 22
        out.append(
            f'<rect x="{cx:.0f}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{c["chip"]}" '
            f'stroke="{c["border"]}"/>'
            f'<text x="{cx + w / 2:.0f}" y="{y + 17.5}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="{size}" fill="{c["muted"]}">{e(item)}</text>'
        )
        cx += w + 8
    return "".join(out)


# ---------------------------------------------------------------- hero banner

def hero(c):
    w, h = 1200, 320
    nodes = [(760, 90), (860, 60), (960, 110), (1080, 80), (820, 190), (930, 220), (1050, 190),
             (1130, 250), (720, 250)]
    edges = [(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (5, 6), (6, 3), (2, 5), (6, 7), (8, 4), (1, 4),
             (2, 6)]
    parts = [f'<rect width="{w}" height="{h}" fill="{c["bg"]}"/>']
    for gx in range(680, 1180, 40):
        parts.append(f'<line x1="{gx}" y1="30" x2="{gx}" y2="290" stroke="{c["border"]}" '
                     f'stroke-width="1" opacity="0.45"/>')
    for gy in range(30, 300, 52):
        parts.append(f'<line x1="680" y1="{gy}" x2="1160" y2="{gy}" stroke="{c["border"]}" '
                     f'stroke-width="1" opacity="0.45"/>')
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        parts.append(f'<path id="e{i}" d="M{x1},{y1} L{x2},{y2}" stroke="{c["accent"]}" '
                     f'stroke-width="1.5" opacity="0.35" fill="none"/>')
    for i in range(0, len(edges), 2):
        dur = 3 + (i % 5) * 0.6
        parts.append(
            f'<circle r="3.5" fill="{c["accent"]}"><animateMotion dur="{dur}s" '
            f'repeatCount="indefinite" begin="{i * 0.4}s"><mpath href="#e{i}"/></animateMotion></circle>'
        )
    for i, (x, y) in enumerate(nodes):
        big = i in (0, 3, 5)
        r = 9 if big else 6
        parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c["bg"]}" stroke="{c["accent"]}" '
                     f'stroke-width="2"/>')
        if big:
            parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c["accent"]}" '
                         f'class="ping" style="animation-delay:{i * 0.5}s"/>')
    # rising trend line with a dot travelling along it
    pts = "690,280 740,262 790,270 840,240 890,250 940,210 990,222 1040,180 1090,190 1150,150"
    parts.append(f'<polyline id="trend" points="{pts}" fill="none" stroke="{c["live"]}" '
                 f'stroke-width="3" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/>')
    parts.append(f'<circle r="5" fill="{c["live"]}"><animateMotion dur="4s" repeatCount="indefinite" '
                 f'path="M{pts.replace(" ", " L")}"/></circle>')
    # text block
    parts.append(f'<text x="64" y="92" font-family="{MONO}" font-size="16" letter-spacing="4" '
                 f'fill="{c["accent"]}" class="fade f1">AI/ML ENGINEER</text>')
    parts.append(f'<text x="60" y="164" font-family="{SANS}" font-size="70" font-weight="800" '
                 f'fill="{c["text"]}" class="fade f2">Smit Bangare</text>')
    parts.append(f'<text x="64" y="208" font-family="{SANS}" font-size="23" fill="{c["text"]}" '
                 f'class="fade f3">Agentic AI · RAG · Computer vision · Production ML</text>')
    parts.append(f'<circle cx="72" cy="251" r="6" fill="{c["live"]}" class="fade f4"/>'
                 f'<circle cx="72" cy="251" r="6" fill="none" stroke="{c["live"]}" class="ping"/>')
    parts.append(f'<text x="88" y="257" font-family="{MONO}" font-size="16" fill="{c["muted"]}" '
                 f'class="fade f4">Mumbai, India · open to AI/ML engineering roles</text>')
    style = (
        ".ping{transform-box:fill-box;transform-origin:center;animation:ping 2.4s ease-out infinite}"
        "@keyframes ping{0%{transform:scale(1);opacity:.8;stroke-width:2}"
        "100%{transform:scale(3);opacity:0;stroke-width:.5}}"
    )
    return svg(w, h, "Smit Bangare, AI/ML Engineer. Agentic AI, RAG, computer vision. Mumbai, India.",
               "\n".join(parts), style)


# ---------------------------------------------------------------- typing line

def typing(c):
    w, h, size = 1200, 56, 24
    char_w = size * 0.6
    step = 4.0
    parts = [f'<defs>']
    for i, phrase in enumerate(PHRASES):
        tw = len(phrase) * char_w
        x0 = (w - tw) / 2
        prev = f"p{len(PHRASES) - 1}.end" if i == 0 else f"p{i - 1}.end"
        begin = f"0s;{prev}" if i == 0 else prev
        parts.append(
            f'<clipPath id="c{i}"><rect x="{x0:.1f}" y="0" width="0" height="{h}">'
            f'<animate id="p{i}" attributeName="width" values="0;{tw + 4:.1f};{tw + 4:.1f};0" '
            f'keyTimes="0;0.4;0.85;1" dur="{step}s" begin="{begin}" fill="freeze"/></rect></clipPath>'
        )
    parts.append('</defs>')
    for i, phrase in enumerate(PHRASES):
        tw = len(phrase) * char_w
        x0 = (w - tw) / 2
        parts.append(
            f'<text x="{x0:.1f}" y="37" font-family="{MONO}" font-size="{size}" fill="{c["accent"]}" '
            f'clip-path="url(#c{i})">{e(phrase)}</text>'
        )
        begin = f"0s;p{len(PHRASES) - 1}.end" if i == 0 else f"p{i - 1}.end"
        parts.append(
            f'<rect x="{x0:.1f}" y="14" width="3" height="30" fill="{c["accent"]}" opacity="0">'
            f'<animate attributeName="x" values="{x0:.1f};{x0 + tw + 4:.1f};{x0 + tw + 4:.1f};{x0:.1f}" '
            f'keyTimes="0;0.4;0.85;1" dur="{step}s" begin="{begin}"/>'
            f'<animate attributeName="opacity" values="1;1;1;0" keyTimes="0;0.5;0.99;1" '
            f'dur="{step}s" begin="{begin}"/></rect>'
        )
    return svg(w, h, "What I build: " + "; ".join(PHRASES), "\n".join(parts))


# ---------------------------------------------------------------- highlights

def highlights(c):
    w, h = 1200, 150
    tile_w, gap = 282, 24
    parts = []
    for i, (value, label, live) in enumerate(HIGHLIGHTS):
        x = i * (tile_w + gap)
        col = c["live"] if live else c["accent"]
        parts.append(
            f'<g class="tile" style="animation-delay:{0.15 * i:.2f}s">'
            f'<rect x="{x + 1}" y="1" width="{tile_w - 2}" height="{h - 2}" rx="16" fill="{c["panel"]}" '
            f'stroke="{c["border"]}"/>'
            f'<rect x="{x + 1}" y="1" width="6" height="{h - 2}" rx="3" fill="{col}"/>'
            f'<text x="{x + 30}" y="72" font-family="{SANS}" font-size="42" font-weight="800" '
            f'fill="{col}">{e(value)}</text>'
            f'<text x="{x + 30}" y="110" font-family="{SANS}" font-size="17" fill="{c["muted"]}">'
            f'{e(label)}</text></g>'
        )
        if live:
            vx = x + 30 + text_width(value, 42, 0.6) + 14
            parts.append(f'<circle cx="{vx:.0f}" cy="58" r="7" fill="{col}"/>'
                         f'<circle cx="{vx:.0f}" cy="58" r="7" fill="none" stroke="{col}" class="ping"/>')
    style = (
        ".ping{transform-box:fill-box;transform-origin:center;animation:ping 2.4s ease-out infinite}"
        "@keyframes ping{0%{transform:scale(1);opacity:.8}100%{transform:scale(2.6);opacity:0}}"
    )
    alt = "Highlights: " + "; ".join(f"{v} {l}" for v, l, _ in HIGHLIGHTS)
    return svg(w, h, alt, "\n".join(parts), style)


# ---------------------------------------------------------------- project cards

def card(p, c):
    w, h = 580, 300
    parts = [
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="{c["panel"]}" '
        f'stroke="{c["border"]}"/>',
        f'<rect x="1" y="1" width="{w - 2}" height="6" rx="3" fill="{c["accent"]}"/>',
        f'<text x="32" y="50" font-family="{MONO}" font-size="14" letter-spacing="2" '
        f'fill="{c["accent"]}">{e(p["tag"])}</text>',
        f'<text x="32" y="92" font-family="{SANS}" font-size="28" font-weight="700" '
        f'fill="{c["text"]}">{e(p["title"])}</text>',
    ]
    for i, line in enumerate(wrap(p["desc"], 17, w - 64)[:3]):
        parts.append(f'<text x="32" y="{128 + i * 25}" font-family="{SANS}" font-size="17" '
                     f'fill="{c["muted"]}">{e(line)}</text>')
    parts.append(chips(p["stack"], 32, 208, c))
    parts.append(f'<line x1="32" y1="252" x2="{w - 32}" y2="252" stroke="{c["border"]}"/>')
    parts.append(f'<text x="32" y="278" font-family="{SANS}" font-size="15" font-weight="600" '
                 f'fill="{c["text"]}">★ {e(p["result"])}</text>')
    parts.append(f'<text x="{w - 32}" y="278" text-anchor="end" font-family="{SANS}" font-size="15" '
                 f'fill="{c["accent"]}">View repo →</text>')
    return svg(w, h, f'{p["title"]}: {p["desc"]}', "\n".join(parts))


def featured_card(p, c):
    w, h = 1200, 330
    parts = [
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="20" fill="{c["panel"]}" '
        f'stroke="{c["border"]}"/>',
        f'<rect x="1" y="1" width="{w - 2}" height="6" rx="3" fill="{c["live"]}"/>',
        f'<circle cx="44" cy="45" r="6" fill="{c["live"]}"/>'
        f'<circle cx="44" cy="45" r="6" fill="none" stroke="{c["live"]}" class="ping"/>',
        f'<text x="60" y="50" font-family="{MONO}" font-size="14" letter-spacing="2" '
        f'fill="{c["live"]}">{e(p["tag"])}</text>',
        f'<text x="36" y="96" font-family="{SANS}" font-size="34" font-weight="800" '
        f'fill="{c["text"]}">{e(p["title"])}</text>',
    ]
    for i, line in enumerate(wrap(p["desc"], 17, 600)[:5]):
        parts.append(f'<text x="36" y="{134 + i * 25}" font-family="{SANS}" font-size="17" '
                     f'fill="{c["muted"]}">{e(line)}</text>')
    parts.append(chips(p["stack"], 36, 268, c))
    # pipeline on the right
    steps = p["flow"]
    x0, x1, y = 720, 1150, 0
    col_w = (x1 - x0) / 2
    positions = []
    for i, step in enumerate(steps):
        col, row = i % 2, i // 2
        positions.append((x0 + col * col_w, 70 + row * 72))
    for i in range(len(positions) - 1):
        (ax, ay), (bx, by) = positions[i], positions[i + 1]
        if ay == by:  # same row: right edge -> left edge
            d = f"M{ax + 190:.0f},{ay + 22} L{bx:.0f},{by + 22}"
        else:  # next row: bottom of box -> top of next box
            d = f"M{ax + 95:.0f},{ay + 44} L{bx + 95:.0f},{by}"
        parts.append(f'<path id="f{i}" d="{d}" stroke="{c["border"]}" stroke-width="2" fill="none"/>')
    for i, (step, (x, yy)) in enumerate(zip(steps, positions)):
        stroke = c["live"] if step == "AI reading" else c["accent"]
        parts.append(
            f'<g class="step" style="animation-delay:{0.25 * i:.2f}s">'
            f'<rect x="{x:.0f}" y="{yy}" width="190" height="44" rx="12" fill="{c["bg"]}" '
            f'stroke="{stroke}" stroke-width="1.5"/>'
            f'<text x="{x + 95:.0f}" y="{yy + 28}" text-anchor="middle" font-family="{SANS}" '
            f'font-size="16" font-weight="600" fill="{c["text"]}">{i + 1}. {e(step)}</text></g>'
        )
    for i in range(len(positions) - 1):
        parts.append(
            f'<circle r="4" fill="{c["live"]}"><animateMotion dur="1s" begin="{i}s;{i}s+{len(steps)}s" '
            f'repeatCount="indefinite"><mpath href="#f{i}"/></animateMotion></circle>'
        )
    parts.append(f'<text x="935" y="300" text-anchor="middle" font-family="{SANS}" font-size="15" '
                 f'font-weight="600" fill="{c["text"]}">★ {e(p["result"])}</text>')
    style = (
        ".ping{transform-box:fill-box;transform-origin:center;animation:ping 2.4s ease-out infinite}"
        "@keyframes ping{0%{transform:scale(1);opacity:.8}100%{transform:scale(2.8);opacity:0}}"
    )
    return svg(w, h, f'{p["title"]}: {p["desc"]} {p["result"]}', "\n".join(parts), style)


# ---------------------------------------------------------------- experience timeline

def timeline(c):
    row = 96
    w, h = 1200, 40 + row * len(ROLES)
    line_x = 300
    parts = [f'<line x1="{line_x}" y1="40" x2="{line_x}" y2="{h - 40}" stroke="{c["border"]}" '
             f'stroke-width="2"/>']
    for i, (period, role, org, what, current) in enumerate(ROLES):
        y = 50 + i * row
        col = c["live"] if current else c["accent"]
        parts.append(f'<g class="row" style="animation-delay:{0.2 * i:.1f}s">')
        parts.append(f'<text x="{line_x - 32}" y="{y + 8}" text-anchor="end" font-family="{MONO}" '
                     f'font-size="16" fill="{c["muted"]}">{e(period)}</text>')
        parts.append(f'<circle cx="{line_x}" cy="{y + 2}" r="9" fill="{c["bg"]}" stroke="{col}" '
                     f'stroke-width="3"/>')
        if current:
            parts.append(f'<circle cx="{line_x}" cy="{y + 2}" r="9" fill="none" stroke="{col}" '
                         f'class="ping"/>')
        parts.append(f'<text x="{line_x + 34}" y="{y + 9}" font-family="{SANS}" font-size="22" '
                     f'font-weight="700" fill="{c["text"]}">{e(role)} '
                     f'<tspan fill="{col}">· {e(org)}</tspan></text>')
        parts.append(f'<text x="{line_x + 34}" y="{y + 38}" font-family="{SANS}" font-size="17" '
                     f'fill="{c["muted"]}">{e(what)}</text>')
        parts.append('</g>')
    style = (
        ".ping{transform-box:fill-box;transform-origin:center;animation:ping 2.4s ease-out infinite}"
        "@keyframes ping{0%{transform:scale(1);opacity:.8}100%{transform:scale(2.4);opacity:0}}"
    )
    alt = "Experience: " + "; ".join(f"{r} at {o}, {p}" for p, r, o, _, _ in ROLES)
    return svg(w, h, alt, "\n".join(parts), style)


# ---------------------------------------------------------------- footer

def footer(c):
    w, h = 1200, 90
    wave = "M0,50 C150,20 300,80 450,50 C600,20 750,80 900,50 C1050,20 1200,80 1350,50 " \
           "C1500,20 1650,80 1800,50 C1950,20 2100,80 2250,50 C2400,20 2550,80 2700,50"
    parts = [
        f'<g class="drift"><path d="{wave}" fill="none" stroke="{c["accent"]}" stroke-width="2" '
        f'opacity="0.55"/></g>',
        f'<g class="drift slow"><path d="{wave}" transform="translate(0,12)" fill="none" '
        f'stroke="{c["live"]}" stroke-width="1.5" opacity="0.35"/></g>',
    ]
    style = (
        ".drift{animation:drift 14s linear infinite}.slow{animation-duration:22s}"
        "@keyframes drift{from{transform:translateX(0)}to{transform:translateX(-900px)}}"
    )
    return svg(w, h, "Decorative wave", "\n".join(parts), style)


def main():
    out = {}
    for name, c in THEMES.items():
        out[f"hero-{name}.svg"] = hero(c)
        out[f"typing-{name}.svg"] = typing(c)
        out[f"highlights-{name}.svg"] = highlights(c)
        out[f"timeline-{name}.svg"] = timeline(c)
        out[f"footer-{name}.svg"] = footer(c)
        out[f"cards/{FEATURED['slug']}-{name}.svg"] = featured_card(FEATURED, c)
        for p in PROJECTS:
            out[f"cards/{p['slug']}-{name}.svg"] = card(p, c)
    for rel, content in out.items():
        path = ASSETS / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"wrote {len(out)} files to {ASSETS}")


if __name__ == "__main__":
    main()
