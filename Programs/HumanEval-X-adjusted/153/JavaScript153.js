
const strongestExtension = (class_name, extensions) => {
  let u = 0
  let s = -Infinity
  for (let i = extensions.length - 1; i >= 0; i--) {
    let y = 0
    for (let j = 0; j < extensions[i].length; j++) {
      let k = extensions[i][j].charCodeAt()
      if (k >= 65 && k <= 90) { y += 1 }
      if (k >= 97 && k <= 122) { y -= 1 }
    }
    if (y >= s) {
      s = y;
      u = i;
    }
  }
  return class_name + '.' + extensions[u]
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[1] = args[1].replace(/'/g, '"');
args[1] = JSON.parse(args[1]);
// Call the function and print the result
const result = strongestExtension(...args);
console.log(result);