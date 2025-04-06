
const strlen = (string) => {
  return string.length;
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = strlen(...args);
console.log(result);