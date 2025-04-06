
const carRaceCollision = (n) => {
  return Math.pow(n, 2);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = carRaceCollision(...args);
console.log(result);