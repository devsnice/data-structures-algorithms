/**
 *
 * O(n) = nlogn
 *
 * @param {*} knapsackWeight
 * @param {*} items
 */
const maxValueOfTheLoot = (knapsackWeight, items) => {
  // sort by value per kg
  const sortedByValueItems = items.sort((a, b) => {
    return b.value / b.weight - a.value / a.weight;
  });

  let resultLootValue = 0;

  // current items index
  let index = 0;

  // look for most valuable items
  while (knapsackWeight !== 0 && index < sortedByValueItems.length) {
    // knapsack can fit only part of item, when knapsack almost done
    if (knapsackWeight - sortedByValueItems[index].weight < 0) {
      resultLootValue +=
        (sortedByValueItems[index].value / sortedByValueItems[index].weight) *
        knapsackWeight;
      knapsackWeight = 0;
      // in another case, we can get all item
    } else {
      resultLootValue +=
        (sortedByValueItems[index].value / sortedByValueItems[index].weight) *
        sortedByValueItems[index].weight;

      knapsackWeight = knapsackWeight - sortedByValueItems[index].weight;
    }

    // go to next iten
    index++;
  }

  return resultLootValue.toFixed(4);
};

/**
 * Read line function
 */

let amountItemsLines;
let knapsackWeight;
let items = [];

let linesReaded;

function readLine(line) {
  if (line !== "\n") {
    const parsedLine = line.toString();

    // parse first line
    if (!amountItemsLines) {
      const values = parsedLine.split(" ");

      amountItemsLines = parseInt(values[0], 10);
      knapsackWeight = parseInt(values[1], 10);
    } else {
      // read item
      const values = parsedLine.split(" ");
      const item = {
        value: parseInt(values[0], 10),
        weight: parseInt(values[1], 10)
      };

      items.push(item);

      // readed all lines
      if (items.length === amountItemsLines) {
        linesReaded = true;
      }
    }

    if (linesReaded) {
      console.log(maxValueOfTheLoot(knapsackWeight, items));

      process.exit();
    }
  }
}

module.exports = maxValueOfTheLoot;
