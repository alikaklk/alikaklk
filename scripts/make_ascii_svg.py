from PIL import Image
import math

RAMP = " .`:-=+*#%@"
WIDTH = 100
HEIGHT = 53

img = Image.open("source-prepped.png").resize((WIDTH, HEIGHT))
pixels = img.load()

svg_lines = []
svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH * 8} {HEIGHT * 15}" width="370" style="background: #0d1117; font-family: monospace;">')
svg_lines.append('<style>')
svg_lines.append('text { fill: #c9d1d9; font-size: 14px; dominant-baseline: hanging; }')
svg_lines.append('</style>')

for y in range(HEIGHT):
    row_chars = []
    for x in range(WIDTH):
        brightness = pixels[x, y]
        idx = math.floor((brightness / 255) * (len(RAMP) - 1))
        char = RAMP[idx]
        if char == ' ':
            char = '&nbsp;'
        row_chars.append(char)
    
    row_str = "".join(row_chars)
    y_pos = y * 15
    svg_lines.append(f'<text x="0" y="{y_pos}">{row_str}</text>')

svg_lines.append('</svg>')

with open("avi-ascii.svg", "w") as f:
    f.write("\n".join(svg_lines))
print("avi-ascii.svg oluşturuldu.")
