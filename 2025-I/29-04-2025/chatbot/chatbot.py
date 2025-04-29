# chatbot.py
import ollama
import streamlit as st

class OllamaChatbot:
    """
    A chatbot class to interact with Ollama models using the ollama library.
    """
    def __init__(self):
        """
        Initializes the chatbot. Tries to fetch available models.
        Handles potential connection errors.
        """
        self.available_models = []
        try:
            # Attempt to list models to check connection and availability
            models_info = ollama.list()
            self.available_models = [model['name'] for model in models_info['models']]
            if not self.available_models:
                 st.warning("No models found. Make sure you have pulled models using 'ollama pull <model_name>'.")
        except Exception as e:
            st.error(f"Failed to connect to Ollama or list models. Please ensure Ollama is running. Error: {e}")
            self.available_models = [] # Ensure it's empty if connection failed

    def list_available_models(self):
        """
        Returns the list of available model names fetched during initialization.
        """
        return self.available_models

    def get_response(self, model_name, messages, stream=False):
        """
        Gets a response from the specified Ollama model.

        Args:
            model_name (str): The name of the Ollama model to use.
            messages (list): A list of message dictionaries (e.g., [{'role': 'user', 'content': '...'}, ...]).
            stream (bool): Whether to stream the response or get it all at once.

        Returns:
            If stream=False: The complete response dictionary from ollama.chat.
            If stream=True: A generator yielding chunks of the response.
            Returns None if an error occurs during the chat request.
        """
        if not model_name:
            st.error("No model selected.")
            return None
        if model_name not in self.available_models:
             st.error(f"Model '{model_name}' not found or Ollama is not running correctly. Available: {self.available_models}")
             return None

        try:
            if stream:
                # Return the generator directly for streaming
                return ollama.chat(
                    model=model_name,
                    messages=messages,
                    stream=True
                )
            else:
                # Get the complete response
                response = ollama.chat(
                    model=model_name,
                    messages=messages,
                    stream=False # Ensure stream is False for non-streaming
                )
                return response # Return the full response dictionary
        except Exception as e:
            st.error(f"Error interacting with Ollama model '{model_name}': {e}")
            return None

# Optional: Instantiate the chatbot once if needed elsewhere,
# but it's better practice to instantiate it within the Streamlit app
# to handle potential errors gracefully within the app's context.
# chatbot_instance = OllamaChatbot()
