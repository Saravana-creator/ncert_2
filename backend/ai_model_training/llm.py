# Using Qwen2.5-1.5B-Instruct for state-of-the-art reasoning and reliability

import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

try:
    # Qwen2.5 is significantly better at logic than TinyLlama
    print("Loading Qwen2.5-1.5B-Instruct...")
    model_name = "Qwen/Qwen2.5-1.5B-Instruct"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        device_map="auto",
        low_cpu_mem_usage=True
    )
    print("[OK] Qwen2.5 loaded successfully")
    model_loaded = True
except Exception as e:
    print(f"[ERROR] Qwen2.5 fails: {e}. Falling back to basic logic.")
    model_loaded = False
    tokenizer = None
    model = None

def answer(question, context_items):
    """
    Generate accurate answer using RAG context with Chain-of-Thought.
    """
    if not context_items:
        return {
            "answer": "I don't have enough specific information in the uploaded NCERT chapters to answer this accurately. Please upload the relevant chapter pages.",
            "citations": []
        }
    
    # Check for direct math calculation first to avoid model confusion
    math_result = handle_math_question(question)
    if math_result:
        return {"answer": math_result, "citations": ["Calculator Tool"]}

    context_text = ""
    citations = []
    seen = set()
    
    for i, item in enumerate(context_items):
        source = f"{item['source']} (Page {item['page']})"
        context_text += f"Source [{i+1}] (from {source}):\n{item['text']}\n\n"
        if source not in seen:
            citations.append(source)
            seen.add(source)

    if model_loaded and model and tokenizer:
        try:
            # Enhanced prompt with Step-by-Step reasoning (Chain of Thought)
            prompt = f"""<|im_start|>system
You are a precise NCERT Subject Matter Expert. Your goal is to provide ACCURATE answers based ONLY on the provided context.

RULES:
1. If the info is NOT in the context, clearly state: "The provided materials do not contain this information."
2. Be extremely careful with chronology (before/after/first/last).
3. Ignore irrelevant context (e.g., ignore Math formulas if the question is about History).
4. Use a TWO-STEP process: 
   - Step 1: Extract direct evidence from the sources.
   - Step 2: Formulate the final answer based on that evidence.
<|im_end|>
<|im_start|>user
Context:
{context_text[:2000]}

Question: {question}

Please answer in this format:
- Reasoning: (Briefly explain your logic using step 1)
- Answer: (The final classroom-ready answer)
<|im_end|>
<|im_start|>assistant
"""
            
            inputs = tokenizer(prompt, return_tensors="pt")
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=400,
                    do_sample=False, # Use greedy for higher factual accuracy
                    temperature=0.0   # 0.0 effectively with greedy
                )
            
            response = tokenizer.decode(outputs[0][len(inputs['input_ids'][0]):], skip_special_tokens=True).strip()
            
            # Clean up the output if it produces extra tokens
            answer_text = response.split("<|im_end|>")[0].strip()
            
            return {
                "answer": answer_text,
                "citations": citations
            }
                
        except Exception as e:
            print(f"[ERROR] Generation error: {e}")
            return generate_structured_answer(question, context_items)
    else:
        return generate_structured_answer(question, context_items)

def handle_math_question(question):
    """Handle basic math to prevent LLM hallucinations on numbers"""
    q = question.lower()
    # Simple regex for 'convert X m to km' or '2500m to km'
    match = re.search(r'(\d+)\s*(m|meter|meters)\s*(in|to|as)\s*(km|kilometer|kilometers)', q)
    if match:
        val = float(match.group(1))
        return f"**Answer:** {val} meters is equal to **{val/1000} kilometers** (1 km = 1000 m)."
    return None

def generate_structured_answer(question, context_items):
    """Fallback: Return most relevant chunk directly"""
    best = context_items[0]
    return {
        "answer": f"**Evidence found in book:**\n{best['text']}\n\n*(Model offline - showing direct source)*",
        "citations": [f"{best['source']} (Page {best['page']})"]
    }