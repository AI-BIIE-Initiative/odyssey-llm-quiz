import json
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def evaluate_model_on_benchmark(model, tokenizer, benchmark_path):
    with open(benchmark_path, "r") as f:
        benchmark = json.load(f)

    num_correct = 0

    for i, item in enumerate(benchmark):
        question = item["question"]
        answers = item["answers"]
        correct_index = item["correct_index"]

        prompt = f"Question: {question}\nOptions: " + ", ".join(f"{j+1}. {ans}" for j, ans in enumerate(answers)) + "\nAnswer:"
        inputs = tokenizer(prompt, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=10)
        
        predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        predicted_index = -1
        for idx, ans in enumerate(answers):
            if ans.lower() in predicted_text.lower():
                predicted_index = idx
                break

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

    total = len(benchmark)
    accuracy = num_correct / total * 100
    print(f"Model Accuracy: {accuracy:.2f}% ({num_correct}/{total})")

def main():
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.eval()

    benchmark_path = "OdysseyMCQ_balanced.json"
    evaluate_model_on_benchmark(model, tokenizer, benchmark_path)

if __name__ == "__main__":
    main()
