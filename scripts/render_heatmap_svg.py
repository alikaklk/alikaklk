import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

try:
    with open("data/contributions.json", "r") as f:
        days = json.load(f)
except FileNotFoundError:
    days = []

svg_lines = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 140" width="860" style="background: #0d1117; font-family: monospace;">',
    '<style>.label { fill: #8b949e; font-size: 11px; }</style>'
]

x_offset = 10
y_offset = 20
for i, day in enumerate(days):
    col = i // 7
    row = i % 7
    color = PALETTE[day.get('level', 0)]
    svg_lines.append(f'<rect x="{x_offset + col * 12}" y="{y_offset + row * 12}" width="10" height="10" rx="2" fill="{color}"/>')

svg_lines.append('</svg>')

with open("contrib-heatmap.svg", "w") as f:
    f.write("\n".join(svg_lines))
print("contrib-heatmap.svg oluşturuldu.")
