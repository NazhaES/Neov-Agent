import streamlit as st
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma


load_dotenv()


CHROMA_PATH = "chroma_db"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

st.title("AI-Powered NEOV Search")
st.write("Ask questions about NEOV, and I'll answer based on the stored data.")

# User query input
user_query = st.text_input("Enter your question:")

if st.button("Search"):
    if user_query:
        # st.write("Searching ChromaDB...")
        results = vectorstore.similarity_search(user_query)
        retrieved_text = results[0].page_content if results else "No relevant data found."
        
        client = OpenAI()
        
        system_prompt = f"""
        You are a helpful assistant. You answer questions about NEOV. 
        But you only answer based on knowledge I'm providing you. You don't use your internal 
        knowledge and you don't make things up.
        If you don't know the answer, just say: I don't know.
        --------------------
        The data:
        {retrieved_text}
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}    
            ]
        )

        st.subheader("AI Response:")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a query.")