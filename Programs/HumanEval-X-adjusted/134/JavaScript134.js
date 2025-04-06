
const checkIfLastCharIsALetter = (txt) => {
  let len = txt.length
  if (len == 0) { return false }
  let y = txt[len - 1].charCodeAt()
  if (len == 1) {
    if ((y >= 65 && y <= 90) || (y >= 97 && y <= 122)) { return true }
    return false
  }
  if (txt[len - 2] == ' ' && ((y >= 65 && y <= 90) || (y >= 97 && y <= 122))) { return true }
  return false
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = checkIfLastCharIsALetter(...args);
console.log(result);