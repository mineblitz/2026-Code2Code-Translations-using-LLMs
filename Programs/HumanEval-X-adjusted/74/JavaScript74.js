
const totalMatch = (lst1, lst2) => {
  var l1 = lst1.reduce(((prev, item) => prev + item.length), 0);
  var l2 = lst2.reduce(((prev, item) => prev + item.length), 0);
  if (l1 <= l2)
    return lst1;
  else
    return lst2;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = args[1].replace(/'/g, '"');
args[1] = JSON.parse(args[1]);
// Call the function and print the result
const result = totalMatch(...args);
console.log(result);