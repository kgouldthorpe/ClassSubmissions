// Array of movie ratings
var movieScores = [
  4.4,
  3.3,
  5.9,
  8.8,
  1.2,
  5.2,
  7.4,
  7.5,
  7.2,
  9.7,
  4.2,
  6.9
];

// Starting a rating count
var sum = 0;

// Arrays to hold movie scores
var goodMovieScores = [];
var okMovieScores = [];
var badMovieScores = [];

//for statement to go throught the list
for (var m=0; m=movieScore.length,m++){
  var score = (sum + m);
  //if statement for over 7
  if(score>=7){
    goodMovieScores.push(score);
  }
  //if statement between 5 and 7
  if (score >=5, && score <7){
    okMovieScores.push(score);
  } 
  //if statement less than 5
  if (score <5){
    badMovieScores.push(score);
  }
}
