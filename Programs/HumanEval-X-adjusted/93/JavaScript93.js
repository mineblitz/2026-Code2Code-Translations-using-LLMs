
const encode = (message) => {
  let t = ''
  for (let i = 0; i < message.length; i++) {
    let p = message[i].charCodeAt()
    if (p > 96) { p -= 32 }
    else if (p!=32 && p < 96) { p += 32 }
    if (p == 65 || p == 97 || p == 69 || p == 101 || p == 73 || p == 105 || p == 79 || p == 111 || p == 85 || p == 117) { p += 2 }
    t += String.fromCharCode(p)
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = encode(...args);
console.log(result);