from datasets import load_dataset
import os
import time

DOCS_DIR = "docs"
os.makedirs(DOCS_DIR, exist_ok=True)

ds = load_dataset("agentlans/common-crawl-sample", split="train")

n = int(input("Add how many new docs?"))

exist_doc = 0
for name in os.listdir(DOCS_DIR):
    if name.endswith(".txt"):
        exist_doc += 1

print(f"Existing documents: {exist_doc}")
start = time.time()
for i in range(exist_doc, exist_doc + n):
    uri = ds[i]["uri"]
    text = ds[i]["text"]

    with open(f"docs/doc_{i}.txt", "w", encoding="utf-8") as f:
        f.write(f"URI: {uri}\n")
        f.write("-" * 100 + "\n")
        f.write(text)

end = time.time()
print("Finish adding")
print(f"Adding takes: {end - start:.4f} seconds")