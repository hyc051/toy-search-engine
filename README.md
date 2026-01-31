# toy-search-engine
## File introduction
The `dataset_crawler` file is used to crawl and extract 100 documents from a web dataset.

The `indexing` file is used to build the search index.

The `search` file is used to query the indexed documents.

The `step3` file is used specifically for step 3 by adding 100 documents with unique identifiers.

The `add_doc` file is used to add documents to the docs folder, the data is also crawled and extracted from the web dataset.

Web dataset used: `https://huggingface.co/datasets/agentlans/common-crawl-sample`

## How to run the program:


####  Install two packages first

`pip install datasets`

`pip install whoosh`

First, run `dataset_crawler.py` to generate the initial 100 documents for Step 1.
After that, use `add_docs.py` to add more documents when needed.
Please remember to rebuild the index by running `indexing.py` before performing any search whenever new documents are added.
