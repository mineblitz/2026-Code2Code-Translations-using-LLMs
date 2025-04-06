
const fruitDistribution = (s, n) => {
  var lis = [];
  for (const i of s.split(" "))
    if (!isNaN(i))
      lis.push(Number(i))
  return n - lis.reduce(((prev, item) => prev + item), 0);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = fruitDistribution(...args);
console.log(result);