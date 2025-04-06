
const closestInteger = (value) => {
  value = Number(value)
  let t = value % 1
  if (t < 0.5 && t > -0.5) { value -= t }
  else { value += t }
  return value
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = closestInteger(...args);
console.log(result);