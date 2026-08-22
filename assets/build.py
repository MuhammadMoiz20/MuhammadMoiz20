#!/usr/bin/env python3
"""
Generates every SVG panel on this profile, in a light and a dark variant.

    python3 assets/build.py

Nothing here is fetched from a badge service. The panels are hand-authored SVG
with CSS animation. GitHub proxies README images through camo, which strips
SMIL, so every panel is authored to read correctly with no animation at all --
the motion is enhancement, never the content. One theme dict below is the single source of truth for colour.
"""

from pathlib import Path

OUT = Path(__file__).parent
W = 880
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(
        bg="#0d1117", panel="#010409", border="#30363d", chrome="#161b22",
        fg="#c9d1d9", dim="#8b949e", faint="#484f58",
        green="#3fb950", blue="#58a6ff", amber="#d29922", purple="#bc8cff",
        red="#ff7b72", cyan="#39c5cf", grid="#161b22",
    ),
    "light": dict(
        bg="#ffffff", panel="#f6f8fa", border="#d0d7de", chrome="#eaeef2",
        fg="#1f2328", dim="#59636e", faint="#9198a1",
        green="#1a7f37", blue="#0969da", amber="#9a6700", purple="#8250df",
        red="#cf222e", cyan="#1b7c83", grid="#eaeef2",
    ),
}


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def head(w, h, t):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(t)}">'
        f'<title>{esc(t)}</title>'
    )


def window(t, title, h, y0=0):
    """Terminal chrome: rounded panel, title bar, three lights."""
    return f"""
  <rect x="0.5" y="{y0}.5" width="{W-1}" height="{h-1}" rx="10" fill="{t['panel']}" stroke="{t['border']}"/>
  <path d="M0.5 {y0+10}.5a10 10 0 0 1 10-10h859a10 10 0 0 1 10 10v22h-879z" fill="{t['chrome']}" stroke="{t['border']}"/>
  <circle cx="20" cy="{y0+17}" r="5" fill="{t['red']}" opacity="0.85"/>
  <circle cx="38" cy="{y0+17}" r="5" fill="{t['amber']}" opacity="0.85"/>
  <circle cx="56" cy="{y0+17}" r="5" fill="{t['green']}" opacity="0.85"/>
  <text x="{W//2}" y="{y0+21}" font-family="{MONO}" font-size="12" fill="{t['dim']}" text-anchor="middle">{esc(title)}</text>"""


# --------------------------------------------------------------------------- 1
def header(t, name):
    """Animated boot console. Lines type in sequence via an expanding clip."""
    h = 268
    lines = [
        ("prompt", "whoami", None),
        ("out", "Muhammad Moiz  ·  Dartmouth CS '26  ·  Hartford, VT", "fg"),
        ("prompt", "cat ~/.plan", None),
        ("out", "Backend & distributed systems. Python/FastAPI, Postgres, async workers.", "dim"),
        ("out", "I build the part users never see and always feel.", "dim"),
        ("prompt", "echo $NEXT", None),
        ("out", "AI Infrastructure Engineering  →  make inference boring, cheap, observable", "blue"),
    ]
    s = [head(W, h, "Terminal boot sequence"), f'<rect width="{W}" height="{h}" fill="none"/>',
         window(t, f"{name}@thayer — zsh — 96x24", h)]

    y = 62
    delay = 0.25
    clips, keys, rules = [], [], []
    for i, (kind, text, color) in enumerate(lines):
        cid = f"c{i}"
        chars = len(text) + (2 if kind == "prompt" else 0)
        span = 34 + chars * 8.8
        dur = max(0.22, chars * 0.017)
        # Static width is the FULL span: if the host strips animation (GitHub's
        # image proxy does), every line is simply already typed out.
        clips.append(
            f'<clipPath id="{cid}"><rect id="r{i}" x="0" y="{y-16}" '
            f'height="24" width="{span:.0f}"/></clipPath>')
        keys.append(f"@keyframes t{i}{{from{{width:0}}to{{width:{span:.0f}px}}}}")
        rules.append(f"#r{i}{{animation:t{i} {dur:.2f}s linear {delay:.2f}s backwards}}")
        if kind == "prompt":
            s_line = (f'<g clip-path="url(#{cid})"><text x="22" y="{y}" font-size="14.5">'
                      f'<tspan fill="{t["green"]}">\\u276f</tspan>'
                      f'<tspan fill="{t["fg"]}"> {esc(text)}</tspan></text></g>')
        else:
            s_line = (f'<g clip-path="url(#{cid})"><text x="22" y="{y}" font-size="14.5" '
                      f'fill="{t[color]}">{esc(text)}</text></g>')
        s.append(s_line)
        y += 27 if kind == "prompt" else 25
        delay += dur + (0.14 if kind == "prompt" else 0.06)

    # trailing prompt + blinking cursor. Static state: solid caret, already shown.
    keys.append("@keyframes fadein{from{opacity:0}to{opacity:1}}")
    keys.append("@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}")
    rules.append(f"#tail{{animation:fadein 0.2s linear {delay:.2f}s backwards}}")
    rules.append(f"#caret{{animation:blink 1.06s step-end {delay:.2f}s infinite}}")
    s.append(f'<g id="tail"><text x="22" y="{y+4}" font-size="14.5" fill="{t["green"]}">\\u276f</text>'
             f'<rect id="caret" x="38" y="{y-8}" width="9" height="15" fill="{t["green"]}"/></g>')
    s.append("<style>" + "".join(keys) + "".join(rules) + "</style>")
    s.insert(2, "<defs>" + "".join(clips) + "</defs>")
    s.append("</svg>")
    return "".join(s)


