
const compare = (game, guess) => {
  for (let i = 0; i < guess.length; i++) {
    game[i] -= guess[i]
 if (game[i]<0)
 game[i]=-game[i];  }
  return game
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
args[1] = args[1].replace(/'/g, '"');
args[1] = JSON.parse(args[1]);
// Call the function and print the result
const result = compare(...args);
console.log(result);