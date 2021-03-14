
def count_words(text):
    text_list = text.lower().split(' ')
    text_dict = {}
    for word in text_list:
        if word in text_dict:
            text_dict[word] = text_dict[word] + 1
        else:
            text_dict[word] = 1
    return text_dict

print(count_words("Oh what a day what A lovely day"))


