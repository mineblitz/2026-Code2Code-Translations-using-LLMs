
const common = (l1, l2) => {
  var ret = new Set();
  for (const e1 of l1)
    for (const e2 of l2)
      if (e1 == e2)
        ret.add(e1);
  return [...ret].sort();
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = args[1].replace(/'/g, '"');
args[1] = JSON.parse(args[1]);
// Call the function and print the result
const result = common(...args);
console.log(result);