
const allPrefixes = (string) => {
  var result = [];
  for (let i = 0; i < string.length; i++) {
    result.push(string.slice(0, i+1));
  }
  return result;
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = allPrefixes(...args);
console.log(result);