
const addElements = (arr, k) => {
  let p = 0
  for (let i = 0; i < k; i++) {
    if (arr[i] < 100 && arr[i] > -100) { p += arr[i] }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = addElements(...args);
console.log(result);