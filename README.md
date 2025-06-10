# ⛵ Odyssey LLM Knowledge Integration Benchmark 🏺


Welcome! This repository contains a technical assessment for engineering candidates centered on enhancing a language model’s literary comprehension abilities using a benchmark derived from *The Odyssey* by Homer.

---

### What You Will Find in This Repository

You will be working with the following assets:

- A chapter from *The Odyssey* (provided in plain text format).
- A set of multiple-choice questions assessing comprehension and reasoning from the chapter.
- A benchmark notebook that evaluates model performance on these questions.
- Baseline results from Google’s FLAN language model, which currently achieves **20% accuracy** on this benchmark (see full results below).
- Evaluation code in [`evaluation.py`](evaluation.py), which was used to assess the baseline performance of the Google FLAN model, and can also be used to test new models or approaches on the same set of questions.


---

### 🎯 Your Objective

Your goal is to **improve the model’s accuracy** by intelligently leveraging the content of the provided chapter using the **Google FLAN** model as the baseline.

Specifically:

- You must use the **`google/flan-t5-small`** model from Hugging Face.  
  This lightweight model is easy to use, quick to load, and ensures consistent comparisons across submissions.

  ```python
  from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

  model_name = "google/flan-t5-small"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


- Explore and justify techniques that can help the model understand and reason better over literary texts.
- Implement and evaluate improvements using the existing benchmark framework.
- You may choose to use retrieval augmentation, prompt engineering, fine-tuning, or other NLP techniques—your design choices should be clear and defensible.

---


## 📘 Odyssey LLM Quiz – Evaluation Report

The current benchmark uses **Google FLAN**, a powerful instruction-tuned model, which achieves **20% accuracy** across 30 multiple-choice questions. You can find the full evaluation breakdown below to understand which types of questions it struggled with.

---

### Q1: To which island did Ulysses and his men first sail after leaving Aeolus?  
**Correct Answer:** Aeolian island  
**Predicted Answer:** Laestrygonian island  
**Result:** ❌ Incorrect

### Q2: Who is Aeolus the son of?  
**Correct Answer:** Hippotas  
**Predicted Answer:** Poseidon  
**Result:** ❌ Incorrect

### Q3: How many daughters and sons does Aeolus have?  
**Correct Answer:** Six daughters and six sons  
**Predicted Answer:** Six daughters and six sons  
**Result:** ✅ Correct!

### Q4: How long did Aeolus entertain Ulysses?  
**Correct Answer:** A month  
**Predicted Answer:** A week  
**Result:** ❌ Incorrect

### Q5: What gift did Aeolus give Ulysses to help him on his way?  
**Correct Answer:** A sack holding the winds  
**Predicted Answer:** A strong ship  
**Result:** ❌ Incorrect

### Q6: What kind of thread was used to bind the mouth of the sack of winds?  
**Correct Answer:** Silver thread  
**Predicted Answer:** Linen thread  
**Result:** ❌ Incorrect

### Q7: Which wind did Aeolus allow to blow to help Ulysses's ship?  
**Correct Answer:** West wind  
**Predicted Answer:** East wind  
**Result:** ❌ Incorrect

### Q8: Why did Ulysses's men open the sack of winds?  
**Correct Answer:** They thought Ulysses was hiding gold and silver.  
**Predicted Answer:** They were curious about the contents.  
**Result:** ❌ Incorrect

### Q9: How many days and nights did Ulysses and his men sail after leaving Aeolus the first time, before their native land showed on the horizon?  
**Correct Answer:** Nine days and nine nights  
**Predicted Answer:** Seven days and seven nights  
**Result:** ❌ Incorrect

### Q10: What was Ulysses doing when his men opened the sack of winds?  
**Correct Answer:** Sleeping lightly  
**Predicted Answer:** Feasting with them  
**Result:** ❌ Incorrect

### Q11: How did Aeolus react when Ulysses returned to his island after the winds escaped?  
**Correct Answer:** He sent him away, calling him abhorred of heaven.  
**Predicted Answer:** He welcomed him back kindly.  
**Result:** ❌ Incorrect

### Q12: After leaving Aeolus the second time, where did Ulysses and his men reach on the seventh day?  
**Correct Answer:** The rocky stronghold of Lamus  
**Predicted Answer:** The Aeaean island  
**Result:** ❌ Incorrect

### Q13: What is the name of the city of the Laestrygonians?  
**Correct Answer:** Telepylus  
**Predicted Answer:** Ogygian  
**Result:** ❌ Incorrect

### Q14: What did Ulysses do with his own ship when they reached the Laestrygonian harbour?  
**Correct Answer:** He moored it to a rock outside the harbor.  
**Predicted Answer:** He moored it to a rock outside the harbor.  
**Result:** ✅ Correct!

### Q15: Who was the king of the Laestrygonians?  
**Correct Answer:** Antiphates  
**Predicted Answer:** Aeetes  
**Result:** ❌ Incorrect

### Q16: What did the Laestrygonians do to Ulysses's men and ships in the harbour?  
**Correct Answer:** They threw vast rocks, crunching the ships and spearing the men.  
**Predicted Answer:** They welcomed them and offered them food.  
**Result:** ❌ Incorrect

### Q17: Who is Circe the sister of?  
**Correct Answer:** Aeetes  
**Predicted Answer:** Perse  
**Result:** ❌ Incorrect

### Q18: What animal did Ulysses kill near Circe's house to feed his men?  
**Correct Answer:** A stag  
**Predicted Answer:** A wild boar  
**Result:** ❌ Incorrect

### Q19: What did Circe do to Ulysses's men after they drank her mess?  
**Correct Answer:** She turned them into pigs.  
**Predicted Answer:** She made them forget their homes.  
**Result:** ❌ Incorrect

### Q20: Who was the only man who suspected mischief and stayed outside Circe's house?  
**Correct Answer:** Eurylochus  
**Predicted Answer:** Polites  
**Result:** ❌ Incorrect

### Q21: Who appeared to Ulysses to help him against Circe?  
**Correct Answer:** Mercury  
**Predicted Answer:** Poseidon  
**Result:** ❌ Incorrect

### Q22: What is the name of the herb that protects Ulysses from Circe's magic?  
**Correct Answer:** Moly  
**Predicted Answer:** Moly  
**Result:** ✅ Correct!

### Q23: What is the appearance of the herb Moly?  
**Correct Answer:** Black root and white flower  
**Predicted Answer:** Black root and white flower  
**Result:** ✅ Correct!

### Q24: What does Ulysses make Circe swear before he goes to bed with her?  
**Correct Answer:** That she will plot no further harm against him  
**Predicted Answer:** That she will help him get home immediately  
**Result:** ❌ Incorrect

### Q25: How did Circe turn Ulysses's men back into humans?  
**Correct Answer:** By touching them with her wand a second time.  
**Predicted Answer:** By touching them with her wand a second time.  
**Result:** ✅ Correct!

### Q26: How long did Ulysses and his men stay with Circe?  
**Correct Answer:** A whole twelvemonth  
**Predicted Answer:** Six months  
**Result:** ❌ Incorrect

### Q27: What is the next journey Ulysses must take before sailing homewards, according to Circe?  
**Correct Answer:** To go to the house of Hades and Proserpine  
**Predicted Answer:** To consult the oracle at Delphi  
**Result:** ❌ Incorrect

### Q28: Whose ghost does Ulysses need to consult in the house of Hades?  
**Correct Answer:** Teiresias  
**Predicted Answer:** Achilles  
**Result:** ❌ Incorrect

### Q29: What offering does Circe instruct Ulysses to pour into the trench for the dead?  
**Correct Answer:** Honey mixed with milk, wine, and water  
**Predicted Answer:** Wine, oil, and blood  
**Result:** ❌ Incorrect

### Q30: What happened to Elpenor before Ulysses and his men left Circe's island?  
**Correct Answer:** He fell off the roof and broke his neck.  
**Predicted Answer:** He fell off the roof and broke his neck.  
**Result:** ✅ Correct!

---

### 📊 **Model Accuracy**: **20.00%** (6 out of 30 correct)


### You must:

1. 🛠️ **Choose a knowledge integration method**, such as:
   - Prompt engineering
   - Retrieval-Augmented Generation (RAG)
   - Embedding-based context retrieval
   - Light-weight fine-tuning or instruction tuning
   - Any hybrid or creative approach

2. 🧠 **Clearly explain your rationale** for the method(s) selected. Why is your approach appropriate for this task? What trade-offs did you consider?

3. 💻 **Implement your full pipeline in code**, including:
   - Preprocessing the corpus (if needed)
   - Modifying the inference setup
   - Running the benchmark
   - Logging outputs and scores

4. 📊 **Produce plots and visualizations** that explain your findings and support your decisions, such as:
   - Accuracy improvements
   - Question-wise model behavior
   - Error breakdowns
   - Confidence calibration (if applicable)

---

## 🧑‍💻 Submission Instructions

Please follow these steps to ensure a complete and reviewable submission.

---

### 💻 Environment Setup

You may use **any IDE or platform you prefer**, including VS Code, Jupyter, PyCharm, or others.

> ⚡️ However, we **recommend using [Google Colab](https://colab.research.google.com/)** or [Kaggle Notebooks](https://www.kaggle.com/code) due to their **free access to GPUs**, which can significantly ease testing and prototyping.

To get started quickly:

```bash
git clone https://github.com/AI-BIIE-Initiative/odyssey-llm-quiz.git
cd odyssey-llm-quiz


## 🏛️ Book License

> _[Placeholder: The excerpt from *The Odyssey* is subject to applicable copyright or public domain laws depending on the translation used. Please ensure that the version provided complies with open-use or academic licensing standards.]_

---

## Final Notes

- This is not just a coding test. We are evaluating your **problem-solving approach**, **communication of trade-offs**, and **ability to analyze outcomes**.
- Please aim for **clarity and structure** in your notebook. Use section headings and code comments liberally.
- We appreciate creativity, but also value simplicity and reproducibility.

---

### Questions?

If anything is unclear, feel free to document assumptions in your notebook or leave inline notes with your reasoning.

Good luck, and enjoy reimagining Odysseus’ journey through the lens of machine intelligence!
