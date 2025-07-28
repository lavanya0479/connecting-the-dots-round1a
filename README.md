# PDF Outline Extractor

This repository contains a solution for **Round 1A** of the **"Connecting the Dots" Challenge**. It extracts the **Title**, **H1**, **H2**, and **H3** sections (along with page numbers) from a collection of PDF documents and outputs a structured JSON per file.

---

## ✅ Features

- Extracts:
  - **Document Title** (from largest text on first page)
  - **Headings** (H1, H2, H3) based on font size and indentation
  - **Page numbers** for each section
- Runs fully **offline**
- Works inside a **Docker container**
- Outputs valid JSON for each input PDF

---

## 📁 Folder Structure
```bash
connecting_the_dots/
├── Dockerfile
├── requirements.txt
├── process_pdfs.py
├── schema/
│ └── output_schema.json
├── sample_dataset/
│ ├── input/
│ │ ├── file01.pdf
│ │ └── file02.pdf
│ ├── output/
│ └── schema/
│ └── output_schema.json
```

---

## 🐳 Docker Usage

### 1. Build the Docker image:

```bash
docker build -t pdf-outline-extractor .
docker run --rm ^
  -v "${PWD}/sample_dataset/input:/app/input" ^
  -v "${PWD}/sample_dataset/output:/app/output" ^
  --network none ^
  pdf-outline-extractor
```
---
## ⚙️ Technologies
Python 3.10

PyMuPDF (fitz)

Docker (CPU-only, ≤200MB image size)
