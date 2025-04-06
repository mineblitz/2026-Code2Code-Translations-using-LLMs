
const uniqueDigits = (x) => {
  let p = []
  for (let i = 0; i < x.length; i++) {
    let h = x[i]
    let boo = 1
    while (h > 0) {
      let r = h % 10
      if (r % 2 == 0) {
        boo = 0;
        break;
      }
      h = (h - r) / 10
    }
    if (boo) {
      p.push(x[i])
    }
  }
  for (let j = 0; j < p.length; j++) {
    let ind = j
    for (let k = j + 1; k < p.length; k++) {
      if (p[k] < p[ind]) {
        ind = k
      }
    }
    if (ind > j) {
      let tmp = p[j]
      p[j] = p[ind]
      p[ind] = tmp
    }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = uniqueDigits(...args);
console.log(result);