var sentence =   [
    "I", "yam", "what", "I", "yam", "and", 'always', 'will', 'be', 'what', 'I', 'yam'];

var count={};

for (var i=0; i< sentence.length; i++){
    var currentWord = [i];

    if (currentWord in sentence){
        count[currentWord] =+ 1;
    }
    else {
        count[currentWord] = 1;
    }
};
console.log(count);
