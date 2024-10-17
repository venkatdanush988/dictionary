'''

1) The program takes a dictionary and checks if a given key exists in a dictionary or not. 
Problem Solution:
1. Declare and initialize a dictionary to have some key-value pairs.{'A':1,'B':2,'C':3}
2. Take a key from the user and store it in a variable.
3. Using an if statement and the in operator, check if the key is present in the dictionary using the dictionary.keys() method.
4. If it is present, print the value of the key.
5. If it isn’t present, display that the key isn’t present in the dictionary.
6. Exit.
Sample Input :
Enter key to check : A
Sample Output :
Key is present and value of the key is: 1


'''

my_dict = {'A': 1, 'B': 2, 'C': 3}

key_to_check = input("Enter key to check: ")

if key_to_check in my_dict.keys():
    # Step 4: If present, print the value of the key
    print(f"Key is present and value of the key is: {my_dict[key_to_check]}")
else:
    # Step 5: If not present, display a message
    print("Key isn't present in the dictionary.")
