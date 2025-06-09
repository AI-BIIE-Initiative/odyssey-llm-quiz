import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

# Load benchmark JSON
with open("OdysseyMCQ_balanced.json", "r") as f:
    benchmark = json.load(f)

# Function to score answer choices using log-probability
def score_answer(prompt, answer):
    input_text = prompt + " " + answer
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss.item()
    return -loss  # higher score = better

# Evaluate
num_correct = 0

for i, item in enumerate(benchmark):
    question = item["question"]
    answers = item["answers"]
    correct_index = item["correct_index"]
    
    scores = [score_answer(question, ans) for ans in answers]
    predicted_index = scores.index(max(scores))

    is_correct = predicted_index == correct_index
    num_correct += is_correct

    print(f"Q{i+1}: {question}")
    print(f"  Correct Answer   [{correct_index}]: {answers[correct_index]}")
    print(f"  Predicted Answer [{predicted_index}]: {answers[predicted_index]}")
    print("  ✅ Correct!" if is_correct else "  ❌ Incorrect")
    print()

# Print accuracy
total = len(benchmark)
accuracy = num_correct / total * 100
print(f"🔍 Model Accuracy: {accuracy:.2f}% ({num_correct}/{total})")
