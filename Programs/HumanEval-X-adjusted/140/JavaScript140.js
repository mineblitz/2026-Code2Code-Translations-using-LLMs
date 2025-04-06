
const fixSpaces = (text) => {
  let t = ''
  let c = 0
  for (let i = 0; i < text.length; i++) {
    if (text[i] == ' ') { c++ }
    else if (c > 0) {
      if (c == 1) { t += '_' }
      if (c == 2) { t += '__' }
      if (c > 2) { t += '-' }
      t += text[i]
      c = 0;
    } else {
      t += text[i]
    }
  }
  if (c == 1) { t += '_' }
  if (c == 2) { t += '__' }
  if (c > 2) { t += '-' }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = fixSpaces(...args);
console.log(result);