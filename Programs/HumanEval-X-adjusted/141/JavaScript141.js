
const fileNameCheck = (file_name) => {
  let t = file_name.split(/\./)
  if (t.length != 2) { return 'No' }
  if (t[1] != 'txt' && t[1] != 'dll' && t[1] != 'exe') { return 'No' }
  if (t[0] == '') { return 'No' }
  let a = t[0][0].charCodeAt()
  if (!((a >= 65 && a <= 90) || (a >= 97 && a <= 122))) { return 'No' }
  let y = 0
  for (let i = 1; i < t[0].length; i++) {
    if (t[0][i].charCodeAt() >= 48 && t[0][i].charCodeAt() <= 57) { y++ }
    if (y > 3) { return 'No' }
  }
  return 'Yes'
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = fileNameCheck(...args);
console.log(result);