
const isPalindrome = (text) => {
  for (let i = 0; i < text.length; i++)
    if (text[i] != text.at(-i-1))
      return false;
  return true;
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = isPalindrome(...args);
console.log(result);