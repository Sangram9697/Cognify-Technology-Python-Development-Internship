def generate_fibonacci_sequence(terms):
    # Initialize the first two terms of the sequence
    fibonacci_sequence = [0, 1]
    
    # Generate subsequent terms of the sequence
    for i in range(2, terms):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate and display the Fibonacci sequence
fibonacci_sequence = generate_fibonacci_sequence(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fibonacci_sequence)
