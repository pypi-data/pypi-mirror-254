# cli.py
import argparse
from .scripted_art import ScriptedArt

def main():
    parser = argparse.ArgumentParser(description='Generate terminal art scripts powered by GPT-4-turbo.')
    parser.add_argument('description', type=str, help='A description of the terminal art to generate')
    args = parser.parse_args()

    scripted_art = ScriptedArt()
    art_script = scripted_art.create_art_script_openai(args.description)
    print("\nGenerating Artwork...")
    scripted_art.execute_art_script(art_script)

if __name__ == '__main__':
    main()
