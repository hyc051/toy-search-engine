#https://huggingface.co/datasets/agentlans/common-crawl-sample
from datasets import load_dataset
import os

ds = load_dataset("agentlans/common-crawl-sample", split="train")
os.makedirs("docs", exist_ok=True)

for i in range(100): #first 100 docs
    uri = ds[i]["uri"]
    text = ds[i]["text"]
    with open(f"docs/doc_{i}.txt", "w", encoding="utf-8") as f:
        f.write(f"URI: {uri}\n")
        f.write("-" * 100 + "\n")
        f.write(text)

print("Finish")