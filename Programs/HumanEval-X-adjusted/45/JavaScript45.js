
const triangleArea = (a, h) => {
  return a * h / 2.0;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = triangleArea(...args);
console.log(result);