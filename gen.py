import os
from xml.sax.saxutils import escape as esc
FONT = "Roboto, 'Google Sans', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"

# Material 3 baseline (purple) color roles
P = {
 "light": dict(surface="#FEF7FF", cont="#F3EDF7", high="#ECE6F0", primary="#6750A4", onPrimary="#FFFFFF",
   pc="#EADDFF", onPc="#21005D", sc="#E8DEF8", onSc="#1D192B", tc="#FFD8E4", onTc="#31111D",
   onSurface="#1D1B20", onVar="#49454F", outline="#79747E"),
 "dark": dict(surface="#141218", cont="#211F26", high="#2B2930", primary="#D0BCFF", onPrimary="#381E72",
   pc="#4F378B", onPc="#EADDFF", sc="#4A4458", onSc="#E8DEF8", tc="#633B48", onTc="#FFD8E4",
   onSurface="#E6E0E9", onVar="#CAC4D0", outline="#938F99"),
}

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{esc(title)}" font-family="{FONT}"><title>{esc(title)}</title>\n{body}\n</svg>\n')

def T(x, y, s, size, weight, fill, anchor="start", ls=0):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(s)}</text>'

for _m in ("light", "dark"):
    os.makedirs(f"assets/{_m}", exist_ok=True)

def out(mode, name, s):
    open(f"assets/{mode}/{name}.svg", "w").write(s)

for mode, c in P.items():
    # ---- hero: primary-container surface, M3 shapes reflecting actual projects ----
    b = '<clipPath id="c"><rect width="1000" height="260" rx="28"/></clipPath>'
    b += f'<rect width="1000" height="260" rx="28" fill="{c["pc"]}"/><g clip-path="url(#c)">'
    b += f'<rect x="760" y="60" width="120" height="200" rx="28" fill="{c["sc"]}"/>'
    b += f'<rect x="780" y="80" width="80" height="160" rx="16" fill="{c["primary"]}" opacity="0.85"/>'
    b += f'<circle cx="820" cy="100" r="6" fill="{c["onPc"]}"/>'
    b += f'<circle cx="820" cy="120" r="4" fill="{c["onPc"]}" opacity="0.5"/>'
    b += f'<circle cx="820" cy="135" r="4" fill="{c["onPc"]}" opacity="0.5"/>'
    b += f'<rect x="880" y="70" width="140" height="90" rx="20" fill="{c["tc"]}"/>'
    b += f'<rect x="895" y="85" width="110" height="60" rx="8" fill="{c["onTc"]}" opacity="0.2"/>'
    b += f'<rect x="700" y="170" width="100" height="40" rx="20" fill="{c["primary"]}"/>'
    b += f'<circle cx="930" cy="210" r="24" fill="{c["primary"]}"/>'
    b += f'<circle cx="950" cy="190" r="16" fill="{c["tc"]}"/>'
    b += '</g>'
    b += T(56, 130, "Md. Rony Hossen", 80, 500, c["onPc"], ls=-2)
    b += T(58, 186, "Computer Hardware Enthusiast and Web Developer", 26, 400, c["onPc"])
    out(mode, "hero", svg(1000, 260, b, "Md. Rony Hossen - Computer Hardware Enthusiast and Web Developer"))

    # ---- buttons: filled / tonal, 40px pill ----
    for name, label, w, kind in [("btn-email", "Email", 96, "filled"), ("btn-linkedin", "LinkedIn", 112, "tonal"),
                                 ("btn-portfolio", "Portfolio", 114, "tonal"), ("btn-telegram", "Telegram", 120, "filled")]:
        if kind == "filled":
            b = f'<rect width="{w}" height="40" rx="20" fill="{c["primary"]}"/>' + T(w/2, 25, label, 14, 500, c["onPrimary"], "middle", .1)
        else:
            b = f'<rect width="{w}" height="40" rx="20" fill="{c["sc"]}"/>' + T(w/2, 25, label, 14, 500, c["onSc"], "middle", .1)
        out(mode, name, svg(w, 40, b, label))