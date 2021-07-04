// Tiny steps to mastering JavaScript

// https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/javascript

function filter_list(l) {
    // Return a new array with the strings filtered out
    var result = []
    for (var item of l) {
        if (typeof (item) === 'number') {
            result.push(item)
        }
    }
    return result
}

// https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/javascript

const binaryArrayToNumber = arr => {
    // Given an array of ones and zeroes, convert the equivalent binary value to an integer.
    return parseInt(arr.join(''), 2);
};


// https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/javascript

function createPhoneNumber(numbers) {
    return `(${numbers.slice(0, 3).join('')}) ${numbers.slice(3,6).join('')}-${numbers.slice(6,10).join('')}`
}
