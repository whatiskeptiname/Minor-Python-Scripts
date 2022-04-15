# The function is expected to return a string.
# The function accepts string as parameter.


def logic(my_input):
    w_list = my_input.split(" ")
    new_list = []
    for my_input in w_list:
        new_list.append(convert(my_input))
        
    return " ".join(new_list)


def convert(my_input):
    if my_input == "x":
        new_string = my_input.replace("x", "ecks")
    elif my_input[0] == "x":
        replace = my_input.replace("x", "z", 1)
        new_string = replace.replace("x", "cks")
    else:
        new_string = my_input.replace("x", "cks")
        
    return new_string


# Do not edit below

# Get the input
my_input = "xx xx"

# Print output returned from the logic function
print(logic(my_input))
