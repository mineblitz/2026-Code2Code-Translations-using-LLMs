
const meanAbsoluteDeviation = (numbers) => {
  var mean = numbers.reduce((prev, item) => {
    return prev + item;
  }, 0) / numbers.length;
  return numbers.reduce((prev, item) => {
    return prev + Math.abs(item - mean);
  }, 0) / numbers.length;

}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = meanAbsoluteDeviation(...args);
console.log(result);