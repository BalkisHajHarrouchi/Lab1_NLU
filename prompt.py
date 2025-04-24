from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
import torch

from redundant_filter_retriever import RedundantFilterRetriever
import langchain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Enable debug mode for LangChain
langchain.debug = True

# Check if GPU is available and set device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Loading the embedder
EMBEDDING_MODEL = 'Lajavaness/bilingual-embedding-large'
embedding_function = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL,
    model_kwargs={
        "trust_remote_code": True,
        "device": device
    }
)

# Load the LLM
model = Ollama(model="llama3.2:1b",temperature=0.1)

# Initialize Chroma vector store
db = Chroma(
    persist_directory="chef/db1",
    embedding_function=embedding_function
)

# Define the chat prompt template
chat_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "Tu es un assistant culinaire expert, conçu pour aider les utilisateurs à cuisiner facilement à la maison. "
        "Ton objectif est de leur proposer des recettes adaptées à leurs besoins : ingrédients disponibles, régime alimentaire, temps de préparation ou niveau de difficulté. "
        "Utilise uniquement le contexte fourni pour formuler une réponse claire, pratique et engageante. Si les informations sont insuffisantes, réponds simplement : 'Je ne sais pas'.\n\n"
        "Contexte :\n"
        "{context}\n\n"
        "Question :\n"
        "{question}\n\n"
        "Réponse :"
    )

)

# Create the retriever with Chroma and HuggingFaceEmbeddings instances
retriever = RedundantFilterRetriever(
    chroma=db,
    embeddings=embedding_function
)

# Create the RetrievalQA chain
chain = RetrievalQA.from_chain_type(
    llm=model,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True,
    chain_type_kwargs={"prompt": chat_prompt},
    verbose=True
)

# Retrieve all documents with their metadata and embeddings
all_docs = db.get()

# Check if the vector store is empty
if len(all_docs['documents']) == 0:
    print("The vector store is empty.")
else:
    for i, doc in enumerate(all_docs['documents']):
        print(f"\nDocument {i + 1}:")
        print("Content:", doc)
        if all_docs['metadatas']:
            print("Metadata:", all_docs['metadatas'][i])
        else:
            print("No metadata found.")

# Uncomment to run the chain
while True:
    question = input(">> ")
    result = chain({"query": question})
    print(result["result"])
