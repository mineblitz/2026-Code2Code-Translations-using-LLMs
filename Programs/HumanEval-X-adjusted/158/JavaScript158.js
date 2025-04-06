
const findMax = (words) => {
  let s = -1
  let u = -1
  if (words.length == 0) { return '' }
  for (let i = 0; i < words.length; i++) {
    let p = 0
    for (let j = 0; j < words[i].length; j++) {
      let y = 1
      for (let k = 0; k < j; k++) {
        if (words[i][j] == words[i][k]) { y = 0 }
      }
      if (y == 1) { p++ }
    }
    if (p > s || (p == s && words[i] < words[u])) {
      u = i;
      s = p;
    }
  }
  return words[u]
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = findMax(...args);
console.log(result);