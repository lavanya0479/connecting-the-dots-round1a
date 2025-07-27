# Connecting the Dots – Round 1A

## 🧠 Objective
Extract structured outline (Title, H1, H2, H3 with page numbers) from PDF files and output JSON format.

## 📁 Structure
- `solution.py` — Main logic to process all PDFs from `/app/input` and create `/app/output/*.json`
- `Dockerfile` — Builds containerized version for offline processing (no internet, CPU-only)
- `requirements.txt` — Python dependencies (e.g., `PyMuPDF`)
- `sample/input/` — Sample PDF(s)
- `sample/output/` — Expected structured JSON output

## 🐳 Run with Docker
```bash
docker build -t adobe-solution .
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none adobe-solution
