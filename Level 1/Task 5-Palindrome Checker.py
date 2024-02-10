def is_Palindrome(str):
    # Remove whitespace and convert to lowercase
    str = str.lower()
    # Check if the string is equal to its reverse and display the message
    if(str==str[::-1]):
        print(str+" is a palindrome.") 
    else:
        print(str+" is not a palindrome.") 
 
#Get the input from the user
str = input ("Enter a string you want: ") 
is_Palindrome(str)
