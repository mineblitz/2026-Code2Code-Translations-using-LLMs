
const search = (lst) => {
  var frq = new Array(Math.max(...lst) + 1).fill(0);
  for (const i of lst)
    frq[i] += 1;
  var ans = -1;
  for (let i = 1; i < frq.length; i++)
    if (frq[i] >= i)
      ans = i;
  return ans;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = search(...args);
console.log(result);