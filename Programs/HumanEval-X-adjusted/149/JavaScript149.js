
const sortedListSum = (lst) => {
  let p = []
  for (let i = 0; i < lst.length; i++) {
    if (lst[i].length % 2 == 0) {
      p.push(lst[i])
    }
  }
  for (let j = p.length - 2; j >= 0; j--) {
    for (let k = 0; k <= j; k++) {
      let f = 0
      if (p[k].length > p[k + 1].length) { f = 1 }
      if (p[k].length == p[k + 1].length) {
        let r = p[k].length
        for (let l = 0; l < r; l++) {
          if (p[k][l].charCodeAt() > p[k + 1][l].charCodeAt()) {
            f = 1;
            break;
          }
          if (p[k][l].charCodeAt() < p[k + 1][l].charCodeAt()) {
            break;
          }
        }
      }
      if (f == 1) {
        let tmp = p[k]
        p[k] = p[k + 1]
        p[k + 1] = tmp
      }
    }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = sortedListSum(...args);
console.log(result);