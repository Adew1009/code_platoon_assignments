
function binarySearch(target, lst, high = "first", low = 0){
  lst = lst.sort()
  if (high == "first") {
    high = lst.length - 1
  mid = Math.floor(((low) + (high))/2) }
  if (low > high) {
    return -1
    }else if (lst[mid] == target) {
  return mid}
  if (lst[mid] > target) {

    return binarySearch(target, lst, mid=mid- 1, low); }
  if (lst[mid] < target) {

    return binarySearch(target, lst, high, mid=mid+ 1); }
  return mid
}

var smallArray = [1,2,3,4,5]
var largeArray = [1,5,7,2,3,8,4,9]

console.log(binarySearch(1, smallArray) === 0);
console.log(binarySearch(2, smallArray) === 1);
console.log(binarySearch(3, smallArray) === 2);
console.log(binarySearch(4, smallArray) === 3);
console.log(binarySearch(5, smallArray) === 4);
console.log(binarySearch(7, largeArray) === 5);

