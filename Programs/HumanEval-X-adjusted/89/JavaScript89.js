
const encrypt = (s) => {
  let t = ''
  for (let i = 0; i < s.length; i++) {
    let p = s[i].charCodeAt() + 4
    if (p > 122) { p -= 26 }
    t += String.fromCharCode(p)
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = encrypt(...args);
console.log(result);