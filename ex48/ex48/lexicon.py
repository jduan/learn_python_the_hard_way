def scan(str):
    DIRECTIONS = ['north', 'south', 'east', 'west', 'down', 'up',
            'left', 'right', 'back']
    VERBS = ['go', 'stop', 'kill', 'eat']
    STOP_WORDS = ['the', 'in', 'of', 'from', 'at', 'it']
    NOUNS = ['door', 'bear', 'princess', 'cabinet']

    words = str.split()
    ret = []

    for word in words:
        original_word = word
        word = word.lower()
        if word in DIRECTIONS:
            ret.append(('direction', word))
        elif word in VERBS:
            ret.append(('verb', word))
        elif word in STOP_WORDS:
            ret.append(('stop', word))
        elif word in NOUNS:
            ret.append(('noun', word))
        elif is_number(word):
            ret.append(('number', int(word)))
        else:
            ret.append(('error', original_word))
    return ret

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
