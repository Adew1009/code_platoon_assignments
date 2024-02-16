function fibonacci(num) {
// const fibSeq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
// return fibSeq[num]
// }
let a = 0;
let b = 1;
let c = 0;
if (num ===0){
  return 0;
} else if (num === 1) {
  return 1;
  TODO this the to list 
} else {
  for (let i =1; i < num; i++){
    c = a + b;
    a = b;
    b = c;
  }
  return c;
}
}
console.log(fibonacci(11))
module.exports = fibonacci;