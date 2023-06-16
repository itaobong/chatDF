# ChatDF - Chat with PDF

ChatDF is an LLM-powered chatbot application built using Streamlit, LangChain, and the OpenAI LLM model. It allows you to upload a PDF file, extract its text content, compute embeddings for the text, and perform question-answering based on user queries.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/itaobong/chatDF.git
   
2. Navigate to the project directory:
   `cd chatDF
   
3. Install the required dependencies:
   `pip install -r requirements.txt
   
4. Visit   `https://platform.openai.com/` to get your API key
   
5. Create a `.env` file in the project directory and set the required environment variables:
   `OPENAI_API_KEY=<your_openai_api_key>`

## **Usage**
1. Run the application
    ```shell
   streamlit run main.py
   
2. The application will open in your web browser. You will see the sidebar with information about the app.

3. Click on the "Upload your PDF" button to upload a PDF file.

4. Once the PDF file is uploaded, the text content will be extracted and processed.

5. Enter a question or query related to the uploaded PDF file in the text input field.

6. Click the "Ask" button to submit your question.

7. The application will compute the most relevant documents based on your query and use the OpenAI LLM model to generate a response.

8. The response will be displayed on the screen.  
9. You can ask additional questions or upload a different PDF file by repeating the steps above.


## **About**
This application utilizes the following technologies:

   - Streamlit: A Python library for building interactive web applications.
   - LangChain: A library for natural language processing tasks, including text splitting, embeddings, and question-answering.
   - OpenAI: The OpenAI LLM model, used for generating responses to user queries.

## **Contributing**
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
