
const rescaleToUnit = (numbers) => {
  var min_number = Math.min(...numbers);
  var max_number = Math.max(...numbers);
  return numbers.map(x => (x - min_number) / (max_number - min_number));
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = rescaleToUnit(...args);
console.log(result);