# --------------------------------------------------------------------------- 2
def services(t):
    """systemctl-style board of what is actually running right now."""
    rows = [
        ("evergreen.service", "active", "green", "DALI Lab · FastAPI + Google OAuth + MCP server"),
        ("classmoji.service", "active", "green", "DALI Lab · led JS→TS migration, 8-workspace monorepo"),
        ("ishaq-dar.service", "active", "green", "financial OS · LLM does zero arithmetic, by design"),
        ("moji-proctor.service", "active", "green", "tamper-evident commit provenance · Ed25519 chain"),
        ("h1b-model.service", "exited", "amber", "denial prediction · honest negative result across regimes"),
        ("neetcode.timer", "waiting", "blue", "150 problems · fires daily, no snooze"),
    ]
    h = 78 + len(rows) * 30 + 18
    s = [head(W, h, "Service status board"), window(t, "systemctl --user status — moiz.target", h)]
    s.append(f'<text x="22" y="58" font-family="{MONO}" font-size="13" fill="{t["dim"]}">'
             f'<tspan fill="{t["green"]}">❯</tspan> systemctl --user list-units --type=service</text>')
    y = 88
    s.append("<style>@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}</style>")
    for i, (unit, state, color, desc) in enumerate(rows):
        s.append(f'<circle cx="28" cy="{y-4}" r="4" fill="{t[color]}" '
                 f'style="animation:pulse 2.4s ease-in-out {i*0.32:.2f}s infinite"/>')
        s.append(f'<text x="44" y="{y}" font-size="13.5" fill="{t["fg"]}">{esc(unit)}</text>')
        s.append(f'<text x="252" y="{y}" font-size="13.5" fill="{t[color]}">{esc(state)}</text>')
        s.append(f'<text x="330" y="{y}" font-size="13" fill="{t["dim"]}">{esc(desc)}</text>')
        y += 30
    return "".join(s) + "</svg>"


