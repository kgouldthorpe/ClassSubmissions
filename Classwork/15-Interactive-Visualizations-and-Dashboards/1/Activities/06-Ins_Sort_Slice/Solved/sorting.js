// Sorts descending
[3, 2, -120].sort(function compareFunction(firstNum, secondNum) {
   // resulting order is (3, 2, -120)
  return secondNum - firstNum;
});


// Sorts ascending
[3, 2, -120].sort(function compareFunction(firstNum, secondNum) {
  // resulting order is (-120, 2, 3)
  return firstNum - secondNum;
});

// Arrow Function (default small to large)
[3, 2, -120].sort();

// Arrow Function (large to small)
[3, 2, -120].sort((first, second) => second-first);
// or try with .reverse()
[3, 2, -120].sort().reverse();

// Arrow Function with text (default a to z)
["Jim", "Bob", "Angela"].sort();

// Arrow Function with text (z to a)
["Jim", "Bob", "Angela"].sort((first,second) => second-first);
//or try with .reverse()
["Jim", "Bob", "Angela"].sort().reverse();