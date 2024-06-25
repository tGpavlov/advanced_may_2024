def concatenate(*strings, **replacements):
    con_string = ''.join(strings)

    for key, value in replacements.items():

        if key in con_string:
            con_string = con_string.replace(key, value)

    return con_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
