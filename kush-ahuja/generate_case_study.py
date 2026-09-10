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
FOOTER = f"Blockchain Policy \u00b7 {STUDENT['name']} \u00b7 {STUDENT['roll']}"

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


class Report(BaseDocTemplate):
    def __init__(self, buffer: io.BytesIO, footer: str, *, cover_first: bool = False, **kw):
        self.footer_text = footer
        super().__init__(
            buffer,
            pagesize=A4,
            leftMargin=MARGIN,
            rightMargin=MARGIN,
            topMargin=MARGIN,
            bottomMargin=MARGIN + 0.4 * cm,
            title=TOPIC,
            author=STUDENT["name"],
            **kw,
        )
        frame = Frame(
            MARGIN,
            MARGIN + 0.4 * cm,
            CONTENT_W,
            PAGE_H - 2 * MARGIN - 0.4 * cm,
            id="main",
        )
        content = PageTemplate(id="content", frames=[frame], onPage=self._footer)
        if cover_first:
            self.addPageTemplates([PageTemplate(id="plain", frames=[frame]), content])
        else:
            self.addPageTemplates([content])

    def _footer(self, canv, doc):
        canv.saveState()
        canv.setStrokeColor(RULE)
        canv.line(MARGIN, MARGIN + 0.15 * cm, PAGE_W - MARGIN, MARGIN + 0.15 * cm)
        canv.setFont("Times-Roman", 8)
        canv.setFillColor(GREY)
        canv.drawString(MARGIN, MARGIN - 0.15 * cm, self.footer_text)
        canv.drawRightString(PAGE_W - MARGIN, MARGIN - 0.15 * cm, str(canv.getPageNumber()))
        canv.restoreState()


def para(text: str) -> Paragraph:
    return Paragraph(text, S["body"])


def heading(text: str) -> Paragraph:
    return Paragraph(text, S["h1"])


def sub(text: str) -> Paragraph:
    return Paragraph(text, S["h2"])


def bullets(items: list[str]) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(item, S["body"]), leftIndent=12) for item in items],
        bulletType="bullet",
        start="\u2022",
        leftIndent=18,
        bulletFontName="Times-Roman",
        bulletFontSize=11,
        spaceBefore=2,
        spaceAfter=6,
    )


def navy_table(rows: list[list[str]], col_widths=None, pad: int = 5):
    data = []
    for r, row in enumerate(rows):
        style = S["cellb"] if r == 0 else S["cell"]
        data.append([Paragraph(str(c), style) for c in row])
    t = Table(data, colWidths=col_widths, hAlign="CENTER", repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), pad),
                ("RIGHTPADDING", (0, 0), (-1, -1), pad),
                ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE),
                ("LINEBELOW", (0, -1), (-1, -1), 0.8, NAVY),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
            ]
        )
    )
    return t


def practical_cover() -> list:
    st: list = []
    st.append(Spacer(1, 0.35 * cm))
    st.append(Paragraph("Practical File / Case Study", S["center"]))
    st.append(Paragraph("On", S["center"]))
    st.append(Spacer(1, 0.2 * cm))
    st.append(
        Paragraph(
            '<font size="16" color="#14375E"><b>BLOCKCHAIN POLICY</b></font>',
            S["center"],
        )
    )
    st.append(Spacer(1, 0.35 * cm))
    st.append(
        Paragraph(
            f'<font size="12" color="#2E75B6"><b>{TOPIC}</b></font>',
            S["center"],
        )
    )
    st.append(Spacer(1, 0.7 * cm))
    st.append(
        Paragraph(
            "Submitted in partial fulfilment of the requirements for<br/>"
            "the award of the degree",
            S["center"],
        )
    )
    st.append(Spacer(1, 0.35 * cm))
    st.append(Paragraph("<b>Bachelor of Technology</b>", S["center"]))
    st.append(Paragraph("in", S["center"]))
    st.append(
        Paragraph(
            "<b>Department of Computer Science and Engineering</b>",
            S["center"],
        )
    )
    st.append(Spacer(1, 0.85 * cm))
    if LOGO_PATH.exists():
        logo_h = 4.6 * cm
        logo_w = logo_h * (595 / 700)
        logo = Image(str(LOGO_PATH), width=logo_w, height=logo_h)
        logo.hAlign = "CENTER"
        st.append(logo)
    else:
        st.append(Paragraph("<i>[SGT logo — add assets/sgt-logo.png]</i>", S["center"]))
    st.append(Spacer(1, 1.0 * cm))
    submitted = Table(
        [
            [
                Paragraph("<b>Submitted to:</b>", S["cell"]),
                Paragraph("<b>Submitted by:</b>", S["cell"]),
            ],
            [
                Paragraph(STUDENT["faculty"], S["cell"]),
                Paragraph(STUDENT["name"], S["cell"]),
            ],
            [
                Paragraph(STUDENT["faculty_title"], S["cell"]),
                Paragraph(STUDENT["roll"], S["cell"]),
            ],
            [
                Paragraph(STUDENT["faculty_dept"], S["cell"]),
                Paragraph(STUDENT["programme"], S["cell"]),
            ],
            [Paragraph("", S["cell"]), Paragraph(STUDENT["section"], S["cell"])],
            [Paragraph("", S["cell"]), Paragraph(STUDENT["semester"], S["cell"])],
        ],
        colWidths=[CONTENT_W * 0.48, CONTENT_W * 0.48],
        hAlign="LEFT",
    )
    st.append(submitted)
    st.append(Spacer(1, 1.4 * cm))
    st.append(Paragraph(STUDENT["school"], S["center"]))
    st.append(Paragraph(STUDENT["department"], S["center"]))
    st.append(Paragraph(f"<b>{STUDENT['university']}</b>", S["center"]))
    st.append(NextPageTemplate("content"))
    st.append(PageBreak())
    return st


def contents_page() -> list:
    items = [
        "Abstract",
        "1. Introduction",
        "2. Background: What \u201cCompliance\u201d Means on a Public Ledger",
        "3. Anatomy of Compliance Cost",
        "4. Real-World Cases and Jurisdictions",
        "5. Who Pays, Who Exits, and What Distorts",
        "6. Policy Discussion",
        "7. Recommendations",
        "8. Conclusion",
        "References",
    ]
    st = [
        Paragraph('<font size="16" color="#14375E"><b>CONTENTS</b></font>', S["center"]),
        Spacer(1, 0.6 * cm),
    ]
    for item in items:
        st.append(Paragraph(item, S["toc"]))
    st.append(PageBreak())
    return st
