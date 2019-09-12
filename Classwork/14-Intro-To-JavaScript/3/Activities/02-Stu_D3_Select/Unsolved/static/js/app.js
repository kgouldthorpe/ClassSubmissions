// The new student and grade to add to the table
var newGrade = ["Wash", 79];

// Use D3 to select the table
var table = d3.select("table");
// Use d3 to create a bootstrap striped table
// http://getbootstrap.com/docs/3.3/css/#tables-striped

// Use D3 to select the table body
var tbody = d3.select("tbody");
// Append one table row `tr` to the table body
var row = tbody.select("tr");
// Append one cell for the student name
row.select("td").append(newGrade[0]);
// Append one cell for the student grade
row.select("td").append(newGrade[1]);