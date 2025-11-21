# Udacity Marketing Analytics Projects

This repository contains three independent marketing analytics projects. Each folder has its own data, scripts, visuals, and detailed README—use this document as a quick launchpad.

## Projects Overview

### 1) Crafting an Analytics Brief (`crafting_analytics_brief`)
- **Goal:** Build a strategic analytics brief for Boston Dynamics Spot Enterprise in Energy & Utilities, with a 14-slide HTML deck and funnel visualization.
- **Key files:** `analytics_brief.py`, `analytics_brief_presentation.html`, `purchase_funnel.png`, `SOURCES.md`.
- **Run:**  
  ```bash
  cd crafting_analytics_brief
  python analytics_brief.py
  ```
- **Notes:** Requires `matplotlib`; install with `python -m pip install --user matplotlib`.

### 2) Sales Objective Analysis (`sales_objective_analysis`)
- **Goal:** Compare Black Friday 2017 vs 2018 across objectives, audience, marketing, sales, and products.
- **Key files:** `marketing_analysis.py`, `PROJECT_ANALYSIS_REPORT.md`, `part*.png`, `Project_ Create a Proposal for the Next Quarter - Sample_Dataset.xlsx`.
- **Run:**  
  ```bash
  cd sales_objective_analysis
  python marketing_analysis.py
  ```
- **Deps:** `pandas openpyxl matplotlib seaborn numpy` (install via `python -m pip install --user pandas openpyxl matplotlib seaborn numpy`).

### 3) Visual Storytelling with Data (`storytelling_with_data`)
- **Goal:** Explain when gift shoppers buy (UK ecommerce) with minimalist visuals and a simple HTML story.
- **Key files:** `storytelling_analysis.py`, `story_visual_*.png`, `story_presentation.html`, `data.csv`.
- **Run:**  
  ```bash
  cd storytelling_with_data
  python storytelling_analysis.py
  ```
- **Deps:** `pandas matplotlib numpy`.

## Environment Notes
- Python 3.x; user installs (`--user`) are fine if system site-packages are read-only.
- If `matplotlib` is “missing” but installed, confirm `python -m pip show matplotlib` uses the same interpreter and that user site-packages are on `sys.path` (no `PYTHONNOUSERSITE`).

## Repo Layout
- `crafting_analytics_brief/` – Strategic brief + funnel viz.
- `sales_objective_analysis/` – Black Friday KPI deep dive + charts.
- `storytelling_with_data/` – Seasonal ecommerce story + visuals.

For full context, see each subfolder’s README and supporting files. This file is intended to get you running quickly across all three projects.
