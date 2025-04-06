
const sortArray = (array) => {
  let arr = array
  let tot = arr[0] + arr[arr.length-1]
  for (let j = 0; j < arr.length; j++) {
    let ind = j
    for (let k = j + 1; k < arr.length; k++) {
      if ((tot % 2 == 1 && arr[k] < arr[ind]) || (tot % 2 == 0 && arr[k] > arr[ind])) {
        ind = k
      }
    }
    let tmp = arr[j]
    arr[j] = arr[ind]
    arr[ind] = tmp
  }
  return arr
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = sortArray(...args);
console.log(result);