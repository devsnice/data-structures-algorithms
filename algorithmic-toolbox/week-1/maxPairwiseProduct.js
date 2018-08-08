/**
 * Find the maximum product of two distinct numbers
 * in a sequence of non-negative integer
 *
 * @param {NumbersArray} numbers
 * @returns {Number} maximum product number
 */
function findMaxPairwiseProduct(numbers) {
	let firstMax = 0;
	let secondMax = 0;

	numbers.map(number => {
		number = parseInt(number, 10);

		if (firstMax < number) {
			secondMax = firstMax;
			firstMax = number;
		} else if (secondMax < number) {
			secondMax = number;
		}
	});

	return firstMax * secondMax;
}
