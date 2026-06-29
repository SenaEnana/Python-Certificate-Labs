def pin_extractor(poems):
    secret_codes = []

    for poem in poems:
        secret_code = ""
        lines = poem.split("\n")

        for line_index, line in enumerate(lines):
            words = line.split()

            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"

        secret_codes.append(secret_code)

    return secret_codes


poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = """The grass is green
here and there
hoping for rain
before it turns yellow"""

poem3 = """There
once
was
a
dragon"""

print(pin_extractor([poem, poem2, poem3]))