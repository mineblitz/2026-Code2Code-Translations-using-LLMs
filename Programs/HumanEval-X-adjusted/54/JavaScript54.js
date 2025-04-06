
const sameChars = (s0, s1) => {
  return JSON.stringify([...new Set(s0)].sort()) === JSON.stringify([...new Set(s1)].sort());
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = sameChars(...args);
console.log(result);