# Simple Chatbot with Streamlit and OpenAI

A simple chatbot application built with Streamlit that uses OpenAI API to answer questions.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
   - Option 1: Create a `.streamlit/secrets.toml` file and add:
     ```
     OPENAI_API_KEY = "your-api-key-here"
     ```
   - Option 2: Set environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - Option 3: Enter it in the sidebar when running the app

## Run the App

```bash
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Add your OpenAI API key in the secrets section:
   - Go to Settings → Secrets
   - Add: `OPENAI_API_KEY = "your-api-key-here"`

## Features

- Simple chat interface
- Conversation history
- Clear chat functionality
- Error handling

