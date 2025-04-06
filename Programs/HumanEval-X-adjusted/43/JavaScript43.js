
const pairsSumToZero = (l) => {
  for (let i = 0; i < l.length; i++)
    for (let j = i + 1; j < l.length; j++)
      if (l[i] + l[j] == 0)
        return true;
  return false;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = pairsSumToZero(...args);
console.log(result);