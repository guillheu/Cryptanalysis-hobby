import sys
import re

def input_int(min=0, max=sys.maxsize):
    if min >= max:
        raise ValueError("min must be smaller than max.")
    
    while True:
        try:
            user_input = int(input(f"Enter an integer between {min} (included) and {max} (excluded): "))
            if min <= user_input < max:
                return user_input
            else:
                print(f"Error: The number must be between {min} and {max}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def input_text_strict(max=None):
    if max is not None and max <= 0:
        raise ValueError("Max must be a positive integer or None.")
    
    # Regex to allow only non-accented letters and punctuation
    pattern = re.compile(r'^[a-zA-Z\s,.!?;:()-]*$')
    
    while True:
        user_input = input("Please enter some text (letters and basic punctuation only, no accents): ")
        if (max is not None and len(user_input) >= max):
            print(f"Error: The text must be shorter than {max} characters.")
        elif not pattern.match(user_input):
            print("Invalid input. Only non-accented letters and basic punctuation are allowed.")
        else:
            # Strip out punctuation from the validated input before returning it
            cleaned_input = re.sub(r'[,.!?;:()-]', '', user_input)  # Removing punctuation
            cleaned_input = re.sub(r'\s+', '', cleaned_input)
            return cleaned_input.strip().upper()
