
const rightAngleTriangle = (a, b, c) => {
  return (a * a + b * b == c * c || a * a == b * b + c * c || b * b == a * a + c * c)
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
args[2] = parseInt(args[2]);
// Call the function and print the result
const result = rightAngleTriangle(...args);
console.log(result);