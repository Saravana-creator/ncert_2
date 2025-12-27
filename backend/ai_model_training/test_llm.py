"""
Test the LLM answer function with real questions
"""

print("="*60)
print("TESTING LLM ANSWER GENERATION")
print("="*60)

# Import the answer function
from llm import answer

# Test 1: Math question (should calculate)
print("\n" + "="*60)
print("TEST 1: Math Question")
print("="*60)
question1 = "What number do we get when we add a thousand to 9,000?"
context1 = ["Numbers can be added together", "Mathematics involves calculations"]

print(f"\nQuestion: {question1}")
print(f"Context: {context1}")
print("\nAnswer:")
result1 = answer(question1, context1)
print(result1)

# Test 2: Definition question with NCERT content
print("\n" + "="*60)
print("TEST 2: Definition Question")
print("="*60)
question2 = "What are angles?"
context2 = [
    "Angles are formed when two lines meet at a point.",
    "They are measured in degrees.",
    "A right angle is 90 degrees."
]

print(f"\nQuestion: {question2}")
print(f"Context: {context2}")
print("\nAnswer:")
result2 = answer(question2, context2)
print(result2)

# Test 3: No context
print("\n" + "="*60)
print("TEST 3: No Context")
print("="*60)
question3 = "What is quantum physics?"
context3 = []

print(f"\nQuestion: {question3}")
print(f"Context: {context3}")
print("\nAnswer:")
result3 = answer(question3, context3)
print(result3)

# Test 4: Another math question
print("\n" + "="*60)
print("TEST 4: Another Math Question")
print("="*60)
question4 = "If we add 500 and 250, what do we get?"
context4 = ["Addition is a basic arithmetic operation"]

print(f"\nQuestion: {question4}")
print(f"Context: {context4}")
print("\nAnswer:")
result4 = answer(question4, context4)
print(result4)

print("\n" + "="*60)
print("TESTING COMPLETE")
print("="*60)
print("\nCheck if:")
print("1. Math questions give calculated answers (e.g., 10,000)")
print("2. Definition questions use context properly")
print("3. No-context questions give appropriate message")
print("="*60)