
const wordsString = (s) => {
  let t = ''
  let p = []
  let k = 0
  for (let i = 0; i < s.length; i++) {
    if (s[i] == ' ' || s[i] == ',') {
      if (k == 0) {
        k = 1;
        p.push(t);
        t = '';
      }
    }
    else {
      k = 0;
      t += s[i]
    }
  }
  if (t != '') {
    p.push(t);
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = wordsString(...args);
console.log(result);