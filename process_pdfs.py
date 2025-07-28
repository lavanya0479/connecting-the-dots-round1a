import fitz  # PyMuPDF
import json
from pathlib import Path

# Define font size thresholds for heading levels
FONT_THRESHOLDS = {
    "H1": 16,
    "H2": 14,
    "H3": 12
}

def get_heading_level(font_size):
    if font_size >= FONT_THRESHOLDS["H1"]:
        return "H1"
    elif font_size >= FONT_THRESHOLDS["H2"]:
        return "H2"
    elif font_size >= FONT_THRESHOLDS["H3"]:
        return "H3"
    return None

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = ""
    outline = []
    max_font_size = 0

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text or len(text) < 3:
                        continue

                    font_size = span["size"]
                    # Capture document title (biggest text on page 1)
                    if page_num == 1 and font_size > max_font_size:
                        title = text
                        max_font_size = font_size

                    heading_level = get_heading_level(font_size)
                    if heading_level:
                        outline.append({
                            "type": heading_level,
                            "text": text,
                            "page": page_num
                        })

    return {
        "title": title,
        "outline": outline
    }

def process_all_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        result = extract_outline(pdf_file)
        output_path = output_dir / f"{pdf_file.stem}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        print(f"✅ Extracted: {pdf_file.name}")

if __name__ == "__main__":
    process_all_pdfs()
