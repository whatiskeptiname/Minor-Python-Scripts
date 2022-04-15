def logic(my_input):
    words = my_input.split(" ")
    word_list = []
    for word in words:
        word_list.append(convert(word))
    return " ".join(word_list)


def convert(word):
    new_word = ""
    new_word = word[1:] + word[0] + "arg"
    return new_word


def special_char(word):
    for i in range(len(word)):
        if word[i] in [".", ";", ":", "?", "!"]:
            pass


# Do not edit below

# Get the input
my_input = "Take what you can, give nothing back."
# Print output returned from the logic function
print(logic(my_input))
