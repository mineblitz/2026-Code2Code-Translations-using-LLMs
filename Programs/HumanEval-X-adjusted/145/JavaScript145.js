
const orderByPoints = (nums) => {
  let p = nums
  for (let j = p.length - 2; j >= 0; j--) {
    for (let k = 0; k <= j; k++) {
      let m = 0
      let n = 0
      let h = p[k]
      let d = p[k + 1]
      let y = 1
      let u = 1
      if (h < 0) { y = -1; h = -h; }
      if (d < 0) { u = -1; d = -d; }
      while (h >= 10) {
        m += h % 10;
        h = (h - h % 10) / 10;
      }
      m += y * h
      while (d >= 10) {
        n += d % 10;
        d = (d - d % 10) / 10;
      }
      n += u * d
      if (m > n) {
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
const result = orderByPoints(...args);
console.log(result);