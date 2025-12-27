#OCR is Optical Character Reader

from paddleocr import PaddleOCR
import os
from PyPDF2 import PdfReader

try:
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
except Exception as e:
    print(f"PaddleOCR initialization failed: {e}")
    ocr = None

def extract_text(path):
    try:
        print(f"Processing file at: {path}")
        
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return f"File not found: {path}"
        
        # Check if file is PDF
        if path.lower().endswith('.pdf'):
            print("PDF detected, extracting text directly...")
            try:
                reader = PdfReader(path)
                all_text = []
                
                for i, page in enumerate(reader.pages):
                    print(f"Processing page {i+1}/{len(reader.pages)}")
                    text = page.extract_text()
                    if text:
                        all_text.append(text)
                
                combined_text = " ".join(all_text)
                print(f"PDF extracted {len(combined_text)} characters from {len(reader.pages)} pages")
                return combined_text if combined_text else "No text found in PDF"
                
            except Exception as e:
                print(f"PDF processing error: {e}")
                return f"Error processing PDF: {str(e)}"
        
        else:
            # Handle image files with OCR
            if not ocr:
                return f"OCR not available for image processing"
                
            print(f"Image file detected, processing with OCR...")
            res = ocr.ocr(path)
            
            if res and res[0]:
                text = " ".join([l[1][0] for l in res[0]])
                print(f"Image OCR extracted {len(text)} characters")
                return text
            else:
                print("No text detected in image")
                return "No text found in image"
            
    except Exception as e:
        print(f"OCR Error: {e}")
        return f"Error processing file: {str(e)}"