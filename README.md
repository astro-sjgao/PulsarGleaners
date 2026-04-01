# Pulsar Gleaners

**Pulsar Gleaners** is a project aimed at identifying pulsars in archival observations from the Five-hundred-meter Aperture Spherical radio Telescope (FAST), including data that were originally obtained for purposes other than pulsar searching. Some of these observations were not originally designed for pulsar surveys, or the pulsars were detected in non-central beams during observations targeting other sources.

This work represents an effort to fully exploit the scientific potential of archival FAST data through reprocessing and dedicated pulsar search techniques, including FFT, FFA, and single-pulse searches.

We gratefully acknowledge all FAST project PIs who made the original observations. This work is entirely based on archival data products and demonstrates the additional scientific return enabled by archival data reuse.

The term “gleaners” in the title *Pulsar Gleaners* originates from the 1857 oil painting *The Gleaners* by Jean-François Millet, which depicts three peasant women collecting stray stalks of wheat left in a field after the harvest. In a similar spirit, this project focuses on searching for pulsars in archival data - sources that were not the primary targets of the original observations, but can still be discovered through careful reprocessing and analysis. The name reflects the idea of “gleaning” additional scientific discoveries from existing data.

---

## Online Catalog

A web-based catalog of pulsars and candidates discovered in FAST archival data is available here:

**GitHub Pages catalog:**  
https://astro-sjgao.github.io/PulsarGleaners/

---

## Repository Contents

- `data.csv`  
  Machine-readable table of pulsars and candidates discovered in FAST archival data.

- `index.html`  
  Generated static catalog webpage (used for GitHub Pages).

- `build_html.py`  
  Script used to generate `index.html` from `data.csv`.

- `timing/`  
  Pulsars with timing solutions. Contains `.par` and `.tim` files.

- `fold/`  
  Folded plots and single-pulse diagnostic plots.

---

## Notes on Positions and Names

- The listed coordinates are **beam-center coordinates** at the time of detection and are not necessarily final timing positions (~3' beam width).
- Source names ending with `t` are **provisional discovery names** unless otherwise noted.
- Some sources have been confirmed using independent archival observations.

---

## Publications

Some pulsars from this project have been published in:
**Gao et al. 2026, ApJ, 997, 210**  
https://ui.adsabs.harvard.edu/abs/2026ApJ...997..210G/abstract

---