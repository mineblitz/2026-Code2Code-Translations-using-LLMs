
const sortArray = (arr) => {
  let p = arr
  for (let j = 0; j < p.length; j++) {
    let ind = j
    for (let k = j + 1; k < p.length; k++) {
      let w1 = p[ind].toString(2)
      let f1 = 0
      for (let u = 0; u < w1.length; u++) {
        if (w1[u] == '1') { f1++ }
      }
      let w2 = p[k].toString(2)
      let f2 = 0
      for (let u = 0; u < w2.length; u++) {
        if (w2[u] == '1') { f2++ }
      }
      if (f2 < f1 || (f1 == f2 && p[k] < p[ind])) {
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
const result = sortArray(...args);
console.log(result);