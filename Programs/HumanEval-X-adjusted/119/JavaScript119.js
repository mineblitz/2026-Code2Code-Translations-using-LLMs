
const matchParens = (lst) => {
  let w1 = lst[0] + lst[1]
  let y = 0
  let u = 1
  for (let i = 0; i < w1.length; i++) {
    if (w1[i] == '(') { y++ }
    else { y-- }
    if (y < 0) {
      u = 0;
      break;
    }
  }
  if (u == 1 && y == 0) { return 'Yes' }
  w1 = lst[1] + lst[0]
  y = 0
  u = 1
  for (let i = 0; i < w1.length; i++) {
    if (w1[i] == '(') { y++ }
    else { y-- }
    if (y < 0) {
      u = 0;
      break;
    }
  }
  if (u == 1 && y == 0) { return 'Yes' }
  return 'No'
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = matchParens(...args);
console.log(result);