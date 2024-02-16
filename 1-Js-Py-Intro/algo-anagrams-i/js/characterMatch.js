exports.isCharacterMatch = function(string1, string2) {
  

    function createDictionary(string) {
        dict = {}
        for (let i = 0; i < string.length; i++) {
            let character = string[i]
            if (character != " "){
            if (dict[character] == undefined) {
                dict[character] = 1
            } else {
                dict[character] += 1
            }
        }
        }
        return dict
    }

    const string1dict = createDictionary(string1.toLowerCase())
    const string2dict = createDictionary(string2.toLowerCase())

    for (key in string1dict) {
        if (string1dict[key] != string1dict[key]){
            return false
    }
    return true
    }

}







exports.anagramsFor = function(word, listOfWords) {

// function anagramsFor(word, listOfWords) {

    answerArray = []

    function createDictionary(string) {
        dict = {}
        for (let i = 0; i < string.length; i++) {
            let character = string[i]
            if (dict[character] == undefined) {
                dict[character] = 1
            } else {
                dict[character] += 1
            }
        }
        return dict
    }
    const wordDict = createDictionary(word.toLowerCase())
 
    for (listword in listOfWords) {
        let listwordDict = createDictionary((listOfWords[listword]).toLowerCase())
        if (word.length === listOfWords[listword].length) {
             for (key in wordDict) {
                    if (wordDict[key] != (listwordDict[key])) {
                    break
                    } 
                }   
            answerArray.push(listOfWords[listword])
         }

};
return answerArray
}
