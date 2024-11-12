import random
import string

# Lists of possible word categories for username generation
animals = ["wolf", "lion", "tiger", "eagle", "bear", "shark", "panther", "dragon", "phoenix", "elephant"]
colors = ["blue", "red", "green", "yellow", "black", "white", "purple", "orange", "pink", "gray"]
fantasy = ["wizard", "knight", "sorcerer", "elf", "druid", "vampire", "troll", "goblin", "golem", "fairy"]
nature = ["forest", "river", "mountain", "desert", "ocean", "sky", "cloud", "storm", "flame", "earth"]

# Combine all word categories into a master list
categories = {
    'animals': animals,
    'colors': colors,
    'fantasy': fantasy,
    'nature': nature
}

# Function to generate a random word based on the selected category
def get_random_word(category):
    if category in categories:
        return random.choice(categories[category])
    else:
        raise ValueError("Invalid category. Choose from 'animals', 'colors', 'fantasy', or 'nature'.")

# Function to generate a random number string
def generate_number_part(min_length, max_length):
    return ''.join(random.choices(string.digits, k=random.randint(min_length, max_length)))

# Function to generate a random special character string
def generate_special_characters(num_special_chars):
    special_chars = "!@#$%^&*()_+-=~`[]{}|;:,.<>?/"
    return ''.join(random.choices(special_chars, k=num_special_chars))

# Function to generate the username
def generate_username(category, min_number_length=2, max_number_length=4, num_special_chars=0, case='mixed', prefix='', suffix=''):
    # Get a random word from the selected category
    word = get_random_word(category)
    
    # Generate a random number part
    number_part = generate_number_part(min_number_length, max_number_length)
    
    # Generate random special characters if required
    special_part = generate_special_characters(num_special_chars)
    
    # Combine parts to form the base of the username
    base_username = word + number_part + special_part
    
    # Apply the case to the username
    if case == 'upper':
        base_username = base_username.upper()
    elif case == 'lower':
        base_username = base_username.lower()
    # 'mixed' is the default and does nothing
    
    # Add prefix and suffix if provided
    final_username = prefix + base_username + suffix
    
    return final_username

if __name__ == "__main__":
    print("Welcome to the Advanced Username Generator!")
    
    # Get user input for customization options
    category = input("Choose a category (animals, colors, fantasy, nature): ").lower()
    min_number_length = int(input("Enter minimum number length (2 recommended): "))
    max_number_length = int(input("Enter maximum number length (4 recommended): "))
    num_special_chars = int(input("Enter number of special characters (0 recommended): "))
    case = input("Choose the case (upper, lower, mixed): ").lower()
    prefix = input("Enter a prefix for the username (optional): ")
    suffix = input("Enter a suffix for the username (optional): ")
    
    # Validate inputs
    if category not in categories:
        print("Invalid category. Please choose one of the following: 'animals', 'colors', 'fantasy', 'nature'.")
    else:
        # Generate and print the username
        username = generate_username(category, min_number_length, max_number_length, num_special_chars, case, prefix, suffix)
        print(f"Generated username: {username}")
