
const wordsInSentence = (sentence) => {
  let t = sentence.split(/\s/)
  let p = ''
  for (let j = 0; j < t.length; j++) {
    let len = t[j].length;
    let u = 1
    if (len == 1 || len == 0) { continue }
    for (let i = 2; i * i <= len; i++) {
      if (len % i == 0) { u = 0 }
    }
    if (u == 0) { continue }
    if (p == '') { p += t[j] }
    else { p = p + ' ' + t[j] }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = wordsInSentence(...args);
console.log(result);