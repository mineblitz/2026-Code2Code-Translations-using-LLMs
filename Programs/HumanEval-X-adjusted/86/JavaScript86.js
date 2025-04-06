
const antiShuffle = (s) => {
  let arr = s.split(/\s/)
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      let ind = j
      for (let k = j + 1; k < arr[i].length; k++) {
        if (arr[i][k].charCodeAt() < arr[i][ind].charCodeAt()) {
          ind = k
        }
      }
      if (ind > j) {
        arr[i] = arr[i].slice(0, j) + arr[i][ind] + arr[i].slice(j + 1, ind) + arr[i][j] + arr[i].slice(ind + 1, arr[i].length)
      }
    }
  }
  let t = ''
  for (let i = 0; i < arr.length; i++) {
    if (i > 0) {
      t = t + ' '
    }
    t = t + arr[i]
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = antiShuffle(...args);
console.log(result);