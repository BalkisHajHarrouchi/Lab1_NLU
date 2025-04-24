import os
import shutil
import subprocess
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from redundant_filter_retriever import RedundantFilterRetriever
import langchain
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms import Ollama

langchain.debug = True

# Loading the embedder
EMBEDDING_MODEL = 'Lajavaness/bilingual-embedding-large'
model_kwargs = {"trust_remote_code": True}
embedding_function = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs=model_kwargs)

# Define text splitter with chunk size and overlap
text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator="\n\n"
)

# Load and split the document
loader = TextLoader("recettes.txt")
docs = loader.load_and_split(text_splitter=text_splitter)

# Define the vector store directory
vectorstore_dir = "chef/db1"

# Check if vector store directory exists and delete it to reset
if os.path.exists(vectorstore_dir):
    shutil.rmtree(vectorstore_dir)  # Delete the directory to start fresh

# Initialize a new vector store
db = Chroma(
    persist_directory=vectorstore_dir,
    embedding_function=embedding_function
)

# Add documents to the vector store
db.add_texts(texts=[doc.page_content for doc in docs])

# Create the retriever
retriever = RedundantFilterRetriever(
    chroma=db, 
    embeddings=embedding_function
)

