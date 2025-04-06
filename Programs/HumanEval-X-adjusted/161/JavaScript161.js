
const solve = (s) => {
  let t = 0
  let p = ''
  for (let i = 0; i < s.length; i++) {
    let y = s[i].charCodeAt()
    if (y >= 65 && y <= 90) {
      y += 32;
      t = 1;
    } else if (y >= 97 && y <= 122) {
      y -= 32;
      t = 1;
    }
    p += String.fromCharCode(y)
  }
  if (t == 1) { return p }
  let u = ''
  for (let i = 0; i < p.length; i++) {
    u += p[p.length - i - 1]
  }
  return u
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = solve(...args);
console.log(result);