# --------------------------------------------------------------------------- 3
def dataplane(t):
    """A request walking the stack I actually build. Animated packets."""
    h = 250
    s = [head(W, h, "Request path through the stack"), window(t, "trace — one request, end to end", h)]

    nodes = [
        (70, "client", "browser", "blue"),
        (222, "edge", "CDN / TLS", "cyan"),
        (374, "api", "FastAPI", "green"),
        (526, "queue", "Redis · arq", "amber"),
        (678, "db", "Postgres RLS", "purple"),
    ]
    cy = 128
    bw, bh = 118, 54
    # rail
    s.append(f'<line x1="{70+bw//2}" y1="{cy}" x2="{678-bw//2}" y2="{cy}" stroke="{t["border"]}" stroke-width="2"/>')

    # travelling packets. Static state: three dots resting on the rail.
    x0, x1 = 70 + bw // 2, 678 - bw // 2
    span = x1 - x0
    keys = ["@keyframes flow{from{transform:translateX(0);opacity:0}"
            "8%{opacity:.95}92%{opacity:.95}"
            "to{transform:translateX(" + str(span) + "px);opacity:0}}"]
    rules = []
    for i, d in enumerate((0, 1.6, 3.2)):
        rules.append(f".p{i}{{animation:flow 4.8s linear {d}s infinite}}")
        s.append(f'<circle class="p{i}" r="4.5" cx="{x0 + i * (x1 - x0) // 3}" cy="{cy}" '
                 f'fill="{t["green"]}" opacity="0.9"/>')
    s.append("<style>" + "".join(keys) + "".join(rules) + "</style>")

    for x, key, label, color in nodes:
        s.append(f'<rect x="{x-bw//2}" y="{cy-bh//2}" width="{bw}" height="{bh}" rx="8" '
                 f'fill="{t["bg"]}" stroke="{t[color]}" stroke-width="1.4"/>')
        s.append(f'<text x="{x}" y="{cy-6}" font-family="{MONO}" font-size="11" fill="{t["dim"]}" '
                 f'text-anchor="middle">{esc(key)}</text>')
        s.append(f'<text x="{x}" y="{cy+13}" font-family="{MONO}" font-size="13" fill="{t[color]}" '
                 f'text-anchor="middle">{esc(label)}</text>')

    # return path
    s.append(f'<path d="M{x1} {cy+38} H{x0}" stroke="{t["faint"]}" stroke-width="1.2" stroke-dasharray="4 5"/>')
    s.append(f'<text x="{W//2}" y="{cy+56}" font-family="{MONO}" font-size="11.5" fill="{t["faint"]}" '
             f'text-anchor="middle">← 200 OK · p99 is a feature, not a graph</text>')

    caption = "every box is somewhere I have had to debug at 2am"
    s.append(f'<text x="22" y="58" font-family="{MONO}" font-size="13" fill="{t["dim"]}">'
             f'<tspan fill="{t["green"]}">❯</tspan> trace --follow  <tspan fill="{t["faint"]}">'
             f'# {esc(caption)}</tspan></text>')
    s.append(f'<text x="22" y="{h-18}" font-family="{MONO}" font-size="11.5" fill="{t["faint"]}">'
             f'auth: OAuth/OIDC   ·   isolation: row-level security   ·   jobs: async workers   ·   '
             f'ship: Docker + GH Actions</text>')
    return "".join(s) + "</svg>"


# --------------------------------------------------------------------------- 4
def stack(t):
    """~/.config/stack.toml — the honest version, with confidence tiers."""
    groups = [
        ("daily", "green", ["Python", "FastAPI", "TypeScript", "PostgreSQL", "Docker", "Pydantic", "SQLAlchemy"]),
        ("fluent", "blue", ["React", "Next.js", "Node", "Redis", "GraphQL", "Prisma", "Playwright"]),
        ("shipped_with", "amber", ["AWS Lambda", "S3", "DynamoDB", "SQS", "RabbitMQ", "NestJS", "Go"]),
        ("learning", "purple", ["CUDA-adjacent infra", "vLLM", "Ray", "distributed training"]),
    ]
    h = 78 + len(groups) * 46 + 14
    s = [head(W, h, "Stack"), window(t, "~/.config/stack.toml", h)]
    s.append(f'<text x="22" y="58" font-family="{MONO}" font-size="13" fill="{t["dim"]}">'
             f'<tspan fill="{t["green"]}">❯</tspan> bat ~/.config/stack.toml</text>')
    y = 86
    for key, color, items in groups:
        s.append(f'<text x="26" y="{y}" font-family="{MONO}" font-size="13.5" fill="{t[color]}">{esc(key)}</text>')
        s.append(f'<text x="26" y="{y+20}" font-family="{MONO}" font-size="12.5" fill="{t["fg"]}">'
                 f'<tspan fill="{t["faint"]}">= [ </tspan>{esc("  ".join(items))}<tspan fill="{t["faint"]}"> ]</tspan></text>')
        y += 46
    return "".join(s) + "</svg>"


def slim(svg):
    """Hoist the repeated font stack into one <style> rule."""
    svg = svg.replace(f'font-family="{MONO}" ', "")
    style = f"<style>text{{font-family:{MONO}}}</style>"
    return svg.replace("</title>", "</title>" + style, 1)


def main():
    for theme, t in THEMES.items():
        (OUT / f"header-{theme}.svg").write_text(slim(header(t, "moiz")))
        (OUT / f"services-{theme}.svg").write_text(slim(services(t)))
        (OUT / f"dataplane-{theme}.svg").write_text(slim(dataplane(t)))
        (OUT / f"stack-{theme}.svg").write_text(slim(stack(t)))
    print("wrote", len(list(OUT.glob("*.svg"))), "svgs")


if __name__ == "__main__":
    main()
