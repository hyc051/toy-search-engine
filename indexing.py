import os, shutil
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer

DOCS_DIR = "docs"
INDEX_DIR = "whoosh_index"

schema = Schema(
    title=ID(stored=True, unique=True),  # URI
    content=TEXT(analyzer=StemmingAnalyzer())
)

if os.path.exists(INDEX_DIR): #clear old index
    shutil.rmtree(INDEX_DIR)

os.mkdir(INDEX_DIR)
ix = index.create_in(INDEX_DIR, schema)

writer = ix.writer()
cnt = 0
#indexing
for name in os.listdir(DOCS_DIR):
    if not name.endswith(".txt"):
        continue
    
    path = os.path.join(DOCS_DIR, name)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    header = lines[0]
    body = lines[2:]
    url = header.replace("URI:", "").strip()
    content = "".join(body).strip()

    writer.add_document(title=url, content=content)
    cnt += 1

writer.commit()
print("Indexed", cnt, "documents")
