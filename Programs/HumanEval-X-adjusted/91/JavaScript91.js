
const isBored = (S) => {
  let t = 0
  if (S[0] == 'I' && S[1] == ' ') { t = 1 }
  for (let i = 0; i < S.length; i++) {
    if (S[i] == '.' || S[i] == '!' || S[i] == '?') {
      if (S[i + 1] == ' ' && S[i + 2] == 'I' && S[i + 3] == ' ') {
        t++
      }
    }
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = isBored(...args);
console.log(result);