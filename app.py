import streamlit as st
import os
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback


#Sidebar contents
with st.sidebar:
    st.title('Welcome to ChatDF \n An LLM Chat App')
    st.markdown('''
        ## About

        This app is an LLM-powered chatbot built using:
        - [Streamlit](https://streamlit.io)
        - [LangChain](https://python.langchain.com/)
        - [OpenAI](htps://platform.openai.com/docs/models) LLM model

    ''')
    add_vertical_space(5)
    st.write('Made  by [Itaobong](https://github.com/itaobong/chatDF)')

load_dotenv()

def main():
    st.header("Chat with PDF")

    

    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        # st.write(pdf_reader)

        text =""
        for page in pdf_reader.pages:
            text +=page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        chunks= text_splitter.split_text(text=text)

        
        store_name =pdf.name[:-4]


        #embeddings
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl","rb") as f:
                VectorStore=pickle.load(f)
            st.write('Embeddings loaded from the disk')
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks,embeddings)
            with open(f"{store_name}.pkl","wb") as f:
                pickle.dump(VectorStore,f)
            st.write('Embeddings computations completed')

        # Accept user question/query
        query=st.text_input("Ask questions relating to your uploaded PDF file")
        if query:
            docs=VectorStore.similarity_search(query=query, k=3)

            llm=OpenAI(temperature=0)
            chain=load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response =chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)

        # st.write(chunks)




if __name__ == '__main__':
    main()