
const sumProduct = (numbers, int) => {
  var sum_value = 0, prod_value = 1;
  for (const n of numbers) {
    sum_value += n;
    prod_value *= n;
  }
  return [sum_value, prod_value];
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = sumProduct(...args);
console.log(result);