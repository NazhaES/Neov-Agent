from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

pdf_loader = DirectoryLoader("docs", glob="*.pdf", loader_cls=PyPDFLoader)
documents = pdf_loader.load()

embeddings = OpenAIEmbeddings (
    model= "text-embedding-3-small"
)

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Documents successfully stored in ChromaDB!")