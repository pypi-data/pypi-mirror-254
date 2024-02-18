from .code_generation import GPT4TurboCaller  # Ensure GPT4TurboCaller is in the file gpt4_turbo_caller.py
from .prompt_templates import Prompts
import json

class ScriptedArt:
    """
    The ScriptedArt class interfaces with the GPT-4-turbo model to generate
    Python scripts for creating ASCII art based on user descriptions.
    """
    
    def __init__(self):
        """
        Initializes the ScriptedArt object with a GPT4TurboCaller instance.
        """
        # Instance of the class to call GPT-4-turbo model.
        self.gpt4_caller = GPT4TurboCaller()

    def create_art_script_openai(self, description):
        """
        Generates a Python script for ASCII art creation based on a user-provided description.
        
        Parameters:
        - description (str): A text description of the desired ASCII art.
        
        Returns:
        - str: A Python code script that, when executed, prints ASCII art.
        """
        # Format the user's description into a prompt template for the model.
        formatted_user_prompt = Prompts.UserPromptOpenai.format(description)
        
        # Generate a response from the GPT-4-turbo model based on the formatted prompt.
        python_code = self.gpt4_caller.generate_chat_response(Prompts.SystemPromptOpenai, formatted_user_prompt)
        
        # Convert the generated code (in JSON format) to a Python dictionary.
        json_converter = json.loads(python_code)
        
        # Return the Python code as a string, if available.
        return json_converter.get("Python_code", None)

    def execute_art_script(self, python_code):
        """
        Executes a Python script to render ASCII art in the terminal.

        Parameters:
        - python_code (str): A string containing the Python code to execute.
        """
        try:
            # Execute the Python code string to render the ASCII art.
            exec(python_code)
            
        except Exception as e:
            # Print an error message if something goes wrong during the execution.
            print(f"Apologies, an error has occurred while generating artwork: {e}")
