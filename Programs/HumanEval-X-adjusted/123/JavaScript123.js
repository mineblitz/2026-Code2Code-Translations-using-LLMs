
const getOddCollatz = (n) => {
  let p = []
  let t = n
  while (1) {
    let u = 0
    for (let i = 0; i < p.length; i++) {
      if (t == p[i]) {
        u = 1
        break;
      }
    }
    if (u == 1) { break }
    if (t % 2 == 1) { p.push(t); t = 3 * t + 1 }
    else { t = t / 2 }
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
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = getOddCollatz(...args);
console.log(result);