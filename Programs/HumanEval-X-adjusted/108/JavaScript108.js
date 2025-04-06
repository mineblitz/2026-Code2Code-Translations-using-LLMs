
const countNums = (arr) => {
  let p = 0
  for (let i = 0; i < arr.length; i++) {
    let h = arr[i]
    if (h > 0) {
      p++;
      continue;
    }
    let k = 0
    h = -h
    while (h >= 10) {
      k += h % 10;
      h = (h - h % 10) / 10;
    }
    k -= h;
    if (k > 0) { p++ }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = countNums(...args);
console.log(result);