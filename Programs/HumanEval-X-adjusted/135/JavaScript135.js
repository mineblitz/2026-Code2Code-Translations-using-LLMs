
const canArrange = (arr) => {
  if (arr.length == 0) { return -1 }
  for (let i = arr.length - 1; i > 0; i--) {
    if (arr[i] < arr[i - 1]) { return i }
  }
  return -1
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = canArrange(...args);
console.log(result);