from collections import Counter

text = 'Word Counter is a tool that provides an extensive statistics about the number of words, characters, characters without spaces... This tool also reports the number of syllables, monosyllabic words, polysyllabic words, sentences, paragraphs, unique words, short words, long words, ...'
print(Counter(text.split()).most_common(10))
print(Counter(text).most_common(10))
