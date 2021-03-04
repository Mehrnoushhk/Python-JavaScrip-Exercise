def text_decorator(kind, text):
    def text_upper():
        return text.upper()
    def text_title():
        return text.title()
    if kind == 'upper':
        return text_upper
    else:
        return text_title

print(text_decorator('upper', 'hello!')())