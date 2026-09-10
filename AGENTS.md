# Agent notes — Blockchain Policy case studies

SGT University, Semester 5, School of Engineering and Technology, Department of CSE.
Course framing: **Blockchain Policy** case studies (not DBMS Lab). Faculty on the cover: **Ms. Bisma**.
Do **not** edit or commit into `HKTITAN/DBMS-Lab`.

## Students

| Folder | Student | Roll | Topic |
|--------|---------|------|--------|
| `harshit-khemani/` | Harshit Khemani | 241302081 | Blockchain Security: Technology vs. Human Error |
| `kush-ahuja/` | Kush Ahuja | 241302122 | Blockchain and the Cost of Regulatory Compliance |

Both: B.Tech CSE (AI/ML), Section - C, 5th Semester.

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

Each `generate_case_study.py` is self-contained (ReportLab). The SGT logo lives at `assets/sgt-logo.png` (copied from the public DBMS-Lab asset URL; this repo does not depend on that tree).

## Rebuild

```bash
python3 -m pip install -r requirements.txt
python3 harshit-khemani/generate_case_study.py
python3 kush-ahuja/generate_case_study.py
```

Commit the generated PDFs. Navy academic styling and the practical-file cover layout should stay aligned with the SGT DBMS Lab cover (title block, logo, Submitted to / Submitted by columns, footer).

## Conventions

- Two **separate** PDFs — never merge both students into one file.
- Cover title: Practical File / Case Study On **BLOCKCHAIN POLICY**.
- Body: full undergraduate case study (abstract through references), not an outline.
- Indian academic register: numbered sections, real cases, policy discussion, recommendations, references.
