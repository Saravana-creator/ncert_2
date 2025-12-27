#This is for generating answers using FLAN-T5 (Google's instruction-tuned model)

import re

try:
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import torch
    
    print("Loading FLAN-T5-base model...")
    model_name = "google/flan-t5-base"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    )
    print("[OK] FLAN-T5-base loaded successfully (850MB)")
    model_loaded = True
except Exception as e:
    print(f"[ERROR] FLAN-T5 failed: {e}")
    model_loaded = False
    tokenizer = None
    model = None

def answer(question, context):
    """Generate intelligent answer"""
    if not context:
        return "I don't have information about this topic in the uploaded NCERT materials. Please upload relevant content first."
    
    question_lower = question.lower()
    combined_context = " ".join(context)[:1000]
    
    # Handle math questions with direct calculation
    math_result = handle_math_question(question_lower)
    if math_result:
        return math_result
    
    # Use FLAN-T5 for reasoning
    if model_loaded and model and tokenizer:
        try:
            # FLAN-T5 works best with clear instructions
            prompt = f"""Answer the question based on the context.

Context: {combined_context}

Question: {question}

Answer:"""
            
            inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_length=150,
                    min_length=10,
                    temperature=0.7,
                    do_sample=True,
                    top_p=0.9,
                    num_return_sequences=1
                )
            
            answer_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            if len(answer_text.strip()) > 10:
                return f"**Answer:** {answer_text}\n\n*Based on your uploaded NCERT materials*"
            else:
                return generate_structured_answer(question, combined_context)
                
        except Exception as e:
            print(f"[ERROR] Generation error: {e}")
            return generate_structured_answer(question, combined_context)
    else:
        return generate_structured_answer(question, combined_context)

def handle_math_question(question):
    """Handle mathematical calculations"""
    question_lower = question.lower()
    
    # Convert word numbers to digits
    word_to_num = {
        'thousand': 1000, 'hundred': 100, 'ten': 10,
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    numbers = []
    
    # Find digit numbers
    digit_nums = re.findall(r'\d+[,\d]*', question)
    for num in digit_nums:
        numbers.append(int(num.replace(',', '')))
    
    # Find word numbers
    for word, value in word_to_num.items():
        if word in question_lower:
            numbers.append(value)
    
    if len(numbers) < 2:
        return None
    
    try:
        num1 = numbers[0]
        num2 = numbers[1]
        
        if 'add' in question_lower or 'plus' in question_lower or 'sum' in question_lower:
            result = num1 + num2
            return f"**Answer:** When we add {num1:,} and {num2:,}, we get **{result:,}**\n\n*Arithmetic calculation*"
        
        elif 'subtract' in question_lower or 'minus' in question_lower:
            result = num1 - num2
            return f"**Answer:** When we subtract {num2:,} from {num1:,}, we get **{result:,}**\n\n*Arithmetic calculation*"
        
        elif 'multiply' in question_lower or 'times' in question_lower:
            result = num1 * num2
            return f"**Answer:** {num1:,} × {num2:,} = **{result:,}**\n\n*Arithmetic calculation*"
        
        elif 'divide' in question_lower:
            result = num1 / num2
            return f"**Answer:** {num1:,} ÷ {num2:,} = **{result:,.2f}**\n\n*Arithmetic calculation*"
    
    except:
        pass
    
    return None

def generate_structured_answer(question, context):
    """Fallback structured answer"""
    question_lower = question.lower()
    sentences = [s.strip() + '.' for s in context.split('.') if len(s.strip()) > 20]
    relevant = sentences[:3]
    
    response = "**Answer:**\n\n"
    
    if 'what' in question_lower or 'define' in question_lower:
        response += "**Definition:** "
    elif 'how' in question_lower:
        response += "**Explanation:** "
    elif 'why' in question_lower:
        response += "**Reason:** "
    
    for sent in relevant:
        response += f"{sent} "
    
    response += "\n\n*Based on your uploaded NCERT materials*"
    return response