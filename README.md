# Blockchain Policy — Case Studies

Undergraduate case studies for **Blockchain Policy**, School of Engineering and Technology, Department of CSE, **SGT University**. Fifth semester, B.Tech CSE (AI/ML), Section C. Submitted to **Ms. Bisma**.

This repository is independent of [HKTITAN/DBMS-Lab](https://github.com/HKTITAN/DBMS-Lab). Do not merge the two.

**GitHub:** [https://github.com/HKTITAN/Blockchain-Policy](https://github.com/HKTITAN/Blockchain-Policy)

## Students and PDFs

| Student | Roll | Topic | PDF |
|---------|------|-------|-----|
| Harshit Khemani | 241302081 | Blockchain Security: Technology vs. Human Error | [View on GitHub](https://github.com/HKTITAN/Blockchain-Policy/blob/main/harshit-khemani/Blockchain_Security_Technology_vs_Human_Error.pdf) · [Raw download](https://raw.githubusercontent.com/HKTITAN/Blockchain-Policy/main/harshit-khemani/Blockchain_Security_Technology_vs_Human_Error.pdf) |
| Kush Ahuja | 241302122 | Blockchain and the Cost of Regulatory Compliance | [View on GitHub](https://github.com/HKTITAN/Blockchain-Policy/blob/main/kush-ahuja/Blockchain_and_the_Cost_of_Regulatory_Compliance.pdf) · [Raw download](https://raw.githubusercontent.com/HKTITAN/Blockchain-Policy/main/kush-ahuja/Blockchain_and_the_Cost_of_Regulatory_Compliance.pdf) |

Each PDF is a complete academic case study (SGT practical-file cover + abstract through references), generated with ReportLab in navy academic styling.

## Clone / download

```bash
git clone https://github.com/HKTITAN/Blockchain-Policy.git
cd Blockchain-Policy
```

ZIP download (no git): [https://github.com/HKTITAN/Blockchain-Policy/archive/refs/heads/main.zip](https://github.com/HKTITAN/Blockchain-Policy/archive/refs/heads/main.zip)

Direct PDF downloads (right-click / `curl -LO`):

```text
https://raw.githubusercontent.com/HKTITAN/Blockchain-Policy/main/harshit-khemani/Blockchain_Security_Technology_vs_Human_Error.pdf
https://raw.githubusercontent.com/HKTITAN/Blockchain-Policy/main/kush-ahuja/Blockchain_and_the_Cost_of_Regulatory_Compliance.pdf
```

## Rebuild the PDFs

Python 3.10+ and the packages in `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
python3 harshit-khemani/generate_case_study.py
python3 kush-ahuja/generate_case_study.py
```

The SGT logo is stored at `assets/sgt-logo.png` (same artwork used on the DBMS Lab practical-file cover). Covers regenerate from that file; do not hand-edit the PDFs.

## Layout

```
README.md
AGENTS.md
assets/sgt-logo.png
requirements.txt
harshit-khemani/generate_case_study.py
harshit-khemani/Blockchain_Security_Technology_vs_Human_Error.pdf
kush-ahuja/generate_case_study.py
kush-ahuja/Blockchain_and_the_Cost_of_Regulatory_Compliance.pdf
```
