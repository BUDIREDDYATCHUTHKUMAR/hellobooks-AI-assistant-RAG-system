print("Assistant script started")

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline


def run_assistant():

    print("Loading embeddings model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Loading vector database...")

    vectorstore = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever()

    print("\nHellobooks AI Assistant Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask accounting question: ")

        if question.lower() == "exit":
            break

        # Retrieve relevant documents
        docs = retriever.invoke(question)

        if len(docs) == 0:
            print("\nNo relevant information found.")
            continue

        # Return the most relevant document
        answer = docs[0].page_content

        print("\nAnswer:")
        print(answer)
        print("-" * 60)


if __name__ == "__main__":
    run_assistant()