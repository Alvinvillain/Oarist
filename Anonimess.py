import itertools
from pyfiglet import Figlet

# Function to generate wordlists
def generate_wordlists(characters, min_length, max_length):
    wordlists = []
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            wordlists.append(''.join(combination))
    return wordlists

# Function to print ASCII art
def print_ascii_art(text):
    figlet = Figlet(font='slant')
    ascii_art = figlet.renderText(numbers)
    print(ascii_art)

# Main function
def main():
    print_ascii_art("OAR")
    
    characters = input("Enter characters to include in the wordlist: ")
    include_numbers = input("Include numbers (0-9)? (yes/no): ").strip().lower()

    if include_numbers == 'yes':
        characters += '0123456789'
    
    min_length = int(input("Enter minimum length of words: "))
    max_length = int(input("Enter maximum length of words: "))

    wordlists = generate_wordlists(characters, min_length, max_length)
    
    # Save to a file
    with open("wordlist.txt", "w") as f:
        for word in wordlists:
            f.write(word + "\n")
    
    print(f"Wordlist generated and saved to wordlist.txt. Total words: {len(wordlists)}")

if __name__ == "__main__":
    main()
