import fitz  # PyMuPDF
import os
import json
import re

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace(".pdf", "")
    outline = []
    seen = set()  # Prevent duplicates

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                if not spans:
                    continue

                text = " ".join([span["text"] for span in spans]).strip()
                if len(text) > 200 or not text or re.match(r'^\d+$', text):
                    continue

                size = max(span["size"] for span in spans)
                is_bold = any(
                    "bold" in span.get("font", "").lower() or span["flags"] & 2
                    for span in spans
                )

                level = None
                if size >= 20 and is_bold:
                    level = "H1"
                elif size >= 16 and is_bold:
                    level = "H2"
                elif size >= 13 and is_bold:
                    level = "H3"

                if level and text not in seen:
                    seen.add(text)
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })

    return {
        "title": title,
        "outline": outline
    }

# ======== Main Runner ========

input_dir = "/app/input"
output_dir = "/app/output"

for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, filename)
        output = extract_outline(pdf_path)
        json_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
