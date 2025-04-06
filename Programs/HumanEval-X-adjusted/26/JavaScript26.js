
const removeDuplicates = (numbers) => {
  var dict = new Object();
  for (const num of numbers) {
    if (num in dict) {
      dict[num] += 1;
    } else {
      dict[num] = 1;
    }
  }
  return numbers.filter(x => dict[x] <= 1);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = removeDuplicates(...args);
console.log(result);