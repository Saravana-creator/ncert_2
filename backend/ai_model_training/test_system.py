"""
NCERT AI System Diagnostic Tool
Run this to check what's working and what's broken
"""

print("="*60)
print("NCERT AI SYSTEM DIAGNOSTIC")
print("="*60)
print()

# Test 1: Basic imports
print("1. Testing Basic Imports...")
try:
    import fastapi
    import uvicorn
    import pydantic
    print("   ✅ FastAPI, Uvicorn, Pydantic - OK")
except Exception as e:
    print(f"   ❌ Basic imports failed: {e}")

# Test 2: PDF Processing
print("\n2. Testing PDF Processing...")
try:
    from PyPDF2 import PdfReader
    print("   ✅ PyPDF2 - OK")
except Exception as e:
    print(f"   ❌ PyPDF2 failed: {e}")

# Test 3: Sentence Transformers
print("\n3. Testing Sentence Transformers (BAAI/bge-m3)...")
try:
    from sentence_transformers import SentenceTransformer
    print("   ⏳ Loading BAAI/bge-m3 model...")
    model = SentenceTransformer("BAAI/bge-m3")
    test_embedding = model.encode("test")
    print(f"   ✅ BAAI/bge-m3 loaded - Embedding shape: {test_embedding.shape}")
except Exception as e:
    print(f"   ❌ Sentence Transformers failed: {e}")

# Test 4: Transformers & Torch
print("\n4. Testing Transformers & PyTorch...")
try:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    print(f"   ✅ PyTorch {torch.__version__} - OK")
    print(f"   ✅ Transformers - OK")
    print(f"   ℹ️  CUDA Available: {torch.cuda.is_available()}")
except Exception as e:
    print(f"   ❌ Transformers/Torch failed: {e}")

# Test 5: Phi-2 Model
print("\n5. Testing Phi-2 Model...")
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
    print("   ⏳ Loading Phi-2 (this may take 2-5 minutes first time)...")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/phi-2",
        torch_dtype=torch.float32,
        trust_remote_code=True,
        low_cpu_mem_usage=True
    )
    print("   ✅ Phi-2 model loaded successfully!")
    
    # Test generation
    print("   ⏳ Testing text generation...")
    test_prompt = "What is 2+2?"
    inputs = tokenizer(test_prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=20)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"   ✅ Generation test: {result[:50]}...")
    
except Exception as e:
    print(f"   ❌ Phi-2 failed: {e}")
    print(f"   ℹ️  This is the main issue - Phi-2 not loading")

# Test 6: RAG Components
print("\n6. Testing RAG Components...")
try:
    from rag import add_to_vector_db, retrieve
    print("   ✅ RAG module imported")
    
    # Test adding to vector DB
    add_to_vector_db("Test content about mathematics and angles")
    results = retrieve("what are angles")
    print(f"   ✅ Vector DB working - Retrieved {len(results)} chunks")
    
except Exception as e:
    print(f"   ❌ RAG failed: {e}")

# Test 7: OCR
print("\n7. Testing OCR...")
try:
    from ocr import extract_text
    print("   ✅ OCR module imported")
except Exception as e:
    print(f"   ❌ OCR failed: {e}")

# Test 8: LLM
print("\n8. Testing LLM Module...")
try:
    from llm import answer
    print("   ✅ LLM module imported")
    
    # Test answer generation
    test_answer = answer("What is 2+2?", ["Two plus two equals four"])
    print(f"   ✅ Answer generation working")
    print(f"   📝 Sample output: {test_answer[:100]}...")
    
except Exception as e:
    print(f"   ❌ LLM failed: {e}")

# Summary
print("\n" + "="*60)
print("DIAGNOSTIC SUMMARY")
print("="*60)
print("\nIf you see ❌ errors above, those components need fixing.")
print("Most common issue: Phi-2 model not loading (takes 5.5GB download)")
print("\nTo fix:")
print("1. Make sure you're in virtual environment")
print("2. Run: pip install -r requirements.txt")
print("3. Wait for Phi-2 to download (first time only)")
print("="*60)