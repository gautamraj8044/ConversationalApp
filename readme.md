

# Streamlit Chat GPT Demo

This is a simple Streamlit application that demonstrates how to use the Hugging Face Transformers library to create a conversational AI model using the `google/flan-t5-large` model. The app allows users to input questions and receive generated responses in real time.

## Features

- User-friendly interface for inputting questions.
- Generates answers using the `google/flan-t5-large` model.
- Session management to keep track of conversation history.

## Requirements

To run this application, you'll need the following Python packages:
```markdown
- streamlit
- transformers
- torch
- langchain
```

## Usage
 You can install the required packages using pip:


```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/gautamraj8044/ConversationalApp.git
   cd ConversationalApp
   ```

2. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to `http://localhost:8501` to access the app.

4. Type your question in the input box and click "Generate" to receive a response from the model.

## Deployment

This app can also be deployed on Hugging Face Spaces. Simply push your code to a new repository on Hugging Face, and it will automatically build and deploy the app.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.com/)



Feel free to replace the placeholder for the GitHub repository link and make any additional adjustments as needed! Let me know if there's anything else you need.