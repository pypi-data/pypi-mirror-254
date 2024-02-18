# ScriptedSketches

ScriptedSketches is an innovative Python package that brings the power of OpenAI's GPT-4 directly to your terminal, allowing you to generate ASCII art from textual descriptions. Designed with simplicity and ease of use in mind, ScriptedSketches opens up a world of creative possibilities for both developers and artists alike.  

## Features  

- **Ease of Use**: Generate art directly from the command line.
- **Powered by GPT-4**: Leverages the latest in AI technology for detailed and accurate art.  
- **Custom Artwork**: Transforms your descriptions into unique ASCII art. 
- **On-the-Fly Creation**: Instantly renders artwork in the terminal window.

## Installation  

To get started with ScriptedSketches, install the package using pip:

```bash  
pip install scriptedsketches
```

This command will download and install ScriptedSketches along with its dependencies. Ensure you have Python 3.6 or newer, as this is required for the package to function correctly.

## Configuration   

Before using ScriptedSketches, you must obtain an API key from OpenAI and set it as an environment variable on your system. This key enables the package to communicate with OpenAI's API to generate ASCII art scripts. 

### Setting Up the OPENAI_API_KEY

**For Linux and macOS Users:**   

Open your terminal.   
Run the following command:
```
export OPENAI_API_KEY='your_openai_api_key_here'
```

To make this change permanent, add the export command to your shell's startup script, such as ~/.bashrc, ~/.zshrc, or ~/.profile.

**For Windows Users:**   

Open Command Prompt.   
Run the following command:
```
setx OPENAI_API_KEY "your_openai_api_key_here"
```

Restart Command Prompt to apply the changes.   

**Important**: Keep your API key secure and never commit it in your version-controlled files.

## Usage   

Once installed and configured, generate ASCII art by simply typing:
```
scriptedsketches "describe your image here"
```

The terminal will display the ASCII art generated based on your description.   

## How It Works   

When you run the scriptedsketches command, the package communicates with the OpenAI API, sending your descriptive prompt to be processed by the GPT-4 model. The model then returns a Python script tailored to your description, which is executed locally to render your ASCII art in the terminal.

## Contributing  

We welcome contributions to ScriptedSketches! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

- Fork the Project  
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')  
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request  

## License  

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments  

- Thanks to OpenAI for providing the GPT-4 API.  
- Hat tip to all contributors who have helped shape this project.   

## Questions or Feedback

For any questions or feedback, please contact the project maintainer at jacobglapkin@gmail.com. Your input is valuable to us! 




