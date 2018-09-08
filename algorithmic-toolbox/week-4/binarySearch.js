function binarySearch(array, low, high, key) {
    if(high < low) {
      return -1;
    }
  
    const mid = low + Math.ceil((high - low) / 2);

    if(array[mid] === key) {
      return mid;
    }
  
    if(array[mid] < key) {
      return binarySearch(array, mid + 1, high, key);
    }
    else {
      return binarySearch(array, low, mid - 1, key);
    }
}