# NCERT AI System Diagnostic Tool
import sys

print("="*60)
print("NCERT AI SYSTEM DIAGNOSTIC")
print("="*60)

# Test 1: Basic imports
print("\n1. Testing Basic Imports...")
try:
    import fastapi
    import uvicorn
    import pydantic
    print("   [OK] FastAPI, Uvicorn, Pydantic")
except Exception as e:
    print(f"   [FAIL] Basic imports: {e}")

# Test 2: PDF Processing
print("\n2. Testing PDF Processing...")
try:
    from PyPDF2 import PdfReader
    print("   [OK] PyPDF2")
except Exception as e:
    print(f"   [FAIL] PyPDF2: {e}")

# Test 3: Sentence Transformers
print("\n3. Testing Sentence Transformers...")
try:
    from sentence_transformers import SentenceTransformer
    print("   [LOADING] BAAI/bge-m3 model...")
    model = SentenceTransformer("BAAI/bge-m3")
    test_embedding = model.encode("test")
    print(f"   [OK] BAAI/bge-m3 - Shape: {test_embedding.shape}")
except Exception as e:
    print(f"   [FAIL] Sentence Transformers: {e}")

# Test 4: PyTorch
print("\n4. Testing PyTorch...")
try:
    import torch
    print(f"   [OK] PyTorch {torch.__version__}")
    print(f"   [INFO] CUDA Available: {torch.cuda.is_available()}")
except Exception as e:
    print(f"   [FAIL] PyTorch: {e}")

# Test 5: Transformers
print("\n5. Testing Transformers...")
try:
    from transformers import AutoTokenizer
    print("   [OK] Transformers library")
except Exception as e:
    print(f"   [FAIL] Transformers: {e}")

# Test 6: Phi-2 Model
print("\n6. Testing Phi-2 Model (THIS IS THE MAIN TEST)...")
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
    print("   [LOADING] Phi-2 model (may take 2-5 min first time)...")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)
    print("   [OK] Tokenizer loaded")
    
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/phi-2",
        torch_dtype=torch.float32,
        trust_remote_code=True,
        low_cpu_mem_usage=True
    )
    print("   [OK] Phi-2 model loaded!")
    
    # Quick test
    inputs = tokenizer("2+2=", return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=5)
    result = tokenizer.decode(outputs[0])
    print(f"   [OK] Generation test passed: {result}")
    
except Exception as e:
    print(f"   [FAIL] Phi-2 model: {e}")
    print("   [INFO] This is likely the main issue!")

# Test 7: Custom modules
print("\n7. Testing Custom Modules...")
try:
    from rag import add_to_vector_db, retrieve
    from llm import answer
    from ocr import extract_text
    print("   [OK] All custom modules imported")
except Exception as e:
    print(f"   [FAIL] Custom modules: {e}")

print("\n" + "="*60)
print("DIAGNOSTIC COMPLETE")
print("="*60)
print("\nLook for [FAIL] messages above to identify issues.")
print("="*60)