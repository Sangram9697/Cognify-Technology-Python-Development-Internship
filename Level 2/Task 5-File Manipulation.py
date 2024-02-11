def count_word_occurrences(file_path):
    word_counts = {}

    # Open the file and read its content
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase to avoid counting the same word with different cases separately
                word = word.strip('.,?!;:"\'').lower()
                # Increment the count for the word
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def display_word_counts(word_counts):
    # Sort the word counts by keys (words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])
    
    # Display the word counts
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

# Example usage:
file_path = r"C:\Users\Dell\Desktop\Cognifyz\Level 2\Python.txt"  # Provide the path to your text file
word_counts = count_word_occurrences(file_path)
display_word_counts(word_counts)
