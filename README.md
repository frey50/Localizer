# 🗺️ Localizer

Just a smart localizer built with **OpenChat (Mistral-7B)** + **NLLB-1.8B**.  
No fine-tuning. No A100s. Just a clean, open-source pipeline for localization.

> Real-time AI assistant that speaks **Uzbek ↔ English**, fully offline.  
Powered by Hugging Face transformers and some clever wiring.

---

## ✨ Features

- 🔁 **Bidirectional Uzbek ↔ English** translation (NLLB)
- 🧠 **Chat & reasoning** powered by OpenChat (Mistral 7B)
- ⚡ **Runs fully local** — works even on consumer GPUs (RTX 3090, 4090 etc.)
- 🧊 **Quantized** for lower VRAM usage (smooth on 16–24GB GPUs)
- 🗣️ **Prompt-tunable translation** — adjust tone from casual to formal
- 🎯 Potential to rival GPT-4 — all it needs is the right dataset
- 🏢 Built for the people — imagine your homie from the 9th floor speaking like GPT

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
