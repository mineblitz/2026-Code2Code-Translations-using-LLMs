
const moveOneBall = (arr) => {
  if (arr.length == 0) { return true }
  let k = 0
  let len = arr.length
  for (let i = 0; i < len; i++) {
    let t = 1;
    for (let j = 1; j < len; j++) {
      if (arr[j] < arr[j - 1]) {
        t = 0;
        break;
      }
    }
    if (t == 1) {
      k = 1;
      break;
    }
    arr.push(arr[0]);
    arr.shift()
  }
  if (k == 1) { return true }
  return false
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = moveOneBall(...args);
console.log(result);