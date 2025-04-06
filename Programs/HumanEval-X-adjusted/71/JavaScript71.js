
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a)
    return -1;
  var s = (a + b + c) / 2;
  var area = Math.pow(s * (s - a) * (s - b) * (s - c), 0.5);
  area = area.toFixed(2);
  return area;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
args[2] = parseInt(args[2]);
// Call the function and print the result
const result = triangleArea(...args);
console.log(result);