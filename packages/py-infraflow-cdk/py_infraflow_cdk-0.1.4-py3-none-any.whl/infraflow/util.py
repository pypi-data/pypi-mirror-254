def caps_camel(s):
    return "".join([cap(word) for word in str(s).replace('_', " ").split(' ')])


def cap(word):
    return word[0].upper() + word[1:]
