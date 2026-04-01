import csv
from pathlib import Path
from datetime import datetime
from html import escape

ROOT = Path(__file__).resolve().parent
csv_file = ROOT / "data.csv"
html_file = ROOT / "index.html"

rows = []
with open(csv_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

def norm(x: str) -> str:
    return (x or "").strip()

def is_yes(x: str) -> bool:
    return norm(x).lower() == "yes"

def detection_string(r: dict) -> str:
    parts = []
    if is_yes(r.get("fft", "")):
        parts.append("FFT")
    if is_yes(r.get("ffa", "")):
        parts.append("FFA")
    if is_yes(r.get("sp", "")):
        parts.append("SP")
    return ", ".join(parts) if parts else "-"

total = len(rows)
confirmed = sum(1 for r in rows if norm(r.get("status", "")).lower() == "confirmed")
candidates = sum(1 for r in rows if norm(r.get("status", "")).lower() == "candidate")
timing_updates = sum(1 for r in rows if norm(r.get("status", "")).lower() == "timing_update")

table_rows = []
for r in rows:
    table_rows.append(f"""
    <tr>
      <td>{escape(norm(r.get('catalog_id', '')))}</td>
      <td>{escape(norm(r.get('psrj', '')))}</td>
      <td>{escape(norm(r.get('ra_beam_center', '')))}</td>
      <td>{escape(norm(r.get('dec_beam_center', '')))}</td>
      <td>{escape(norm(r.get('p0_s', '')))}</td>
      <td>{escape(norm(r.get('dm_pc_cm3', '')))}</td>
      <td>{escape(detection_string(r))}</td>
      <td>{escape(norm(r.get('discovery_date', '')))}</td>
      <td>{escape(norm(r.get('project_id', '')))}</td>
      <td>{escape(norm(r.get('source_name', '')))}</td>
      <td>{escape(norm(r.get('beam_id', '')))}</td>
      <td>{escape(norm(r.get('obs_date', '')))}</td>
      <td>{escape(norm(r.get('status', '')))}</td>
      <td>{escape(norm(r.get('note', '')))}</td>
    </tr>
    """)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PulsarGleaners</title>
  <style>
    body {{
      font-family: Arial, Helvetica, sans-serif;
      max-width: 1280px;
      margin: 36px auto;
      padding: 0 20px 40px;
      line-height: 1.5;
      color: #222;
    }}
    h1 {{
      margin-bottom: 0.2em;
    }}
    .subtitle {{
      color: #555;
      margin-top: 0;
    }}
    .stats {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin: 20px 0 18px;
    }}
    .card {{
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 12px 16px;
      min-width: 150px;
      background: #fafafa;
    }}
    .note {{
      background: #f7f7f7;
      border-left: 4px solid #999;
      padding: 10px 12px;
      margin: 14px 0;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 18px;
      font-size: 14px;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px 10px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: #f2f2f2;
      position: sticky;
      top: 0;
    }}
    code {{
      background: #f1f1f1;
      padding: 2px 6px;
      border-radius: 6px;
    }}
    .footer {{
      margin-top: 20px;
      color: #666;
      font-size: 13px;
    }}
  </style>
</head>
<body>
  <h1>PulsarGleaners</h1>
  <p class="subtitle">Pulsar discoveries and candidates identified from public archive data.</p>

  <div class="stats">
    <div class="card"><strong>Total Pulsars</strong><br>{total}</div>
  </div>

  <div class="note">
    Coordinates listed here are beam-center coordinates. Names ending with <code>t</code> are provisional unless otherwise noted.
  </div>

  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>PSRJ</th>
        <th>RA</th>
        <th>DEC</th>
        <th>P0 (s)</th>
        <th>DM</th>
        <th>Detection</th>
        <th>Discovery date</th>
        <th>Project ID</th>
        <th>Source Name</th>
        <th>Beam ID</th>
        <th>Obs date</th>
        <th>Status</th>
        <th>Note</th>
      </tr>
    </thead>
    <tbody>
      {''.join(table_rows)}
    </tbody>
  </table>

  <p class="footer">Last generated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}</p>
</body>
</html>
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated: {html_file}")