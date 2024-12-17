


import json
from fun import loading

def load_translations(language):
    try:
        with open(f"translation/{language}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Translation file for '{language}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in the translation file '{language}.json'.")
        return None



def get_translation(key, translations, *args):
    # If the key exists, format the string with additional arguments
    if key in translations:
        return translations[key].format(*args)
    else:
        print(f"Warning: Translation for '{key}' not found.")
        return key  # Fallback to the key itself
        


def choose_language():
    while True:
        
        print("Select Language:")
        print("1. English")
        print("2. Español")
        print("3. Indonesia")
        language_choice = input("Please choose a language: ")

        if language_choice == "1":
            return "en"
        elif language_choice == "2":
            return "es"
        elif language_choice == "3":
            return "ina"
    
        else:
            print("Invalid choice, defaulting to English.")
            loading(1)
            return "en"
        
# Ask user to select language
global tsl
tsl = load_translations(choose_language()) 
    