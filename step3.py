import os

DOCS_DIR = "docs"
os.makedirs(DOCS_DIR, exist_ok=True)

exist_doc = 0
for name in os.listdir(DOCS_DIR):
    if name.endswith(".txt"):
        exist_doc += 1

print(f"Existing documents: {exist_doc}")

for i in range(exist_doc, exist_doc + 100):
    url = f"http://newdoc/{i}"
    text = f"Newly added 100 docs to show step 3"

    with open(f"{DOCS_DIR}/doc_{i}.txt", "w", encoding="utf-8") as f:
        f.write(f"URI: {url}\n")
        f.write("-" * 100 + "\n")
        f.write(text + "\n")

print("Finish")
