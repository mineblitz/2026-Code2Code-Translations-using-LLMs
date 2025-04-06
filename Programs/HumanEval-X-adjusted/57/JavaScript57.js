
const monotonic = (l) => {
  var sort1 = [...l].sort((a, b) => a - b);
  var sort2 = [...l].sort((a, b) => b - a);
  if (JSON.stringify(l) === JSON.stringify(sort1) ||
      JSON.stringify(l) === JSON.stringify(sort2))
    return true;
  return false;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = monotonic(...args);
console.log(result);