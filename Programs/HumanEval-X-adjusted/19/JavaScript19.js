
const sortNumbers = (numbers) => {
  const value_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  };
  return numbers.split(' ')
          .filter(x => x != '')
          .sort((a, b) => value_map[a] - value_map[b])
          .join(' ');
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = sortNumbers(...args);
console.log(result);