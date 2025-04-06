
const howManyTimes = (string, substring) => {
  var times = 0;
  for (let i = 0; i < string.length - substring.length + 1; i++) {
    if (string.slice(i, i+substring.length) == substring) {
      times += 1;
    }
  }
  return times;
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = howManyTimes(...args);
console.log(result);