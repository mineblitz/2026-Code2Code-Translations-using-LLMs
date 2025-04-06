import ast
import sys
def get_closest_vowel(word):
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""
if __name__ == "__main__":
    n = sys.argv[1]
    result = get_closest_vowel(n)
    print(result)
