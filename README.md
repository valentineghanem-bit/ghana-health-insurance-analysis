# NHIS Uninsurance & Health Equity — Ghana 261 Districts

[![CI](https://github.com/valentineghanem-bit/ghana-health-insurance-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/valentineghanem-bit/ghana-health-insurance-analysis/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/) [![R 4.3+](https://img.shields.io/badge/R-4.3+-blue.svg)](https://www.r-project.org/) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--8332--0220-green.svg)](https://orcid.org/0009-0002-8332-0220)

**Author:** Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic, Accra, Ghana
**ORCID:** [0009-0002-8332-0220](https://orcid.org/0009-0002-8332-0220)
**Affiliation:** Ghana COCOBOD Cocoa Clinic, Accra, Ghana
**Reporting standard:** STROBE · RECORD-Spatial · TRIPOD+AI
**Date:** 2026
**Status:** Manuscript in preparation

## 1. Abstract

Ghana's National Health Insurance Scheme (NHIS), established in 2003, aims for universal health coverage but faces a persistent "subscription paradox" driven by poverty, geographic remoteness, and low literacy. This ecological study analyses all 261 districts using 2021 Population and Housing Census data integrated with NHIS administrative registers. Spatial econometrics (Global Moran's I = 0.54, p < 0.001) confirm strong spatial clustering of uninsurance. An XGBoost classifier (AUC = 0.87, LOROCV) identifies poverty incidence (SHAP 3.82) and illiteracy rate (SHAP 2.94) as the dominant barriers. Out-of-pocket expenditure as a share of current health expenditure declined from 44.4% (2000) to 26.4% (2022), signalling partial NHIS impact. High-High uninsurance clusters concentrate in the Oti, Savannah, and Northern belt (54 districts), calling for targeted enrolment interventions.

## 2. Research Question & Aims

**Primary question:** What spatial patterns and socioeconomic determinants drive district-level NHIS uninsurance inequities across Ghana's 261 districts?

**Aims:**
1. Map the spatial distribution and clustering of NHIS uninsurance at district level.
2. Identify socioeconomic determinants using XGBoost and SHAP explainability.
3. Quantify the temporal trend in out-of-pocket health expenditure (2000–2022).
4. Delineate high-burden clusters to guide targeted policy intervention.

## 3. Methods Summary

| Method | Tool | Purpose |
|--------|------|---------|
| Global Moran's I | PySAL (Python) | Spatial autocorrelation of uninsurance |
| Bivariate LISA | PySAL/esda (Python) | Local cluster and outlier detection |
| Getis-Ord Gi* | PySAL (Python) | Hotspot and coldspot identification |
| XGBoost | scikit-learn (Python) | District uninsurance prediction (AUC=0.87) |
| SHAP | shap (Python) | Feature importance and explainability |
| LOROCV | custom (Python) | Leave-one-region-out cross-validation |

## 4. Data Sources

| Source | Variables | Year | Access |
|--------|-----------|------|--------|
| Ghana Population & Housing Census (PHC) | Uninsurance rate, population, literacy | 2021 | Public — GSS |
| NHIS Administrative Register | Enrolment, active membership | 2021–2022 | Restricted — NHIA |
| WHO Global Health Expenditure Database | OOP as % CHE | 2000–2022 | Public — WHO GHE |
| Ghana Health Service (GHS) | Facility density, healthcare access | 2022 | Public — GHS |
| Ghana Statistical Service (GSS) | Poverty incidence, employment | 2021 | Public — GSS |
| Ghana 260-District GeoJSON | Administrative boundaries | 2021 | Public — GADM |

## 5. Key Findings

| Metric | Value |
|--------|-------|
| Global Moran's I (uninsurance) | 0.54 (p < 0.001) |
| Highest uninsurance | 47.7% — Oti Region |
| Lowest uninsurance | 13.5% — Upper East Region |
| National average uninsurance | 31.1% (261 districts pooled) |
| XGBoost AUC (LOROCV) | 0.87 |
| Top predictor (SHAP) | Poverty incidence (3.82) |
| OOP as % CHE 2000 | 44.4% |
| OOP as % CHE 2022 | 26.4% (−18 pp improvement) |
| High-High cluster districts | 54 (Oti, Savannah, Northern belt) |

## 6. Repository Structure

```
ghana-health-insurance-analysis/
├── dashboard/
│   └── NHIS_OOP_Ghana_Dashboard.html
├── poster/
│   └── NHIS_OOP_Ghana_Poster.html
├── scripts/
│   ├── analysis_pipeline.py
│   ├── spatial_utils.py
│   └── spatial_diagnostics.R
├── tests/
│   └── test_pipeline.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── analysis.R
├── requirements.txt
├── CITATION.cff
├── LICENSE
└── README.md
```

## 7. Reproducibility

### 7.1 Requirements

- Python 3.12+ with packages in `requirements.txt`
- R 4.3+ with `spdep`, `spatialreg`, `dplyr`, `ggplot2`

### 7.2 Clone & install

```bash
git clone https://github.com/valentineghanem-bit/ghana-health-insurance-analysis.git
cd ghana-health-insurance-analysis
pip install -r requirements.txt
```

### 7.3 Run the analytical pipeline

```bash
bash run_all.sh
```

### 7.4 Run the test suite

```bash
pytest tests/ -v
```

### 7.5 Launch the interactive Dash application

```bash
python app.py
```

### 7.6 Open the static HTML dashboard

```bash
# macOS
open dashboard/NHIS_OOP_Ghana_Dashboard.html
# Windows
start dashboard/NHIS_OOP_Ghana_Dashboard.html
# Linux
xdg-open dashboard/NHIS_OOP_Ghana_Dashboard.html
```

## 8. Outputs

| Output | Description |
|--------|-------------|
| `dashboard/NHIS_OOP_Ghana_Dashboard.html` | Interactive spatial dashboard — choropleth, LISA, lollipop, OOP trend, SHAP |
| `poster/NHIS_OOP_Ghana_Poster.html` | A0 conference poster, print-ready |
| `scripts/analysis_pipeline.py` | End-to-end Python analytical pipeline |
| `analysis.R` | Spatial diagnostics — spdep/spatialreg |

## 8a. Downloadable Artefacts (HTML)

| Artefact | View on GitHub | Live preview | Direct download (raw HTML) |
|----------|---------------|--------------|---------------------------|
| Interactive dashboard | [View](https://github.com/valentineghanem-bit/ghana-health-insurance-analysis/blob/main/dashboard/NHIS_OOP_Ghana_Dashboard.html) | [Preview](https://htmlpreview.github.io/?https://github.com/valentineghanem-bit/ghana-health-insurance-analysis/blob/main/dashboard/NHIS_OOP_Ghana_Dashboard.html) | [Download](https://raw.githubusercontent.com/valentineghanem-bit/ghana-health-insurance-analysis/main/dashboard/NHIS_OOP_Ghana_Dashboard.html) |
| Conference poster | [View](https://github.com/valentineghanem-bit/ghana-health-insurance-analysis/blob/main/poster/NHIS_OOP_Ghana_Poster.html) | [Preview](https://htmlpreview.github.io/?https://github.com/valentineghanem-bit/ghana-health-insurance-analysis/blob/main/poster/NHIS_OOP_Ghana_Poster.html) | [Download](https://raw.githubusercontent.com/valentineghanem-bit/ghana-health-insurance-analysis/main/poster/NHIS_OOP_Ghana_Poster.html) |

> **Tip:** The dashboard works fully offline once downloaded. The poster is print-ready at A0 (841 × 1189 mm).

## 9. Reporting Standard

This study follows the **STROBE** reporting guideline for observational ecological studies. Machine learning components follow **TRIPOD+AI**; spatial statistical components follow **RECORD-Spatial**.

## 10. Ethical Statement

All data are publicly available secondary administrative and census sources. No individual-level data were collected or processed. All analyses operate at district-level aggregates. Standard institutional research ethics principles for secondary data analysis apply.

## 11. Citation

**APA:**
Ghanem, V. G. (2026). *NHIS Uninsurance & Health Equity — Ghana 261 Districts.* GitHub. https://github.com/valentineghanem-bit/ghana-health-insurance-analysis

**BibTeX:**
```bibtex
@misc{ghanem2026nhis,
  author = {Ghanem, Valentine Golden},
  title  = {NHIS Uninsurance \& Health Equity --- Ghana 261 Districts},
  year   = {2026},
  url    = {https://github.com/valentineghanem-bit/ghana-health-insurance-analysis}
}
```

A machine-readable citation is provided in `CITATION.cff`.

## 12. License

Code is released under the **MIT License** — see [LICENSE](LICENSE) for details.
Outputs and figures: **CC BY 4.0**.

## 13. Author & Contact

**Valentine Golden Ghanem**
Ghana COCOBOD Cocoa Clinic, Accra, Ghana
Email: valentineghanem@gmail.com
ORCID: [0009-0002-8332-0220](https://orcid.org/0009-0002-8332-0220)

## 14. Acknowledgements

The author thanks the Ghana Statistical Service (GSS), National Health Insurance Authority (NHIA), and Ghana Health Service (GHS) for making district-level administrative data publicly available. This work is conducted in the public health research interest and does not represent the official position of any affiliated institution.
