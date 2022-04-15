import re


string = "I say what I mean. I mean what I say. I do susan."

search_word = "i"

SENTENCES = re.split(r' *[\.\?!][\'"\)\]]* *', string)
DICT = {}
LIST = string.split(".")
WORDS = list(set(string.lower().replace(".", "").split()))
LIST = [set((x.lower()).split()) for x in LIST]

for i in range(len(LIST)):
    for item in WORDS:
        if item in LIST[i]:
            DICT.setdefault(item, []).append(i)

for value in DICT[search_word]:
    print(SENTENCES[value])
