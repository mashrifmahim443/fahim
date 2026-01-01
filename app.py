import streamlit as st
from openai import OpenAI
import os

# Page configuration
st.set_page_config(
    page_title="MIST Gazipur",
    page_icon="💬",
    layout="centered"
)

# Initialize OpenAI client
@st.cache_resource
def init_openai_client():
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("💬 MIST Gazipur")
st.markdown("Ask me anything!")

# Sidebar for API key input (if not in secrets)
client = init_openai_client()
if client is None:
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Enter your OpenAI API key here"
        )
        if api_key:
            client = OpenAI(api_key=api_key)
            st.success("API key set!")
        else:
            st.warning("Please enter your OpenAI API key to use the chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    if client is None:
        st.error("Please set your OpenAI API key in the sidebar first!")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Call OpenAI API
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            *[{"role": msg["role"], "content": msg["content"]} 
                              for msg in st.session_state.messages]
                        ],
                        temperature=0.7,
                        max_tokens=500
                    )
                    
                    assistant_response = response.choices[0].message.content
                    st.markdown(assistant_response)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append(
                        {"role": "assistant", "content": assistant_response}
                    )
                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg}
                    )

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

