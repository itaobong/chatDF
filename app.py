import streamlit as st
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter


#Sidebar contents
with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
        ## About

        This app is an LLm-powered chatbot built using:
        - [Streamlit](https://streamlit.io)
        - [LangChain](https://python.langchain.com/)
        - [OpenAI](htps://platform.openai.com/docs/models) LLM model

    ''')
    add_vertical_space(5)
    st.write('Made with by [Prompt Engineer](https://youtube.com/@engineerprompt)')


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
            st.write(text)



if __name__ == '__main__':
    main()