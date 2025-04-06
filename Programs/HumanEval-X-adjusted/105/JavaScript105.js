
const byLength = (arr) => {
  p = []
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0 && arr[i] < 10) { p.push(arr[i]) }
  }
  for (let j = 0; j < p.length; j++) {
    let ind = j
    for (let k = j + 1; k < p.length; k++) {
      if (p[k] > p[ind]) {
        ind = k
      }
    }
    if (ind > j) {
      let tmp = p[j]
      p[j] = p[ind]
      p[ind] = tmp
    }
  }
  let l = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
  let t = []
  for (let j = 0; j < p.length; j++) {
    t.push(l[p[j]-1])
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = byLength(...args);
console.log(result);