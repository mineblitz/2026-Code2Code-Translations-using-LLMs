
const unique = (l) => {
  return Array.from(new Set(l)).sort((a, b) => (a - b));
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = unique(...args);
console.log(result);