import streamlit as st
import re
from utils import chunks
from load_files import get_repos,get_file
from file import embeddings,model
from langchain_community.vectorstores import Chroma
from langchain.schema import Document 

st.set_page_config(layout = "wide")

st.title("Chat with GitHub Files")
st.write("**Please press \"Enter\" after entering username**")

with st.form("Form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        username = st.text_input("Enter username : ")

    with col2:     
        if username:
             repos = get_repos(username)
             repository = st.selectbox("Select repository",repos)
        else:
            repository = st.text_input("Enter repository")
        
    with col3:
        file = st.text_input("Enter file name : ")
        
    query = st.text_input("Enter your question : ") 
        
    submitted = st.form_submit_button("Submit")
    
if submitted:
    try:
    
        file_content = get_file(username,repository,file)
             
        file_extention = re.search(r'\.([a-zA-Z0-9]+)$',file)    
        
        if file_extention in ["py","js","jsx","css","ts","tsx","php","rb","go"]:
            
            code_chunks = chunks(file_content,file_extention)
        
            code_chunks = [code_chunks[chunk] for chunk in code_chunks]
            
            code_blocks = [Document(page_content = chunk) for chunk in code_chunks]
                
            vector_store = Chroma.from_documents(
                documents = code_blocks,
                embedding = embeddings,
            )
            
            relevant_data = vector_store.similarity_search(query)
        
        else:
            relevant_data = file_content
        
        response = model.generate_content(model = "gemini-2.0-flash", contents = [f"you are speaclized progammer that gives meaningful answer for the given question which is - {query} based on the given data {relevant_data}"])
        
        response = str(response.text).lower()
        
        st.write(response)
    
    except:
        if file is not "":
           st.write("No file found for the given")
