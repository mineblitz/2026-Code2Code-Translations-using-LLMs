
const strangeSortList = (lst) => {
  var res = [], sw = true;
  while (lst.length) {
    res.push(sw ? Math.min(...lst) : Math.max(...lst));
    lst.splice(lst.indexOf(res.at(-1)), 1);
    sw = !sw;
  }
  return res;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = strangeSortList(...args);
console.log(result);