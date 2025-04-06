
const flipCase = (string) => {
  return string.split('')
          .map(x => (x.toUpperCase() == x ? x.toLowerCase() : x.toUpperCase()))
          .join('');
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = flipCase(...args);
console.log(result);