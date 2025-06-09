# 🏛️ Odyssey LLM Knowledge Integration Benchmark 🏺

## 🧪 Technical Assessment Instructions

Welcome! This repository contains a technical assessment for engineering candidates focused on enhancing the performance of a language model on a literary comprehension benchmark derived from *The Odyssey* by Homer.

You will find:
- 📜 A chapter from *The Odyssey* (in plain text format).
- 🧩 A set of multiple-choice questions that evaluate understanding and reasoning based on that chapter.
- 🤖 A baseline language model (DistilGPT) that currently achieves **X%** accuracy on the benchmark.
- ⚙️ Evaluation code in [`evaluation.py`](evaluation.py) to test DistilGPT2 on the benchmark.

Your objective is to **improve this performance** by intelligently incorporating knowledge from the book corpus.

---

## 🎯 Task Overview

Your challenge is to explore, justify, and implement methods that increase the model's ability to correctly answer questions by leveraging knowledge from the provided text.

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

Please follow these procedural steps carefully to ensure a complete and reviewable submission:

### ⚙️ Environment Setup

1. 🧬 **Clone this repository** to your local machine or directly into your GitHub Classroom account:  
   ```bash
   git clone https://github.com/YOUR_ORG_NAME/odyssey-llm-assessment.git
   ```

2. 📓 **Open a new [Google Colab](https://colab.research.google.com/) notebook**.

3. ⚡ **Enable GPU acceleration**:  
   In the Colab menu:  
   `Runtime` → `Change runtime type` → Select `GPU` under “Hardware accelerator”.

### 🔨 Implementation

4. ✍️ **Do all your work in the Colab notebook**, including:
   - Loading the chapter and questions
   - Applying your integration method
   - Evaluating the results
   - Visualizing performance metrics

5. 📥 **Save your notebook** and push it to this GitHub repository root folder:  
   ```bash
   git add your_solution_notebook.ipynb
   git commit -m "Add completed technical assessment notebook"
   git push origin main
   ```

6. 🗃️ **If you generate external files** (e.g., charts, config files, helper scripts), include them in your commit and reference them from the notebook.

---

## 🤖 Use of LLMs & AI Tools

You are encouraged to use Large Language Models such as ChatGPT, Claude, Gemini, or others to assist in:
- Brainstorming
- Code drafting and debugging
- Literature review
- Visualizations

However, you **must explicitly document**:
- Which model(s) or tool(s) you used
- What you used them for
- Why you chose them

This helps us understand how effectively you incorporate modern AI tools into your workflow.

---

## 🏛️ Book License

> _[Placeholder: The excerpt from *The Odyssey* is subject to applicable copyright or public domain laws depending on the translation used. Please ensure that the version provided complies with open-use or academic licensing standards.]_

---

## 🧾 Final Notes

- This is not just a coding test. We are evaluating your **problem-solving approach**, **communication of trade-offs**, and **ability to analyze outcomes**.
- Please aim for **clarity and structure** in your notebook. Use section headings and code comments liberally.
- We appreciate creativity, but also value simplicity and reproducibility.

---

### 📬 Questions?

If anything is unclear, feel free to document assumptions in your notebook or leave inline notes with your reasoning.

Good luck, and enjoy reimagining Odysseus’ journey through the lens of machine intelligence!
