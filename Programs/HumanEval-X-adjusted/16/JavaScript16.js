
const countDistinctCharacters = (string) => {
  return (new Set(string.toLowerCase())).size;

}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = countDistinctCharacters(...args);
console.log(result);