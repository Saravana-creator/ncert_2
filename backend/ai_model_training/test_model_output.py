"""Quick test to verify FLAN-T5 model output"""

from llm import answer

# Test cases
test_cases = [
    {
        "question": "What number do we get when we add a thousand to 9,000?",
        "context": ["Mathematics chapter on addition and place value"]
    },
    {
        "question": "What is photosynthesis?",
        "context": ["Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water. Chlorophyll is essential for this process. Plants produce oxygen as a byproduct."]
    },
    {
        "question": "Why do we need oxygen?",
        "context": ["Oxygen is essential for respiration in living organisms. It helps in breaking down food to release energy. Without oxygen, cells cannot produce energy efficiently."]
    }
]

print("=" * 60)
print("TESTING FLAN-T5 MODEL OUTPUT")
print("=" * 60)

for i, test in enumerate(test_cases, 1):
    print(f"\n[TEST {i}]")
    print(f"Question: {test['question']}")
    print(f"Context: {test['context'][0][:80]}...")
    print("\n" + "-" * 60)
    
    result = answer(test['question'], test['context'])
    print(f"Answer:\n{result}")
    print("=" * 60)
