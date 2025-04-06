
const vowelsCount = (s) => {
  var vowels = "aeiouAEIOU";
  var n_vowels = s.split('').reduce((prev, item) => {
    return prev + (vowels.includes(item));
  }, 0);
  if (s.at(-1) == 'y' || s.at(-1) == 'Y')
    n_vowels += 1;
  return n_vowels;
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = vowelsCount(...args);
console.log(result);