def get_last_letter(s):

    max_char = ''
    result = ''

    if s is None or s.isnumeric():
        return 'Invalid Input'

    for char in s:
        if char.isalpha():
            if char.lower() > max_char:
                max_char = char.lower()
                result = char
    return result


print(get_last_letter("aBc"))
print(get_last_letter("Hello World!"))
print(get_last_letter("The quick brown fox jumped over the lazy dog."))
print(get_last_letter("12345"))