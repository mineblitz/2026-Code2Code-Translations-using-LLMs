
const intersperse = (numbers, delimeter) => {
  if (!Array.isArray(numbers) || numbers.length == 0)
    return [];
  var result = [];
  for (const n of numbers) {
    result.push(n, delimeter);
  }
  result.pop();
  return result;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = intersperse(...args);
console.log(result);