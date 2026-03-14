from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from load_documents import load_docs


def create_db():

    documents = load_docs()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)

    vectorstore.save_local("vector_db")

    print("Vector database created!")


if __name__ == "__main__":
    create_db()