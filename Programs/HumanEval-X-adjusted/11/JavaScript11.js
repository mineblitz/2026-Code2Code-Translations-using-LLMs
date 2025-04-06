
const stringXor = (a, b) => {
  var xor = function (i, j) {
    if (i == j)
      return '0';
    else
      return '1';
  }
  return a.split('').map((item, index) => xor(item, b[index])).join('');
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = stringXor(...args);
console.log(result);