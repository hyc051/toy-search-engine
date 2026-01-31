from whoosh import index
from whoosh.qparser import QueryParser

idx = index.open_dir("whoosh_index")
parser = QueryParser("content", schema=idx.schema)

print("Type index terms or exit")

while True:
    ipt = input("- ").strip()
    if ipt.lower() == "exit":
        break

    with idx.searcher() as searcher:
        query = parser.parse(ipt)
        results = searcher.search(query, limit=None)
        print("Searched:", len(results), "results")
        for r in results:
            print(r["title"])
