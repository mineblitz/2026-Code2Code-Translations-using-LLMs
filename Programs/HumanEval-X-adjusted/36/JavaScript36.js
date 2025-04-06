
const fizzBuzz = (n) => {
  var ns = [], ans = 0;
  for (let i = 0; i < n; i++)
    if (i % 11 == 0 || i % 13 == 0)
      ns.push(i);
  var s = ns.map(x => x.toString()).join('');
  for (const c of s)
    ans += (c == '7');
  return ans;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = fizzBuzz(...args);
console.log(result);