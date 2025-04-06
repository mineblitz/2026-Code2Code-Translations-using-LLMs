
const isNested = (string) => {
  let opening_bracket_index = []
  let closing_bracket_index1 = []
  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      opening_bracket_index.push(i)
    }
    else {
      closing_bracket_index1.push(i)
    }
  }
  let closing_bracket_index = []
  for (let i = 0; i < closing_bracket_index1.length; i++) {
    closing_bracket_index.push(closing_bracket_index1[closing_bracket_index1.length - i - 1])
  }
  let cnt = 0
  let i = 0
  let l = closing_bracket_index.length
  for (let k = 0; k < opening_bracket_index.length; k++) {
    if (i < l && opening_bracket_index[k] < closing_bracket_index[i]) {
      cnt += 1;
      i += 1;
    }
  }
  return cnt >= 2
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = isNested(...args);
console.log(result);