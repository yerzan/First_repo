def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        return " " * spaces + string + " " * spaces

formatted_string = format_string("Hello", 50)
print(formatted_string)
