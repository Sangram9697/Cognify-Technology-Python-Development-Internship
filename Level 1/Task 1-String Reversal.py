#Function to reverse the string
def reverse_string(original_string):
    return original_string[::-1]
#To get the input from the user
original_string = input("Enter a string you want:")
#To reverse the input string using reverse_string function
reversed_string = reverse_string(original_string)
#Printing the original and reversed string
print("Original:", original_string)
print("Reversed:", reversed_string)
