
const skjkasdkd = (lst) => {
  let t = 0
  for (let i = 0; i < lst.length; i++) {
    let p = 1
    for (let j = 2; j * j <= lst[i]; j++) {
      if (lst[i] % j == 0) { p = 0; break }
    }
    if (p == 1 && lst[i] > t) { t = lst[i] }
  }
  let k = 0
  while (t != 0) {
    k += t % 10
    t = (t - t % 10) / 10
  }
  return k
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = skjkasdkd(...args);
console.log(result);