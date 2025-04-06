
const getClosestVowel = (word) => {
  for (let i = word.length - 2; i > 0; i--) {
    if (
      !(word[i] != 'a' && word[i] != 'e' && word[i] != 'i' && word[i] != 'o' && word[i] != 'u' && word[i] != 'A' &&
        word[i] != 'U' && word[i] != 'O' && word[i] != 'I' && word[i] != 'E')
      &&
      (word[i + 1] != 'a' && word[i + 1] != 'e' && word[i + 1] != 'i' && word[i + 1] != 'o' && word[i + 1] != 'u' && word[i + 1] != 'A' &&
        word[i + 1] != 'U' && word[i + 1] != 'O' && word[i + 1] != 'I' && word[i + 1] != 'E')
      &&
      (word[i - 1] != 'a' && word[i - 1] != 'e' && word[i - 1] != 'i' && word[i - 1] != 'o' && word[i - 1] != 'u' && word[i - 1] != 'A' &&
        word[i - 1] != 'U' && word[i - 1] != 'O' && word[i - 1] != 'I' && word[i - 1] != 'E')
    ) {
      return word[i]
    }
  }
  return ''
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = getClosestVowel(...args);
console.log(result);