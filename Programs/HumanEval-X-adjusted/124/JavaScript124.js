
const validDate = (date) => {
  let t = date.split(/-/)
  if (t.length != 3) { return false }
  if (t[0] < 1 || t[0] > 12 || t[1] < 1) { return false }
  if (t[0] == 2 && t[1] > 29) { return false }
  if ((t[0] == 1 || t[0] == 3 || t[0] == 5 || t[0] == 7 || t[0] == 8 || t[0] == 10 || t[0] == 12) && t[1] > 31) { return false }
  if ((t[0] == 4 || t[0] == 6 || t[0] == 9 || t[0] == 11) && t[1] > 30) { return false }
  return true
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = validDate(...args);
console.log(result);