
const correctBracketing = (brackets) => {
  var depth = 0;
  for (const b of brackets) {
    if (b == "<")
      depth += 1;
    else
      depth -= 1;
    if (depth < 0)
      return false;
  }
  return depth == 0;
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = correctBracketing(...args);
console.log(result);