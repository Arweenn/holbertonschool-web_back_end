export default function appendToEachArrayValue(array, appendString) {
  const newArr = [];
  for (const idx of array) {
    newArr.push(appendString + idx);
  }

  return newArr;
}
