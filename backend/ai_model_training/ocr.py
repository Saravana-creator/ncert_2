#OCR is Optical Character Reader

try:
    from paddleocr import PaddleOCR
except ImportError:
    print("PaddleOCR not installed.")
    PaddleOCR = None

import os
from PyPDF2 import PdfReader

# Initialize PaddleOCR with Hindi (which covers Devanagari) and English
try:
    # lang='hi' supports Hindi and English characters
    ocr = PaddleOCR(use_angle_cls=True, lang='hi')
except Exception as e:
    print(f"PaddleOCR initialization failed: {e}")
    ocr = None

def extract_text(path):
    """
    Extracts text from PDF or Image.
    Returns a list of dicts: [{'text': str, 'page': int, 'source': str}]
    """
    try:
        print(f"Processing file at: {path}")
        file_name = os.path.basename(path)
        
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return []
        
        results = []

        # Check if file is PDF
        if path.lower().endswith('.pdf'):
            print("PDF detected, extracting text directly...")
            try:
                reader = PdfReader(path)
                
                for i, page in enumerate(reader.pages):
                    print(f"Processing page {i+1}/{len(reader.pages)}")
                    text = page.extract_text()
                    
                    # If direct extraction fails (scanned PDF), try OCR on the page image if possible
                    # For simplicity in this version, we stick to text extraction + basic fallback warning
                    if not text or len(text.strip()) < 50:
                         # TODO: Convert page to image and use OCR (requires pdf2image)
                         # For now, just mark it
                         text = "[Scanned content or Empty Page]"
                    
                    if text and len(text.strip()) > 10:
                        results.append({
                            'text': text,
                            'page': i + 1,
                            'source': file_name
                        })
                
                print(f"PDF extracted content from {len(results)} pages")
                return results
                
            except Exception as e:
                print(f"PDF processing error: {e}")
                return []
        
        else:
            # Handle image files with OCR
            if not ocr:
                print("OCR not available for image processing")
                return []
                
            print(f"Image file detected, processing with OCR...")
            res = ocr.ocr(path, cls=True)
            
            if res and res[0]:
                # Combine all detected lines
                text = " ".join([line[1][0] for line in res[0]])
                print(f"Image OCR extracted {len(text)} characters")
                results.append({
                    'text': text,
                    'page': 1, # Images are treated as single page
                    'source': file_name
                })
                return results
            else:
                print("No text detected in image")
                return []
            
    except Exception as e:
        print(f"OCR Error: {e}")
        return []