import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


def load_docs():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(BASE_DIR, "data")

    docs = []

    for file in os.listdir(data_path):
        if file.endswith(".md"):
            file_path = os.path.join(data_path, file)
            loader = TextLoader(file_path, encoding="utf-8")
            docs.extend(loader.load())

    print("Documents loaded:", len(docs))

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = splitter.split_documents(docs)

    print("Split documents:", len(documents))

    return documents