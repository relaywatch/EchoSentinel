# EchoSentinel

**AI Volatility Filter for Autonomous Agent Chains**  
Detects and flags emotional contradiction across GPT-generated prompt chains to ensure consistency, trust, and operational safety in agent workflows.

---
> GPT agents can sound confident while being emotionally unstable.

> EchoSentinel flags emotional contradiction across prompt chains. If an agent flips from “we’re doing great” to “everything might collapse,” this tool scores that volatility and recommends override — before the agent acts.

## 🔍 What It Does

EchoSentinel analyzes a series of prompts (or GPT-generated messages) and measures **emotional volatility**. If the chain flips tone (optimism → doom → joy → fear), it gets flagged.

Use it to:
- 🔒 Validate GPT or agent output before acting
- 📊 Score volatility in reasoning or emotion
- 🧠 Plug into AutoGPT / LangChain to override unstable chains

---

## ⚙️ How It Works

- Uses HuggingFace's `emotion-english-distilroberta-base` to classify each message
- Maps emotions to a numeric scale
- Calculates **variance** across the sequence
- Flags high-volatility chains with: `"recommended_action": "flag"`

---

## 🛠️ Installation

```bash
pip install transformers torch numpy

from echo_sentinel import analyze_prompt_chain

chain = [
    "This is the most amazing breakthrough we've ever seen.",
    "We're all doomed — nothing can save us now.",
    "Our team has made incredible progress!",
    "I fear this project has completely failed."
]

result = analyze_prompt_chain(chain)
print(result)

{
  "volatility_score": 0.0625,
  "recommended_action": "flag"
}
