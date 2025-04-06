
const countUpper = (s) => {
  let p = 0
  for (let i = 0; i < s.length; i += 2) {
    if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') { p++ }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = countUpper(...args);
console.log(result);