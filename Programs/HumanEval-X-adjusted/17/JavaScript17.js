
const parseMusic = (music_string) => {
  const note_map = {'o': 4, 'o|': 2, '.|': 1};
  return music_string.split(' ').filter(x => x != '').map(x => note_map[x]);
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = parseMusic(...args);
console.log(result);