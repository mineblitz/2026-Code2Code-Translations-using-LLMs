
const isSorted = (lst) => {
  if (lst.length == 0) { return true }
  let dup = 1
  let pre = lst[0]
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < pre) { return false }
    if (lst[i] == pre) {
      dup += 1;
      if (dup == 3) { return false }
    } else {
      pre = lst[i]
      dup = 1
    }
  }
  return true
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = isSorted(...args);
console.log(result);