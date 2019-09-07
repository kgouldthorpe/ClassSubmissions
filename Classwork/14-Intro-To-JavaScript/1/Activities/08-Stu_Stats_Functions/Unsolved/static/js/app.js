var movieScore = [4.4, 3.3, 5.9, 8.8, 1.2, 5.2, 7.4, 7.5, 7.2, 9.7, 4.2, 6.9];

function printMean(userList){
    var totalMean = 0;
    for(var i=0; i<userList.length; i++){
        var meanPrep= (totalMean + i);
    }
    var mean = Math.mean(meanPrep);
    console.log(`The mean is ${mean}.`);
}
function printVariance(userList){
    var totalVar = 0;
    for(var i=0; i<userList.length; i++){
        var varPrep= (totalVar + i);
    }
    var variance = Math.variance(varPrep);
    console.log(`The variance is ${variance}.`);
}
function printStdDev(userList){
    var totalstd = 0;
    for(var i=0; i<userList.length; i++){
        var stdPrep= (totalstd + i);
    }
    var std = Math.sqrt(variance);
    console.log(`The standard deviation is ${std}.`);
}
printStdDev(movieScore);
printMean(movieScore);
printVariance(movieScore);