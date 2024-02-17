def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

dictionary = load_dictionary("words.txt")

def get_difference(word1, word2):
    len_word1, len_word2 = len(word1), len(word2)
    if len_word1 > len_word2:
        word1, word2 = word2, word1
        len_word1, len_word2 = len_word2, len_word1
    current_row = range(len_word1 + 1)
    for i in range(1, len_word2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_word1
        for j in range(1, len_word1 + 1):
            insert, delete, change = previous_row[j] + 1, current_row[j-1] +  1, previous_row[j-1]
            if word1[j-1] != word2[i-1]:
                change += 1 
            current_row[j]= min(insert, delete, change)
    return current_row[len_word1]

def spell_check(word, amount: int, show_distance=False):
    global dictionary
    suggestions= []

    for correct_word in dictionary:
        distance = get_difference(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    suggestions = suggestions[:amount]

    if not show_distance:
        suggestions_placeholder = suggestions
        suggestions = []
        for word in suggestions_placeholder:
            suggestions.append(word[0])

    return suggestions

def correct_word(word):
    return spell_check(word, 1)

def correct_sentance(sentance):
    global dictionary
    sentance_split = sentance.split(' ')
    new_sentance_list = []
    for i in sentance_split:
        suggestions = spell_check(i, 1)
        new_sentance_list += [suggestions[0]]
    new_sentance = ' '.join(new_sentance_list)
    return new_sentance