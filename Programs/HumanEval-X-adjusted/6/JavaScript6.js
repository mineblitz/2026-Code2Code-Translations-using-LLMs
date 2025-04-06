
const parseNestedParens = (paren_string) => {
  var parseParenGroup = function (s) {
    let depth = 0, max_depth = 0;
    for (const c of s) {
      if (c == '(') {
        depth += 1;
        max_depth = Math.max(max_depth, depth);
      } else {
        depth -= 1;
      }
    }
    return max_depth;
  }
  return paren_string.split(' ')
          .filter(x => x != '')
          .map(x => parseParenGroup(x));
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = parseNestedParens(...args);
console.log(result);