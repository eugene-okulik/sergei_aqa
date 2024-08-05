text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

part_of_word = 'ing'

words = text.split()
fin_words = []
for word in words:
        if word.endswith('.'):
                new_word = word.replace('.', '')
                fin_word = f'{new_word}{part_of_word}.'
        elif word.endswith(','):
                new_word = word.replace(',', '')
                fin_word = f'{new_word}{part_of_word},'
        else:
                fin_word = f'{word}{part_of_word}'

        fin_words.append(fin_word)

print(' '.join(fin_words))
