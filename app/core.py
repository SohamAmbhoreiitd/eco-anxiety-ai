
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Note: The sys.path.append lines are no longer needed
# if you run the script from the main 'eco-anxiety-ai' folder.

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
# --- Make sure these imports are at the top ---
from langchain_groq import ChatGroq # MODIFIED
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.config import GROQ_API_KEY # MODIFIED
# --- Constants ---
KNOWLEDGE_BASE_DIR = "knowledge_base"
CHROMA_PERSIST_DIR = "chroma_db"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

def create_vector_db():
    """
    Creates and persists a vector database from documents in the knowledge base.
    """
    # ... (This function remains unchanged) ...
    print("--- Starting Vector DB creation ---")
    loader = DirectoryLoader(KNOWLEDGE_BASE_DIR, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    if not documents:
        print("No documents found. Aborting.")
        return
    print(f"Loaded {len(documents)} document(s).")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    print(f"Split documents into {len(texts)} chunks.")
    print(f"Loading embedding model: {EMBEDDING_MODEL_NAME}...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    print(f"Creating and persisting vector store to '{CHROMA_PERSIST_DIR}'...")
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=CHROMA_PERSIST_DIR
    )
    vectordb.persist()
    print("--- Vector DB creation complete! ---")


# --- REPLACE your old function with this new one ---
def get_chat_response(query: str) -> str:
    """
    Queries the vector database and generates a response using Groq.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectordb = Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=embeddings
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    prompt_template = """
    You are an empathetic and supportive AI assistant for counseling on eco-anxiety. 
    Your role is to provide compassionate, psychologically-informed support based ONLY on the provided context.
    Do not use any information outside of the context. If the answer is not in the context, say that you don't have information on that topic.
    Be kind, reassuring, and focus on validating the user's feelings and suggesting actionable, mindful steps from the text.
    
    Context: {context}
    
    Question: {question}
    
    Supportive Answer:
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # --- THIS IS THE MAIN CHANGE ---
    # Initialize the Groq LLM with a powerful open-source model
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-8b-8192", # Or "mixtral-8x7b-32768"
        temperature=0.7
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": PROMPT}
    )

    response = qa_chain.invoke({"query": query}) # Use .invoke() instead of .__call__
    return response["result"]

# --- This block runs when you execute the script directly ---
if __name__ == '__main__':
    # We don't need to create the database again, so this is commented out.
    # create_vector_db() 

    print("Chatbot is ready. Let's test the response with Groq.")

    # This is the question we will ask our chatbot.
    test_query = "I feel guilty about the environment. What can I do?"

    print(f"\nQuery: '{test_query}'")
    print("---")

    # This line actually calls the function to get a response.
    response = get_chat_response(test_query)

    print("AI Response:")
    print(response)
    print("---")