"""
Kush Ahuja — Blockchain Policy case study
=========================================

Builds the cover (SGT practical-file style) and a full undergraduate
case study: *Blockchain and the Cost of Regulatory Compliance*.

Run
---
    python3 generate_case_study.py
"""

from __future__ import annotations

import io
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
OUT_PDF = ROOT / "Blockchain_and_the_Cost_of_Regulatory_Compliance.pdf"
LOGO_PATH = REPO / "assets" / "sgt-logo.png"

STUDENT = {
    "name": "Kush Ahuja",
    "roll": "241302122",
    "programme": "B.Tech CSE (AI/ML)",
    "section": "Section - C",
    "department": "Department of CSE",
    "school": "School of Engineering and Technology",
    "university": "SGT University",
    "semester": "5th Semester",
    "faculty": "Ms. Bisma",
    "faculty_title": "Faculty",
    "faculty_dept": "CSE / SOET",
}

TOPIC = "Blockchain and the Cost of Regulatory Compliance"
FOOTER = f"Blockchain Policy · {STUDENT['name']} · {STUDENT['roll']}"
