
const median = (l) => {
  l.sort((a, b) => a - b);
  var len = l.length;
  if (l.length % 2 == 1)
    return l[Math.floor(len / 2)];
  else
    return (l[len / 2 - 1] + l[len / 2]) / 2.0;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = median(...args);
console.log(result);