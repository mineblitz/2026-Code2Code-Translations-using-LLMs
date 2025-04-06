
const intersection = (interval1, interval2) => {
  let lo = interval1[0]
  if (interval2[0] > lo) { lo = interval2[0] }
  let hi = interval1[1]
  if (interval2[1] < hi) { hi = interval2[1] }
  let len = 0
  if (hi > lo) { len = hi - lo }
  if (len == 1 || len == 0) { return 'NO' }
  for (let i = 2; i * i <= len; i++) {
    if (len % i == 0) { return 'NO' }
  }
  return 'YES'
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = args[1].replace(/'/g, '"');
args[1] = JSON.parse(args[1]);
// Call the function and print the result
const result = intersection(...args);
console.log(result);