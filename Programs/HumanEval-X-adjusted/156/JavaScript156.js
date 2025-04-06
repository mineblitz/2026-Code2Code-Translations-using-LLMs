
const intToMiniRoman = (number) => {
  let num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  let sym = ['i', 'iv', 'v', 'ix', 'x', 'xl', 'l', 'xc', 'c', 'cd', 'd', 'cm', 'm']
  let i = 12
  let res = ''
  while (number) {
    let div = (number - number % num[i]) / num[i]
    number = number % num[i]
    while (div) {
      res += sym[i]
      div -= 1
    }
    i -= 1
  }
  return res
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = intToMiniRoman(...args);
console.log(result);