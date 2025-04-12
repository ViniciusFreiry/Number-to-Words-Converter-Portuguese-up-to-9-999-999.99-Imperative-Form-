# Number to Words Converter (Portuguese - PT-BR)

This is a simple **Python script** that converts numbers from **0 to 9,999,999.99** into their **full written form in Brazilian Portuguese (PT-BR)**.

Unlike money formatters, this script does **not** include currency units like "reais" or "centavos". Instead, if a decimal point exists, it is written out using the word **"vírgula"** (comma in Portuguese).

---

## 🧠 Features

- Accepts numbers from `0` to `9,999,999.99`
- Outputs the number in full (written) form in Portuguese
- Handles millions, thousands, hundreds, and decimal fractions
- Includes proper conjunctions (`e`, `vírgula`, etc.)
- Uses imperative programming style for simplicity

---

## 📦 Requirements

No external libraries are required. This script runs with **pure Python 3**.

---

## ▶️ How to Run

1. Clone this repository or copy the script.
2. Make sure you have Python 3 installed.
3. Run the script from your terminal:

```bash
python number_to_words_ptbr.py