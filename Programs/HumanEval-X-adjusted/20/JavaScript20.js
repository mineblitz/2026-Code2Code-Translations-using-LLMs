
const findClosestElements = (numbers) => {
  var closest_pair, distance;
  for (let i = 0; i < numbers.length; i++)
    for (let j = 0; j < numbers.length; j++)
      if (i != j) {
        let a = numbers[i], b = numbers[j];
        if (distance == null) {
          distance = Math.abs(a - b);
          closest_pair = [Math.min(a, b), Math.max(a, b)];
        } else {
          let new_distance = Math.abs(a - b);
          if (new_distance < distance) {
            distance = new_distance;
            closest_pair = [Math.min(a, b), Math.max(a, b)];
          }
        }
      }
  return closest_pair;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = findClosestElements(...args);
console.log(result);