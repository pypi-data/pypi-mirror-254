<img scr='https://github.com/vertmit/pyspell/assets/132244922/430f888d-e332-4f9c-bf55-72554f0894e0' alt='PySpell'>
<br>

# PySpell
PySpell provides functionality for spell checking and sentence correction. It uses a dictionary of words and the Levenshtein distance algorithm to suggest corrections.

## Functions

### load_dictionary(file_path)
This function loads a dictionary from a text file. Each line in the file should contain a single word.

### get_difference(word1, word2)
This function calculates the Levenshtein distance between two words. The Levenshtein distance is a measure of the difference between two sequences of words.

### spell_check(word, amount: int, show_distance=False)
This function checks the spelling of a word and suggests corrections. The number of suggestions is determined by the `amount` parameter. If `show_distance` is set to True, the function will also return the Levenshtein distance for each suggestion.

### correct_word(word)
This function returns the most likely correction for a word.

### correct_sentence(sentence)
This function corrects all the words in a sentence and returns the corrected sentence.

## Usage

First, load the dictionary:

```python
# Optional
dictionary = load_dictionary("words.txt")

# Then, you can check the spelling of a word:
print(spell_check("helo", 5)) # It will give the top 5 closest words

# Or correct a sentence:
print(correct_sentence("helo wrld"))
```