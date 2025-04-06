const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  if (string == '')
    return '';
  var beginning_of_suffix = 0;
  while (!isPalindrome(string.slice(beginning_of_suffix)))
    beginning_of_suffix += 1;
  return string + string.slice(0, beginning_of_suffix).split('').reverse().join('');
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = makePalindrome(...args);
console.log(result);