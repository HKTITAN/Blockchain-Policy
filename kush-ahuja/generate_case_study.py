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
        start="•",
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
        "2. Background: What “Compliance” Means on a Public Ledger",
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


def body() -> list:
    st: list = []

    st.append(Paragraph('<font size="16" color="#14375E"><b>ABSTRACT</b></font>', S["center"]))
    st.append(Spacer(1, 0.35 * cm))
    st.append(
        Paragraph(
            "Public blockchains were designed to lower the cost of transferring value "
            "without a trusted intermediary. The firms that sit around those chains — "
            "exchanges, custodians, on-ramps, stablecoin issuers, and increasingly "
            "some DeFi front-ends — now spend a large and growing share of their "
            "budget on something the white papers omitted: regulatory compliance. "
            "Know-your-customer checks, anti-money-laundering monitoring, the FATF "
            "Travel Rule, tax withholding, licensing across dozens of countries, "
            "sanctions screening, and consumer-disclosure duties are not optional "
            "overhead for any business that touches the rupee, the dollar, or the "
            "euro. They are the price of remaining in the formal financial system. "
            "This case study asks a narrower question than “should crypto be "
            "regulated?” It asks what compliance <i>costs</i>, who pays those costs, "
            "and how the structure of the bill changes market structure. Evidence "
            "from Coinbase’s public filings, Binance’s settlements, the European "
            "Union’s Markets in Crypto-Assets regime, United States enforcement, "
            "and India’s virtual-digital-asset tax-and-TDS design shows a consistent "
            "pattern. Fixed compliance costs favour incumbents. Ambiguous rules "
            "create a risk premium that is larger than the cash cost of a licence. "
            "Rules written for banks fit custodial exchanges better than "
            "non-custodial software, so the industry either centralises to become "
            "legible or exits to friendlier jurisdictions. The policy implication "
            "for India is not zero regulation and not a copy-paste of banking law "
            "onto every wallet. It is proportionate, activity-based rules whose "
            "compliance cost is knowable in advance — because an unknowable cost is "
            "itself a barrier to lawful business.",
            S["abstract"],
        )
    )
    st.append(
        Paragraph(
            "<b>Keywords:</b> regulatory compliance; VASP; FATF Travel Rule; MiCA; "
            "KYC/AML; virtual digital assets; TDS; compliance cost; India.",
            S["abstract"],
        )
    )

    st.append(heading("1. Introduction"))
    st.append(
        para(
            "A blockchain transaction is cheap at the margin if the network is not "
            "congested: a signature, a fee, a few minutes of confirmation. A "
            "<i>compliant</i> rupee-to-token conversion is not cheap. Before that "
            "signature exists, a licensed platform has identified the customer, "
            "screened the name against sanctions lists, assigned a risk score, "
            "recorded the purpose of the transfer, reserved capital against "
            "operational loss, withheld tax where the statute requires it, and "
            "prepared to send originator and beneficiary information to the next "
            "virtual-asset service provider (VASP) under the Travel Rule. Each of "
            "those steps is staff, software, law-firm hours, and residual legal "
            "risk. The chain did not impose them. The state did — for reasons that "
            "are often good. This paper treats those reasons as given and studies "
            "the bill."
        )
    )
    st.append(
        para(
            "Compliance cost is an old topic in banking. What is new is the collision "
            "between a technology that was meant to be jurisdiction-agnostic and a "
            "regulatory project that is irreducibly territorial. Bitcoin does not "
            "know whether a spender is in Gurugram or Lisbon. MiCA, the U.S. "
            "Bank Secrecy Act, and India’s Income-tax Act do. Anyone who wants to "
            "connect a public ledger to a bank account must therefore buy a "
            "translation layer: licences, identity vendors, transaction-monitoring "
            "engines, and people who can explain a suspicious-transaction report to "
            "the Financial Intelligence Unit. That translation layer is now a "
            "primary cost centre of the industry, and in some years a larger "
            "strategic constraint than block-space fees."
        )
    )
    st.append(
        para(
            "The undergraduate temptation is to pick a side — “regulation is "
            "innovation-killing” versus “anything less than bank rules is a loophole.” "
            "Both slogans hide the engineering-and-economics problem. Some rules "
            "are high-fixed-cost and low-variable-cost (building a Travel Rule "
            "messaging stack). Some are high-variable-cost (manual review of every "
            "withdrawal above a threshold). Some are not cash costs at all but "
            "option-value costs: a firm delays a product because it cannot get a "
            "no-action letter. India’s present mix — heavy taxation without a "
            "comprehensive licensing statute — is a distinctive case of the third "
            "kind. Platforms pay 1 percent TDS and customers face a 30 percent tax "
            "on gains, while the Reserve Bank’s discomfort with bank–crypto rails "
            "and the absence of a dedicated VASP law leave lawful operators unsure "
            "which additional shoe will drop."
        )
    )
    st.append(
        para(
            "Section 2 defines compliance in this setting and why public ledgers "
            "make some classic tools awkward. Section 3 decomposes cost into "
            "licence, identity, monitoring, tax, cross-border, and ambiguity. "
            "Section 4 reads real cases: a listed U.S. exchange, a global platform "
            "that settled with the Department of Justice, Europe’s attempt to "
            "harmonise the bill, and India’s tax-first path. Section 5 asks who "
            "pays and how costs reshape competition. Section 6 discusses policy "
            "design: activity-based rules, mutual recognition, and the special "
            "problem of non-custodial software. Section 7 recommends a compliance "
            "architecture India could actually implement. Section 8 concludes."
        )
    )

    st.append(heading("2. Background: What “Compliance” Means on a Public Ledger"))
    st.append(sub("2.1 From bank secrecy to VASPs"))
    st.append(
        para(
            "Modern AML law grew out of cash-intensive crime and, after 2001, "
            "terrorist-finance concerns. Banks became deputies: they identify "
            "customers, monitor transactions, and report suspicion. The Financial "
            "Action Task Force exported that model worldwide. When virtual assets "
            "became large enough to matter, FATF Recommendation 15 extended the "
            "same duties to VASPs — exchanges, transfer services, custodians, and "
            "some issuers. The Travel Rule, originally a wire-transfer obligation, "
            "was interpreted to require VASPs to pass originator and beneficiary "
            "information with qualifying transfers. That single sentence creates a "
            "technical problem the SWIFT network already solved for banks and that "
            "public blockchains did not: there is no native field on a Bitcoin "
            "transaction for a legal name and address."
        )
    )
    st.append(
        para(
            "Compliance in this paper therefore means the bundle of legal duties "
            "that a business accepts in exchange for access to the formal payment "
            "system and to a mass retail market. It is not the same as on-chain "
            "“transparency.” Anyone can see a Bitcoin address. Almost no one can "
            "see the person. The expensive part is connecting those two facts "
            "lawfully, storing the connection for years, and being ready to produce "
            "it to FIU-IND or a foreign counterpart without leaking it to everyone "
            "else. Data-protection law (in Europe, GDPR; in India, the Digital "
            "Personal Data Protection Act, 2023) then adds a second constraint: "
            "collect enough identity to satisfy AML, but not so much, and not for "
            "so long, that you violate privacy statute. The intersection is where "
            "lawyers earn their fees."
        )
    )
    st.append(sub("2.2 Why the technology fights the form"))
    st.append(
        para(
            "Three properties of public ledgers raise compliance cost relative to "
            "a closed bank ledger. First, <b>permissionless entry</b>: a new "
            "counterparty address can appear without a prior legal relationship. "
            "Banks are used to a finite set of correspondent institutions. VASPs "
            "must decide, in software, whether the other side is a regulated "
            "exchange, an unhosted wallet, or a sanctioned protocol. Second, "
            "<b>finality</b>: a mistaken or illicit transfer is hard to reverse, "
            "so monitoring must happen <i>before</i> broadcast, not after a "
            "chargeback window. Third, <b>composability</b>: a user can route "
            "value through a decentralised exchange, a mixer, a bridge, and a "
            "centralised off-ramp in one afternoon. Each hop is a monitoring "
            "problem. Vendors sell “blockchain analytics” precisely because the "
            "native data model is addresses, not customers."
        )
    )
    st.append(
        para(
            "None of this makes compliance impossible. It makes it an industry. "
            "Chainalysis, TRM Labs, Elliptic, and Sumsub are not footnotes; they "
            "are the outsourced compliance department of firms that cannot build "
            "graph analytics or liveness detection in-house. When a case study "
            "talks about the cost of regulation, a large fraction of that cost is "
            "rent paid to this vendor layer. That is not a criticism of the "
            "vendors. It is a description of how legal duties become line items."
        )
    )
    st.append(sub("2.3 Two markets, two bills"))
    st.append(
        para(
            "It helps to split the industry. <b>Custodial platforms</b> look like "
            "financial institutions: they hold keys, they have bank accounts, they "
            "can be licensed, examined, and fined. Their compliance bill is high "
            "but conceptually familiar. <b>Non-custodial software</b> — a wallet "
            "that never holds the user’s key, a smart-contract protocol with no "
            "company at the centre — does not fit the VASP form without legal "
            "creativity. Some jurisdictions treat a front-end operator or a DAO "
            "foundation as the obligated party. Some do not. The uncertainty is "
            "itself a cost: teams spend money arguing about whether they are a "
            "VASP before they spend money acting like one. Policy that pretends "
            "this split does not exist will either exempt too much (and look "
            "asleep) or capture too much (and push development offshore)."
        )
    )

    st.append(heading("3. Anatomy of Compliance Cost"))
    st.append(
        para(
            "A useful decomposition for an engineering audience is to treat "
            "compliance as a system with fixed costs, variable costs, and a "
            "residual risk term. Table 1 is schematic, not an audited cost model. "
            "Public companies disclose enough to show the orders of magnitude; "
            "private startups do not."
        )
    )
    st.append(
        navy_table(
            [
                ["Cost bucket", "Mostly fixed or variable?", "What buys it", "Who feels it first"],
                [
                    "Licensing and legal",
                    "Fixed, then per-jurisdiction",
                    "Applications, local counsel, capital",
                    "Startups trying to launch in 5 countries",
                ],
                [
                    "KYC / identity",
                    "Variable per user",
                    "Vendor APIs, manual review, liveness",
                    "Retail on-ramps",
                ],
                [
                    "AML monitoring &amp; Travel Rule",
                    "Fixed stack + per-transfer",
                    "Analytics, messaging networks, SAR staff",
                    "Exchanges and custodians",
                ],
                [
                    "Tax withholding / reporting",
                    "Variable + systems",
                    "TDS engines, 1099/equivalent, support",
                    "Indian platforms; U.S. brokers",
                ],
                [
                    "Sanctions / geo-blocking",
                    "Fixed rules + alerts",
                    "List screening, VPN detection",
                    "Global platforms",
                ],
                [
                    "Ambiguity / enforcement risk",
                    "Risk premium",
                    "Reserves, delayed products, settlements",
                    "Anyone without a clear licence path",
                ],
            ],
            col_widths=[CONTENT_W * 0.22, CONTENT_W * 0.22, CONTENT_W * 0.28, CONTENT_W * 0.28],
        )
    )
    st.append(
        Paragraph(
            "Table 1. A working breakdown of compliance cost around public-ledger businesses.",
            S["caption"],
        )
    )

    st.append(sub("3.1 Licensing as a barrier, not a stamp"))
    st.append(
        para(
            "A licence is often described as a certificate. Economically it is a "
            "sunk-cost tournament. An applicant pays lawyers to map every entity, "
            "writes policies that will be obsolete in eighteen months, posts "
            "capital, waits, answers a second round of questions, and in some "
            "countries discovers that the statute the application assumed has "
            "changed. MiCA at least publishes a single rulebook for the Union, "
            "which is why European counsel can quote a price. A firm that wants "
            "to serve India, the UAE, Singapore, and the United States is buying "
            "four interpretations of “the same” activity. Each interpretation "
            "needs a local responsible officer. Those officers do not scale like "
            "cloud compute. They scale like humans."
        )
    )
    st.append(sub("3.2 Identity: the per-user tax"))
    st.append(
        para(
            "KYC looks cheap on a slide — “a few rupees per PAN-Aadhaar match.” "
            "The fully loaded cost includes failed liveness checks, address "
            "documents that do not match, politically exposed person review, "
            "and the support tickets generated by honest people who dyed their "
            "hair or changed phones. Conversion drops when friction rises. "
            "Marketing then spends more to replace the users that compliance "
            "filtered or fatigued. A serious cost model therefore includes "
            "<i>lost gross merchandise</i>, not only vendor invoices. This is "
            "why platforms fight over thresholds and over whether a low-value "
            "account can be opened with lighter identification. FATF’s "
            "risk-based approach allows that conversation. Political pressure "
            "after a scandal usually ends it."
        )
    )
    st.append(sub("3.3 Monitoring and the Travel Rule"))
    st.append(
        para(
            "Transaction monitoring on a blockchain is both easier and harder "
            "than on a bank core. Easier: the history is public, so a vendor "
            "can score an address for mixer exposure before the withdrawal is "
            "signed. Harder: the customer can empty the account to an unhosted "
            "wallet the platform does not control, and the next hop is invisible "
            "to the platform’s ledger even though it is visible on-chain. The "
            "Travel Rule then requires VASPs to transmit identity data they "
            "never needed for settlement. Competing messaging protocols "
            "(TRISA, OpenVASP, and vendor-specific networks) recreate, badly, "
            "what SWIFT already is. Until one standard wins, every integration "
            "is a bilateral project. That is a textbook network-cost problem "
            "created by law, not by cryptography."
        )
    )
    st.append(sub("3.4 Tax administration as compliance"))
    st.append(
        para(
            "India’s Finance Act, 2022 inserted a special regime for virtual "
            "digital assets: a 30 percent tax on transfers under section 115BBH, "
            "without set-off of losses against other income in the ordinary way, "
            "and a 1 percent TDS under section 194S on many transfers above a "
            "threshold. Whatever one thinks of the rates, the <i>compliance</i> "
            "consequence is concrete. Indian exchanges had to build withholding "
            "engines, reconcile on-chain transfers with off-chain books, and "
            "explain to users why a sale produced both a tax event and a "
            "deduction from proceeds. Some peer-to-peer and offshore activity "
            "moved out of the reporting perimeter — a standard behavioural "
            "response to a high, visible tax at source. The state collected "
            "some TDS and lost some visibility. That trade-off is the cost of "
            "a tax-first policy in a market that can relocate in a browser tab."
        )
    )
    st.append(sub("3.5 The price of not knowing"))
    st.append(
        para(
            "Ambiguity is the residual term in Table 1 and often the largest. "
            "A firm that cannot tell whether its token is a security, whether "
            "its staking product is a deposit, or whether its Indian bank will "
            "be told tomorrow to close the account will hold extra cash, delay "
            "hiring, and price a legal catastrophe into every board meeting. "
            "Settlements in the United States — sometimes in the billions of "
            "dollars — teach global boards that the downside is existential. "
            "Even firms that never enter the U.S. market pay a version of this "
            "premium because dollar rails and cloud vendors still feel U.S. "
            "law. Compliance cost is therefore not only what you spend to obey "
            "a known rule. It is what you spend because the rule might be "
            "applied to you after the product ships."
        )
    )

    st.append(heading("4. Real-World Cases and Jurisdictions"))
    st.append(sub("4.1 A listed exchange: compliance as a line item you can see"))
    st.append(
        para(
            "Coinbase Global, as a U.S. public company, is useful because it "
            "must describe risk and spending in filings. Year after year the "
            "10-K language is blunt: the firm operates in a shifting legal "
            "environment; it spends heavily on compliance, legal, and "
            "policy; a change in a single state’s money-transmitter reading "
            "or a federal classification of an asset can strand a product. "
            "Headcount in legal, compliance, and institutional coverage is "
            "not a rounding error next to engineering. That is the point. "
            "Once a platform decides to be a full-stack, bank-adjacent "
            "business, its cost structure starts to resemble a bank’s. "
            "Critics call this capture. Supporters call it growing up. For "
            "this paper it is simply evidence that compliance, at scale, is "
            "an operating system — not a weekend policy PDF."
        )
    )
    st.append(
        para(
            "The competitive implication is immediate. A well-capitalised "
            "listed firm can amortise a global licence map and a 24-hour "
            "financial-crime operations centre. A ten-person Indian startup "
            "that wants to list a new token and offer INR pairs cannot. If "
            "the policy goal is “only serious firms should touch retail "
            "money,” high fixed costs are a feature. If the goal is “let a "
            "domestic industry form under supervision,” the same costs are "
            "a bug. India has not clearly chosen which goal it wants, which "
            "is why the next subsection matters."
        )
    )

    st.append(sub("4.2 Binance and the price of being everywhere without a map"))
    st.append(
        para(
            "Binance’s 2023 resolution with the U.S. Department of Justice "
            "and related agencies — a criminal plea, a multi-billion-dollar "
            "financial penalty, and the departure of its founder from the "
            "CEO role — is the most expensive compliance case study in the "
            "sector. The government’s theory was not that the blockchain "
            "was illegal. It was that a business which served U.S. customers "
            "and dollar infrastructure, while treating compliance as a "
            "growth constraint to be gamed, had violated BSA-type duties "
            "and sanctions expectations. One may debate charging theories. "
            "One cannot debate the lesson boards took: extra-territorial "
            "enforcement can bankrupt a strategy of “launch first, pick a "
            "headquarters later.”"
        )
    )
    st.append(
        para(
            "After such cases, remaining global platforms raise the quality "
            "(and cost) of geofencing, KYC, and government-relations staff. "
            "Some shrink their country list. Users in excluded countries do "
            "not stop trading; they move to platforms with weaker controls "
            "or to peer-to-peer rails. Compliance cost, pushed high enough "
            "in the formal sector, reallocates volume to the informal "
            "sector. A ministry that only measures licensed-entity reports "
            "will then congratulate itself on cleanliness while the risk "
            "migrates. That is a standard result in AML research, not a "
            "crypto special case."
        )
    )

    st.append(sub("4.3 Europe: paying for a single rulebook (MiCA)"))
    st.append(
        para(
            "MiCA (Regulation (EU) 2023/1114) is the most ambitious attempt "
            "to make the compliance bill predictable. It creates categories "
            "for asset-referenced tokens, e-money tokens, and crypto-asset "
            "service providers; it requires white papers, governance, "
            "complaints handling, and, for some issuers, prudential "
            "safeguards. Passporting inside the Union is the reward for "
            "paying the fixed cost once. For an Indian student the "
            "interesting feature is not the recitals. It is the economic "
            "bet: better to impose a large, known cost than a small, "
            "unknown one. Early evidence is mixed in the way all licensing "
            "regimes are mixed. Some firms left the Union or narrowed "
            "products. Some treated a MiCA licence as a quality signal and "
            "a ticket to bank partnerships. Compliance cost became a "
            "competitive language — “we are MiCA-ready” — which is exactly "
            "what a high-fixed-cost regime produces."
        )
    )
    st.append(
        para(
            "MiCA is also honest about what it does not cover. Decentralised "
            "protocols without an issuer or service provider sit awkwardly "
            "at the edge. Europe did not solve the non-custodial problem; "
            "it postponed the hardest classification fights. That "
            "postponement is itself a policy choice, and it is more "
            "transparent than pretending a DAO is already a bank."
        )
    )

    st.append(sub("4.4 India: tax first, licence later"))
    st.append(
        para(
            "India’s distinctive path is to tax virtual digital assets "
            "sharply while leaving a comprehensive market-conduct and "
            "custody statute unfinished. The Reserve Bank has warned banks "
            "and the public about crypto risk for years and has explored a "
            "central bank digital currency as a public alternative. SEBI’s "
            "perimeter covers securities; many tokens are not clearly "
            "securities. Home-ministry and CERT-In instruments address "
            "fraud and incident reporting. FIU-IND has registered some "
            "offshore platforms as reporting entities after litigation and "
            "negotiation — a reminder that enforcement can create de facto "
            "compliance duties even without a dedicated Act."
        )
    )
    st.append(
        para(
            "For an Indian exchange the resulting cost stack is peculiar. "
            "The tax engine is mandatory and live. Banking access is "
            "politically fragile. Advertising is constrained. Users can "
            "still open accounts at offshore platforms that do not withhold "
            "1 percent TDS. Domestic compliance cost is therefore incurred "
            "in a market that can leak. Several Indian platforms shrank, "
            "pivoted to education, or emphasised foreign users. That "
            "outcome can be defended if the social goal was to cool "
            "speculation. It cannot be defended if the social goal was to "
            "build a supervised domestic industry. Compliance cost without "
            "a licence path is not supervision. It is a toll on whoever is "
            "too visible to dodge it."
        )
    )

    st.append(sub("4.5 Tornado Cash and the cost of protocol-level enforcement"))
    st.append(
        para(
            "The U.S. sanctions action against Tornado Cash (2022) and the "
            "subsequent litigation and partial unwind showed a different "
            "cost: developers, front-end operators, and even some users of "
            "privacy-preserving smart contracts faced criminal and civil "
            "risk for code that, once deployed, no single firm fully "
            "controlled. Whatever one’s view of mixers, the compliance "
            "lesson is that when intermediaries are the only easy target, "
            "enforcement will stretch the definition of intermediary. "
            "Legal teams now budget for “are we a publisher of software or "
            "a transfer service?” The hours spent on that question are "
            "compliance costs. They do not show up as KYC vendor invoices. "
            "They show up as products that are never shipped in the United "
            "States or India."
        )
    )

    st.append(
        navy_table(
            [
                ["Case / regime", "What was expensive", "Intended public benefit", "Side effect"],
                [
                    "Listed U.S. exchange",
                    "Standing legal/compliance org",
                    "Investor and customer protection",
                    "Incumbent advantage",
                ],
                [
                    "Binance settlement",
                    "Penalties + rebuilding controls",
                    "AML and sanctions integrity",
                    "Volume leakage to weaker venues",
                ],
                [
                    "MiCA",
                    "Licence + white paper + capital",
                    "Passport and predictability",
                    "Exit by smaller issuers",
                ],
                [
                    "India VDA tax / TDS",
                    "Withholding systems + 30% rate",
                    "Revenue and cooling speculation",
                    "Offshore and P2P leakage",
                ],
                [
                    "Tornado-type actions",
                    "Legal classification risk",
                    "Sanctions effectiveness",
                    "Chill on non-custodial tooling",
                ],
            ],
            col_widths=[CONTENT_W * 0.20, CONTENT_W * 0.26, CONTENT_W * 0.27, CONTENT_W * 0.27],
        )
    )
    st.append(
        Paragraph(
            "Table 2. Compliance spend is never only a private cost; it reallocates activity.",
            S["caption"],
        )
    )

    st.append(heading("5. Who Pays, Who Exits, and What Distorts"))
    st.append(sub("5.1 Incidence: users, not compliance officers"))
    st.append(
        para(
            "Economics 101 still applies. A per-user KYC fee and a 1 percent "
            "TDS are paid by platforms in the first instance and by users "
            "after prices and spreads adjust. Withdrawal fees rise. Spreads "
            "widen. Small tickets become unprofitable and are discouraged "
            "in the UI. Retail users — the population consumer-protection "
            "law claims to help — face a worse deal or leave for informal "
            "channels that have <i>zero</i> consumer protection. High "
            "compliance cost can therefore reduce measured fraud on "
            "licensed platforms while increasing unmeasured fraud off them. "
            "A complete welfare analysis must count both."
        )
    )
    st.append(sub("5.2 Concentration"))
    st.append(
        para(
            "Fixed legal costs are a classic source of concentration. After "
            "MiCA, after U.S. enforcement waves, and after India’s tax "
            "shock, the surviving formal firms are larger, more "
            "bank-like, and more able to hire Delhi, Brussels, and "
            "Washington counsel. That may be acceptable. Payment systems "
            "are also concentrated. The intellectual error is to describe "
            "the resulting market as “what users chose” rather than “what "
            "the cost curve plus the statute produced.” If policymakers "
            "later complain that a handful of exchanges have too much "
            "systemic importance, they should remember who paid for the "
            "moat."
        )
    )
    st.append(sub("5.3 Innovation that becomes uncompliant by default"))
    st.append(
        para(
            "Some of the technically interesting work in the last five "
            "years — account abstraction, intent-based trading, "
            "cross-chain settlement, privacy-preserving identity — sits "
            "in the gap between “software library” and “transfer service.” "
            "If every new primitive is presumed a VASP until proven "
            "otherwise, research-to-product pipelines inside India will "
            "thin out. Talent will ship from Singapore or Lisbon under a "
            "clearer licence, or from nowhere in particular under a "
            "pseudonym. Compliance cost then becomes an industrial-policy "
            "instrument, whether or not Parliament intended that."
        )
    )
    st.append(sub("5.4 A note on “code is free”"))
    st.append(
        para(
            "Open-source protocol work is often said to have zero "
            "compliance cost because there is no company. That is true "
            "only until a foundation, a laboratory, or a front-end "
            "company takes a donation, pays a developer, or hosts a "
            "website that helps users enter transactions. The moment "
            "fiat or a legal entity appears, the cost function appears "
            "with it. Students who plan to “just launch a contract” "
            "should treat that sentence as the beginning of the "
            "compliance analysis, not the end."
        )
    )

    st.append(heading("6. Policy Discussion"))
    st.append(sub("6.1 Regulate activities, not adjectives"))
    st.append(
        para(
            "The cheapest compliance system to administer is one that "
            "asks what a person is <i>doing</i>: holding someone else’s "
            "keys, exchanging INR for a token, issuing a redeemable "
            "stablecoin, giving personalised investment advice. Those "
            "activities already have cousins in Indian law (custodian, "
            "payment intermediary, prepaid instrument, investment "
            "adviser). Copying the cousin is not always right — a "
            "stablecoin is not exactly a PPI — but it is more "
            "tractable than regulating “blockchain” or “Web3” as a "
            "mood. Activity-based rules also let non-custodial "
            "software remain software until the operator crosses a "
            "factual line (control of keys, pooling of customer value, "
            "solicitation of retail in India)."
        )
    )
    st.append(sub("6.2 Predictability is a cost-reduction tool"))
    st.append(
        para(
            "MiCA’s deepest exportable idea is not any particular "
            "article. It is the idea that a firm should be able to "
            "buy a calendar. Sandboxes help only if graduation criteria "
            "are real. No-action processes help only if they are "
            "published. India’s current mix — tax clarity plus "
            "licensing fog — maximises revenue administration and "
            "minimises business-model administration. A dedicated VASP "
            "chapter, even a strict one, would likely <i>lower</i> "
            "total compliance cost for honest firms because it would "
            "convert the ambiguity premium into a list of controls. "
            "Strict-and-clear beats vague-and-severe."
        )
    )
    st.append(sub("6.3 Proportionality and thresholds"))
    st.append(
        para(
            "FATF’s risk-based language is easy to quote and hard to "
            "implement. A platform with twenty users and a platform "
            "with twenty million should not buy the same monitoring "
            "stack on day one. Tiered duties — registration, then "
            "licence, then enhanced obligations above thresholds of "
            "volume or custody — keep the on-ramp to legality open. "
            "The political failure mode is that after the first "
            "scandal, tiers collapse to “everyone does everything.” "
            "The economic failure mode is that tiers become loopholes. "
            "The design job is to accept both risks and still write "
            "numbers: a custody threshold, a transfer threshold for "
            "Travel Rule, a deadline for SAR filing. Engineers can "
            "implement numbers. They cannot implement vibes."
        )
    )
    st.append(sub("6.4 Cross-border recognition"))
    st.append(
        para(
            "A large share of cost is duplicated KYC and duplicated "
            "licensing for the same customer who already passed a "
            "comparable check abroad. Mutual recognition or "
            "passporting is how the EU attacks that waste. India will "
            "not passport into MiCA tomorrow. It can still accept, for "
            "low-risk customers, KYC performed by a regulated Indian "
            "bank or by another FIU-registered VASP, instead of "
            "forcing a second selfie. Interoperable Travel Rule "
            "messaging — one Indian-standard gateway rather than five "
            "vendor lock-ins — is a public-good problem that MeitY or "
            "a self-regulatory organisation could host. Standards work "
            "is unglamorous and cheaper than twenty private integrations."
        )
    )
    st.append(sub("6.5 Do not make analytics a secret law"))
    st.append(
        para(
            "When platforms outsource “risk scores” to a handful of "
            "analytics firms, those firms’ heuristics become de facto "
            "regulation. An address clustered near a mixer may become "
            "unbankable without a hearing. Policy should require "
            "explainability to the customer and a redress path, the "
            "way credit scoring eventually had to grow up. Otherwise "
            "compliance cost includes an unaccountable exclusion "
            "machine — cheap for the platform, expensive for the "
            "wrongly flagged user, and invisible in official reports."
        )
    )
    st.append(sub("6.6 Taxation should not impersonate market conduct"))
    st.append(
        para(
            "A 30 percent tax and a 1 percent TDS can be defended as "
            "revenue measures. They should not be asked to do the work "
            "of a custody statute, an advertising code, or an AML "
            "rule. When tax is the only clear lever, platforms optimise "
            "for withholding mechanics rather than for operational "
            "resilience or consumer outcomes. Split the instruments. "
            "Let CBDT collect tax. Let a market supervisor write "
            "conduct rules. Let FIU-IND collect financial-intelligence "
            "reports. Each organisation will still impose costs. The "
            "costs will at least point at the right objective."
        )
    )

    st.append(heading("7. Recommendations"))
    st.append(sub("7.1 For the Union government and regulators"))
    st.append(
        bullets(
            [
                "<b>Enact an activity-based VASP law</b> that lists licensable "
                "acts (custody, exchange, fiat on-ramp, stablecoin issuance, "
                "portfolio management) and explicitly carves out unaffiliated "
                "non-custodial software until an operator takes control of "
                "customer value.",
                "<b>Publish a single Indian Travel Rule technical profile</b> "
                "(message fields, sunrise thresholds, unhosted-wallet "
                "treatment) so every exchange is not paying for a private "
                "standard war.",
                "<b>Tier duties by custody and volume</b> with numeric "
                "thresholds, a registration tier for small domestic firms, "
                "and a full licence for retail custody.",
                "<b>Stabilise bank access</b> for licensed entities through "
                "an RBI circular that states conditions rather than leaving "
                "every compliance officer to interpret newspaper interviews.",
                "<b>Keep tax policy and conduct policy in different "
                "instruments.</b> Review whether 194S TDS is driving "
                "reportable activity offshore; if yes, the provision is "
                "failing as intelligence infrastructure even if it raises "
                "some cash.",
                "<b>Require analytics vendors used by Indian VASPs</b> to "
                "offer a customer redress channel when a score blocks a "
                "lawful transfer.",
            ]
        )
    )
    st.append(sub("7.2 For platforms operating in or into India"))
    st.append(
        bullets(
            [
                "Budget compliance as a product surface: cooling-off, "
                "withdrawal allow-lists, and tax lots are user experience, "
                "not only Legal’s problem.",
                "Prefer reusable KYC (account-aggregator or bank-attested "
                "identity) over collecting a fresh document pile for every "
                "feature launch.",
                "Measure leakage: if TDS and friction push volume to "
                "unregulated peers, report that number to the board the "
                "way you report conversion. It is a policy risk metric.",
                "Do not advertise “decentralisation” as an AML exemption "
                "when a company still hosts the front-end, the sequencer, "
                "or the upgrade key.",
            ]
        )
    )
    st.append(sub("7.3 For this course and for student builders"))
    st.append(
        bullets(
            [
                "When proposing a dApp in a lab, add a one-page “who is "
                "the VASP?” memo. If the answer is “nobody,” explain who "
                "pays the server bill and who can pause the contract.",
                "Read one primary instrument end-to-end (MiCA Title, FATF "
                "Recommendation 15 guidance, or the Finance Act VDA "
                "clauses) instead of only news summaries. Compliance cost "
                "hides in definitions.",
                "Treat vendor lock-in (KYC, analytics, Travel Rule) as an "
                "architecture decision equal to choice of chain.",
            ]
        )
    )
    st.append(sub("7.4 What not to copy"))
    st.append(
        para(
            "Do not copy a full banking capital stack onto a non-custodial "
            "wallet. Do not copy a ban and then wonder why FIU reporting "
            "quality collapsed. Do not copy another country’s list of "
            "licensable tokens without copying its passporting and its "
            "appeals process — that is how you import costs without "
            "importing the efficiency that was supposed to justify them."
        )
    )

    st.append(heading("8. Conclusion"))
    st.append(
        para(
            "Blockchain lowers the cost of settlement among strangers. "
            "Regulation raises the cost of connecting that settlement to "
            "real-world identity, banks, and consumer protection. Both "
            "sentences can be true at once. The last decade shows that "
            "the second cost now dominates the business models that "
            "ordinary Indian users actually touch. Exchanges, not "
            "consensus algorithms, are where rupees meet tokens. Those "
            "exchanges buy licences, identity checks, analytics, tax "
            "engines, and legal insurance against a rule that has not "
            "been written yet."
        )
    )
    st.append(
        para(
            "The cost is not illegitimate. Money laundering, sanctions "
            "evasion, and retail fraud are real. The design error is to "
            "treat every instrument as free. High fixed costs concentrate "
            "the market. Ambiguous costs freeze it or push it offshore. "
            "Tax instruments that are asked to do the work of a licence "
            "collect some revenue and leak a lot of activity. Europe’s "
            "bet on a known bill, the United States’ bet on enforcement, "
            "and India’s bet on taxation plus caution are three different "
            "ways to spend the same political capital. Only the first "
            "makes the spend knowable to a compliance officer who has to "
            "ship software on a Tuesday."
        )
    )
    st.append(
        para(
            "For Blockchain Policy as a course, the operational moral is "
            "to read cost the way an engineer reads latency: measure it, "
            "attribute it, and refuse a design that adds latency without "
            "buying a property you can name. If a proposed Indian rule "
            "cannot say whether it is buying AML visibility, consumer "
            "redress, or monetary-sovereignty theatre, it will still "
            "impose a bill. Someone will pay it. This case study’s only "
            "insistence is that the someone, and the rupee amount, be "
            "part of the argument — not an afterthought once the adjective "
            "“crypto” has done all the work."
        )
    )

    st.append(heading("References"))
    refs = [
        "Bank for International Settlements. (various years). Papers on permissioned versus permissionless ledgers and the regulatory perimeter of crypto intermediaries.",
        "Coinbase Global, Inc. Annual Reports on Form 10-K (recent years). U.S. Securities and Exchange Commission EDGAR. (Used for qualitative evidence that legal and compliance are material cost centres.)",
        "European Union. (2023). Regulation (EU) 2023/1114 on markets in crypto-assets (MiCA). <i>Official Journal of the European Union</i>.",
        "FATF. (2019/2021). <i>Guidance for a risk-based approach to virtual assets and VASPs</i> (and updates). Financial Action Task Force.",
        "FATF. (2021). Interpretive note to Recommendation 16 (wire transfers / Travel Rule as applied to virtual assets).",
        "Financial Intelligence Unit — India. Registration and reporting expectations for VASPs / reporting entities dealing in virtual digital assets (as evolved through directions and court-adjacent processes).",
        "Government of India. (2022). Finance Act, 2022, inserting ss. 115BBH and 194S (virtual digital assets). Ministry of Finance / Central Board of Direct Taxes circulars on TDS.",
        "Government of India. (2023). Digital Personal Data Protection Act, 2023. (Relevant to retention and purpose limitation of KYC data.)",
        "Nakamoto, S. (2008). <i>Bitcoin: A peer-to-peer electronic cash system</i>.",
        "Reserve Bank of India. Public statements and circulars cautioning regulated entities on cryptocurrency-related exposures; e-rupee / CBDC materials (contrast case).",
        "U.S. Department of Justice. (2023). Resolutions concerning Binance Holdings Limited and related persons (BSA / information and plea materials).",
        "U.S. Department of the Treasury / OFAC. (2022–2024). Actions and subsequent litigation concerning Tornado Cash.",
        "Zetzsche, D. A., Buckley, R. P., Arner, D. W., &amp; Föhr, L. (2018–2021). The DLT and FinTech compliance literature on “embedded supervision” and the cost of applying bank-like duties to new intermediaries.",
        "Auer, R. (2022). Embedded supervision: How to build regulation into blockchain finance. BIS Working Papers (discussion of supervisory data access versus traditional reporting).",
        "OECD. (2022–2023). Crypto-asset reporting framework (CARF) materials — the next major cross-border reporting cost for platforms.",
        "Sumsub, Chainalysis, TRM Labs, Elliptic. Public product documentation and industry surveys on KYC and blockchain-analytics pricing (vendor layer described in Section 2).",
        "Securities and Exchange Board of India. Existing adviser / exchange / custody frameworks used in this paper only as analogies for activity-based design.",
        "World Bank / IMF Fintech notes on AML effectiveness and the risk that high compliance cost displaces activity into unmonitored channels.",
        "SGT University, School of Engineering and Technology, Department of CSE. Blockchain Policy case-study brief, 5th Semester, B.Tech CSE (AI/ML), Section C. Submitted to Ms. Bisma.",
        "Indian Computer Emergency Response Team. Incident-reporting directions that add an operational compliance duty distinct from tax and AML.",
    ]
    for r in refs:
        st.append(Paragraph(r, S["ref"]))

    return st


def build() -> Path:
    story = practical_cover() + contents_page() + body()
    buf = io.BytesIO()
    doc = Report(buf, FOOTER, cover_first=True)
    doc.multiBuild(story)
    OUT_PDF.write_bytes(buf.getvalue())
    return OUT_PDF


if __name__ == "__main__":
    path = build()
    print(f"Wrote {path}")
