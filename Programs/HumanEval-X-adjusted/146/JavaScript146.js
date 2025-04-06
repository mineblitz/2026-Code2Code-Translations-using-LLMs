
const specialFilter = (nums) => {
  let p = 0
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < 10) { continue }
    let y = nums[i].toString()
    if (Number(y[0]) % 2 == 1 && Number(y[y.length - 1]) % 2 == 1) {
      p++
    }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = specialFilter(...args);
console.log(result);