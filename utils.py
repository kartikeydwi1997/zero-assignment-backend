def get_pig_latin_word(word):
    """
    Translates a word into pig latin.

    :param word: The word to translate.
    :return: The translated word in pig latin.
    """
    if word[0] in 'aeiou':
        return word + 'hey'
    else:
        vowel_index = 0
        for i in range(len(word)):
            if word[i] in 'aeiou':
                vowel_index = i
                break

        return word[vowel_index:] + word[:vowel_index] + 'ay'


def pig_latin_translate(sentence):
    """
    Translates a sentence into pig latin.

    :param sentence: The sentence to translate.
    :return: The translated sentence in pig latin.
    """
    words = sentence.split()
    translated_words = []
    for word in words:
        translated_words.append(get_pig_latin_word(word).lower())

    return ' '.join(translated_words).capitalize()