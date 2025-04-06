
const numericalLetterGrade = (grades) => {
  let letter_grade = []
  for (let i = 0, len = grades.length; i < len; i++) {
    let gpa = grades[i]
    if (gpa == 4.0) {
      letter_grade.push('A+')
    } else if (gpa > 3.7) {
      letter_grade.push('A')
    } else if (gpa > 3.3) {
      letter_grade.push('A-')
    } else if (gpa > 3.0) {
      letter_grade.push('B+')
    } else if (gpa > 2.7) {
      letter_grade.push('B')
    } else if (gpa > 2.3) {
      letter_grade.push('B-')
    } else if (gpa > 2.0) {
      letter_grade.push('C+')
    } else if (gpa > 1.7) {
      letter_grade.push('C')
    } else if (gpa > 1.3) {
      letter_grade.push('C-')
    } else if (gpa > 1.0) {
      letter_grade.push('D+')
    } else if (gpa > 0.7) {
      letter_grade.push('D')
    } else if (gpa > 0.0) {
      letter_grade.push('D-')
    } else {
      letter_grade.push('E')
    }
  }
  return letter_grade
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = numericalLetterGrade(...args);
console.log(result);