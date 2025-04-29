# main_app.py
import streamlit as st
from chatbot import OllamaChatbot # Import the chatbot class

# --- Page Configuration ---
st.set_page_config(
    page_title="Ollama Chatbot Dashboard",
    page_icon="🤖",
    layout="wide"
)

# --- Initialize Chatbot ---
# Instantiate the chatbot here so Streamlit can handle errors during app load
try:
    chatbot = OllamaChatbot()
    available_models = chatbot.list_available_models()
except Exception as e:
    # If OllamaChatbot() itself fails (e.g., cannot connect at all)
    st.error(f"Failed to initialize the chatbot. Is Ollama running? Error: {e}")
    chatbot = None # Set chatbot to None if initialization fails
    available_models = []

# --- Sidebar ---
with st.sidebar:
    st.title("Settings")
    st.markdown("Select the Ollama model you want to chat with.")

    # Model Selection
    if chatbot and available_models: # Only show selector if chatbot initialized and models exist
        selected_model = st.selectbox(
            "Choose Ollama Model:",
            options=available_models,
            key="selected_model",
            index=available_models.index(st.session_state.get("selected_model", available_models[0])) if st.session_state.get("selected_model") in available_models and available_models else 0 # Pre-select if possible
        )
        # Store the selection in session state immediately
        st.session_state["selected_model"] = selected_model
    elif not chatbot:
         st.warning("Chatbot could not be initialized. Check Ollama status.")
    else: # Chatbot initialized but no models found
        st.warning("No Ollama models found. Please pull a model (e.g., `ollama pull llama3`).")
        st.session_state["selected_model"] = None # Ensure no model is selected


    # Streaming Option
    use_streaming = st.toggle("Stream Response", value=True, key="use_streaming")

    # Clear Chat Button
    if st.button("Clear Chat History", key="clear_chat"):
        st.session_state.messages = []
        st.success("Chat history cleared!")
        st.rerun() # Rerun to reflect the cleared messages

# --- Main Chat Interface ---
st.title("🤖 Ollama Chatbot Dashboard")
st.caption(f"Using model: {st.session_state.get('selected_model', 'None Selected')}")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle chat input from the user
if prompt := st.chat_input("What can I help you with?"):
    # Ensure a model is selected before proceeding
    if not st.session_state.get("selected_model") or not chatbot:
        st.warning("Please select a valid model from the sidebar or ensure Ollama is running.")
    else:
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response from the chatbot
        with st.chat_message("assistant"):
            try:
                if use_streaming:
                    response_stream = chatbot.get_response(
                        st.session_state.selected_model,
                        st.session_state.messages,
                        stream=True
                    )
                    if response_stream:
                        # Use st.write_stream for generators/iterators
                        full_response = st.write_stream(
                            (chunk['message']['content'] for chunk in response_stream if 'message' in chunk and 'content' in chunk['message'])
                        )
                        # Add the complete streamed response to history
                        st.session_state.messages.append({"role": "assistant", "content": full_response})
                    else:
                        # Handle cases where get_response returned None (error displayed already)
                         st.warning("Could not get response from model.")


                else: # Non-streaming
                    response_data = chatbot.get_response(
                        st.session_state.selected_model,
                        st.session_state.messages,
                        stream=False
                    )
                    if response_data and 'message' in response_data and 'content' in response_data['message']:
                        full_response = response_data['message']['content']
                        st.markdown(full_response)
                        # Add the complete response to history
                        st.session_state.messages.append({"role": "assistant", "content": full_response})
                    else:
                         # Handle cases where get_response returned None or unexpected format
                         st.warning("Could not get response from model or response format was unexpected.")

            except Exception as e:
                st.error(f"An error occurred during chat generation: {e}")


# --- Instructions/Notes ---
st.sidebar.markdown("---")
st.sidebar.markdown("### Notes:")
st.sidebar.markdown("- Ensure Ollama is running locally.")
st.sidebar.markdown("- Ensure you have pulled the desired models (`ollama pull <model_name>`).")
st.sidebar.markdown("- Select a model from the dropdown to start chatting.")
