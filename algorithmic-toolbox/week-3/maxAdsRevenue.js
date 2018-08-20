/**
 * Maximum Advertisement Revenue
 *
 * O(n) = 2 * nlog(n) + n = nlog(n)
 *
 * @param {Array} ads
 * @param {Array} numberOfClicksBySlots
 */
const maxAdsRevenue = (ads, numberOfClicksBySlots) => {
  const sortedAds = ads.sort((a, b) => {
    return b - a;
  });

  const sortedSlots = numberOfClicksBySlots.sort((a, b) => {
    return b - a;
  });

  let result = 0;

  // product sum of average amount of clicks by slots on profit per click from an ad
  sortedAds.forEach((ad, index) => {
    result += ad * sortedSlots[index];
  });

  return result;
};

module.exports = maxAdsRevenue;
