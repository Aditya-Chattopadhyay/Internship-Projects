def word_count(text):
    # Split the text into words
    words = text.split()
    # Return the count of words
    return len(words)

def main():
    print("Welcome to the Word Counter program!")
    
    # Prompt user for input
    text = input("Please enter a sentence or paragraph: ")
    
    # Check for empty input
    if not text.strip():
        print("Error: Empty input! Please enter some text.")
        return
    
    # Call word_count function to count words
    count = word_count(text)
    
    # Display the word count
    print(f"Word count: {count}")

if __name__ == "__main__":
    main()
