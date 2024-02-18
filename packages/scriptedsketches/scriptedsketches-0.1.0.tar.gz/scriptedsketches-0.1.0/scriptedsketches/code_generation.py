from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class GPT4TurboCaller:
    """
    The GPT4TurboCaller class handles communication with the OpenAI API using the GPT-4-turbo model.

    This class is designed to send prompts to the GPT-4-turbo model and retrieve the generated responses.
    It encapsulates the API key management and the logic for constructing and sending requests.
    
    Attributes:
        api_key (str): The API key for authenticating with the OpenAI API, loaded from environment variables.
        client (OpenAI): An instance of the OpenAI client configured with the API key.
    """

    def __init__(self):
        """
        Initializes the GPT4TurboCaller instance, setting up the API key and OpenAI client.
        """
        # The API key for the OpenAI service, retrieved from environment variables.
        self.api_key = os.getenv("OPENAI_API_KEY")
        # The OpenAI API client instance, used to make requests to the service.
        self.client = OpenAI()

    def generate_chat_response(self, system_prompt, user_prompt, temp=0.5):
        """
        Generates a chat response from the GPT-4-turbo model based on a system prompt and a user prompt.

        Parameters:
            system_prompt (str): The prompt defining the role and capabilities of the AI.
            user_prompt (str): The user's input or question for the AI.
            temp (float): The temperature setting for the AI's creativity. Lower values mean less randomness.

        Returns:
            str: The content of the message from the AI's response.
        """
        # Send a chat completion request to the OpenAI API using the provided prompts and temperature.
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ], 
            temperature=temp
        )
        # Return the AI's response content.
        return response.choices[0].message.content
