
const pluck = (arr) => {
  if (arr.length == 0) return [];
  var evens = arr.filter(x => x % 2 == 0);
  if (evens.length == 0) return [];
  return [Math.min(...evens), arr.indexOf(Math.min(...evens))];
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = pluck(...args);
console.log(result);