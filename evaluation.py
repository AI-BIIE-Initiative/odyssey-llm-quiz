import json
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load FLAN-T5 small
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.eval()

# Load benchmark JSON
with open("OdysseyMCQ_balanced.json", "r") as f:
    benchmark = json.load(f)

# Evaluate
num_correct = 0

for i, item in enumerate(benchmark):
    question = item["question"]
    answers = item["answers"]
    correct_index = item["correct_index"]

    # Construct prompt with options
    prompt = f"Question: {question}\nOptions: " + ", ".join(f"{j+1}. {ans}" for j, ans in enumerate(answers)) + "\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=10)
    
    predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Find best match: check if generated answer contains any of the answer strings
    predicted_index = -1
    for idx, ans in enumerate(answers):
        if ans.lower() in predicted_text.lower():
            predicted_index = idx
            break

    # Fallback: if no match, use option number parsing
    if predicted_index == -1:
        for idx, ans in enumerate(answers):
            if str(idx+1) in predicted_text:
                predicted_index = idx
                break

    is_correct = predicted_index == correct_index
    num_correct += is_correct

    print(f"Q{i+1}: {question}")
    print(f"  Correct Answer   [{correct_index}]: {answers[correct_index]}")
    print(f"  Predicted Answer [{predicted_index}]: {answers[predicted_index] if predicted_index != -1 else 'N/A'}")
    print("  ✅ Correct!" if is_correct else "  ❌ Incorrect")
    print()

# Print accuracy
total = len(benchmark)
accuracy = num_correct / total * 100
print(f"FLAN-T5 Model Accuracy: {accuracy:.2f}% ({num_correct}/{total})")
