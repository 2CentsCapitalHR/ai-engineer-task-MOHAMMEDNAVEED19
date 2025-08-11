<!-- [![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vgbm4cZ0)-->


# Corporate Agent - ADGM Legal Assistant

## Overview
The **Corporate Agent** is an AI-powered legal assistant designed to review, validate, and help users prepare documentation for business incorporation and compliance within the **Abu Dhabi Global Market (ADGM)** jurisdiction. It leverages **Retrieval-Augmented Generation (RAG)** to ensure alignment with real-world ADGM laws, regulations, and processes.

## Features
- **Upload & Parse Documents**: Accepts `.docx` documents and identifies document types.
- **Completeness Check**: Verifies if all mandatory documents are provided for a specific process.
- **Red Flag Detection**: Highlights legal risks, inconsistencies, and non-compliant clauses.
- **Contextual Comments**: Inserts comments directly into the `.docx` file for flagged content.
- **Clause Suggestions** *(Optional)*: Proposes legally compliant alternatives.
- **Downloadable Reviewed Files**: Generates marked-up `.docx` files.
- **Structured Reporting**: Outputs findings in JSON/Python format.

## Architecture
1. **Document Upload Module**: Handles file upload and format validation.
2. **Document Parsing & Classification Module**: Reads `.docx` files and identifies document type.
3. **Compliance Checklist Module**: Compares against a predefined ADGM document checklist.
4. **Red Flag Detection Module**: Uses AI/NLP to detect issues.
5. **Comment Insertion Module**: Adds contextual notes to flagged content.
6. **Report Generation Module**: Produces JSON/Python structured output.
7. **Output Module**: Prepares reviewed `.docx` for download.

## Setup Instructions
```bash
# Clone repository
git clone https://github.com/2CentsCapitalHR/ai-engineer-task-MOHAMMEDNAVEED19.git
cd corporate-agent

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Usage
1. Upload `.docx` documents.
2. The system classifies and verifies completeness.
3. Review the highlighted red flags.
4. Download the marked-up `.docx` and structured report.

## References
- [General Incorporation, AoA, MoA, Registers, UBO, Board Resolutions](https://www.adgm.com/registration-authority/registration-and-incorporation)
- [Resolution for Incorporation (LTD - Multiple Shareholders)](https://assets.adgm.com/download/assets/adgm-ra-resolution-multiple-incorporate-shareholders-LTD-incorporation-v2.docx/186a12846c3911efa4e6c6223862cd87)
- [Incorporation, SPV, LLC, Other Forms & Templates](https://www.adgm.com/setting-up)
- [Guidance, Templates, Policy Statements](https://www.adgm.com/legal-framework/guidance-and-policy-statements)
- [Checklist – Company Set-up (Various Entities)](https://www.adgm.com/documents/registration-authority/registration-and-incorporation/checklist/branch-non-financial-services-20231228.pdf)
- [Checklist – Private Company Limited](https://www.adgm.com/documents/registration-authority/registration-and-incorporation/checklist/private-company-limited-by-guarantee-non-financial-services-20231228.pdf)
- [Standard Employment Contract Template (2024 update)](https://assets.adgm.com/download/assets/ADGM+Standard+Employment+Contract+Template+-+ER+2024+(Feb+2025).docx/ee14b252edbe11efa63b12b3a30e5e3a)
- [Standard Employment Contract Template (2019 short version)](https://assets.adgm.com/download/assets/ADGM+Standard+Employment+Contract+-+ER+2019+-+Short+Version+(May+2024).docx/33b57a92ecfe11ef97a536cc36767ef8)
- [Appropriate Policy Document Template](https://www.adgm.com/documents/office-of-data-protection/templates/adgm-dpr-2021-appropriate-policy-document.pdf)
- [Annual Accounts & Filings](https://www.adgm.com/operating-in-adgm/obligations-of-adgm-registered-entities/annual-filings/annual-accounts)
- [Application for Official Letters & Permits](https://www.adgm.com/operating-in-adgm/post-registration-services/letters-and-permits)
- [Incorporation Package, Filings, Templates](https://en.adgm.thomsonreuters.com/rulebook/7-company-incorporation-package)
- [Shareholder Resolution – Amendment of Articles](https://assets.adgm.com/download/assets/Templates_SHReso_AmendmentArticles-v1-20220107.docx/97120d7c5af911efae4b1e183375c0b2?forcedownload=1)


