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

NAVY = colors.HexColor("#14375E")
ACCENT = colors.HexColor("#2E75B6")
LIGHT = colors.HexColor("#EAF1F8")
GREY = colors.HexColor("#5A6672")
RULE = colors.HexColor("#C6D3E2")

PAGE_W, PAGE_H = A4
MARGIN = 2 * cm
CONTENT_W = PAGE_W - 2 * MARGIN

_base = getSampleStyleSheet()
S = {
    "body": ParagraphStyle(
        "body",
        parent=_base["Normal"],
        fontName="Times-Roman",
        fontSize=11,
        leading=15.5,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    ),
    "h1": ParagraphStyle(
        "h1",
        parent=_base["Heading1"],
        fontName="Times-Bold",
        fontSize=14,
        leading=18,
        textColor=NAVY,
        spaceBefore=10,
        spaceAfter=8,
    ),
    "h2": ParagraphStyle(
        "h2",
        parent=_base["Heading2"],
        fontName="Times-Bold",
        fontSize=12,
        leading=16,
        textColor=NAVY,
        spaceBefore=10,
        spaceAfter=6,
    ),
    "h3": ParagraphStyle(
        "h3",
        parent=_base["Heading3"],
        fontName="Times-Bold",
        fontSize=11,
        leading=15,
        textColor=ACCENT,
        spaceBefore=8,
        spaceAfter=4,
    ),
    "center": ParagraphStyle(
        "center",
        parent=_base["Normal"],
        alignment=TA_CENTER,
        fontName="Times-Roman",
        fontSize=11,
        leading=16,
    ),
    "abstract": ParagraphStyle(
        "abstract",
        parent=_base["Normal"],
        fontName="Times-Roman",
        fontSize=10.5,
        leading=15,
        alignment=TA_JUSTIFY,
        leftIndent=0.6 * cm,
        rightIndent=0.6 * cm,
        spaceAfter=8,
    ),
    "caption": ParagraphStyle(
        "caption",
        parent=_base["Normal"],
        fontName="Times-Italic",
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=GREY,
        spaceBefore=3,
        spaceAfter=10,
    ),
    "ref": ParagraphStyle(
        "ref",
        parent=_base["Normal"],
        fontName="Times-Roman",
        fontSize=10,
        leading=14,
        alignment=TA_LEFT,
        leftIndent=1.1 * cm,
        firstLineIndent=-1.1 * cm,
        spaceAfter=5,
    ),
    "cell": ParagraphStyle(
        "cell",
        parent=_base["Normal"],
        fontName="Times-Roman",
        fontSize=8.5,
        leading=11.5,
    ),
    "cellb": ParagraphStyle(
        "cellb",
        parent=_base["Normal"],
        fontName="Times-Bold",
        fontSize=8.5,
        leading=11.5,
        textColor=colors.white,
    ),
    "toc": ParagraphStyle(
        "toc",
        parent=_base["Normal"],
        fontName="Times-Roman",
        fontSize=11,
        leading=18,
        leftIndent=0.3 * cm,
    ),
}
