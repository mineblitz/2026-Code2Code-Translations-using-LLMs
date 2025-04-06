
const circularShift = (x, shift) => {
  s = x.toString();
  if (shift > s.length)
    return s.split('').reverse().join('');
  else
    return s.slice(-shift) + s.slice(0, -shift);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = circularShift(...args);
console.log(result);