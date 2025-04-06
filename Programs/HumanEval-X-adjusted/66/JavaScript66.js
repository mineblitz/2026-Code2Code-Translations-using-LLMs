
const digitSum = (s) => {
  if (s == '') return 0;
  return s.split('').reduce((prev, char) => {
    let ord_char = char.charCodeAt(0)
    return prev + (ord_char > 64 && ord_char < 91 ? ord_char : 0);
  }, 0);
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = digitSum(...args);
console.log(result);