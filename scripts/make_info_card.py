svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 350" width="490" style="background: #0d1117; font-family: monospace; font-size: 14px;">
  <style>
    .title { fill: #58a6ff; font-weight: bold; }
    .key { fill: #7ee787; }
    .val { fill: #c9d1d9; }
  </style>
  <rect width="100%" height="100%" rx="6" fill="#161b22"/>
  <text x="20" y="30" class="title">alikaklk@github</text>
  <text x="20" y="60" class="key">------------------</text>
  <text x="20" y="90" class="key">Now:  <tspan class="val">Building awesome projects</tspan></text>
  <text x="20" y="125" class="key">Prev: <tspan class="val">Full-stack engineering</tspan></text>
  <text x="20" y="160" class="key">Stack:<tspan class="val">Python, JavaScript, Git</tspan></text>
  <text x="20" y="195" class="key">Goal: <tspan class="val">Open source contributions</tspan></text>
</svg>"""

with open("info-card.svg", "w") as f:
    f.write(svg_content)
print("info-card.svg oluşturuldu.")
