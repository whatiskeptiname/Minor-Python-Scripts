# The function is expected to return a string.
# The function accepts string as parameter.


def logic(my_input):
    # Write your code here and remove pass statement
    # Don't print anything. Just return the intended output
    # You can create other functions and call from here
    vowels = ["a", "e", "i", "o", "u"]
    my_input = my_input.lower()
    final_string = ""
    for vowel in vowels:
        count = 0
        for char in my_input:
            if char == vowel:
                count += 1
        vowel_count = str(count)+vowel
        if count != 0:
            final_string = final_string + vowel_count
    return final_string


# Do not edit below

# Get the input
my_input = "Hello world, SEE this"

# Print output returned from the logic function
print(logic(my_input))
