
const exchange = (lst1, lst2) => {
  let k = lst1.length
  let t = 0
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 == 0) { t++ }
  }
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 0) { t++ }
  }
  if (t >= k) { return 'YES' }
  return 'NO'
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = args[1].replace(/'/g, '"');
args[1] = JSON.parse(args[1]);
// Call the function and print the result
const result = exchange(...args);
console.log(result);