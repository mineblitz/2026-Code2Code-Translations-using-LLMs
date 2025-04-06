
const smallestChange = (arr) => {
  var ans = 0;
  for (let i = 0; i < Math.floor(arr.length / 2); i++)
    if (arr[i] != arr.at(-i - 1))
      ans++;
  return ans;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = smallestChange(...args);
console.log(result);