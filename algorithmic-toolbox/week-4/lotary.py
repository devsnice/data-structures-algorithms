# Uses python3
import sys

def findBorder(segments, point, l, r):
    if l<=r:
        return r

    middle = l + (r - l) // 2

    if segments[middle]['start'] > point:
        return middle

    if segments[middle]['end'] > point:
        return findBorder(segments, point, middle + 1, r)
    else:
        return findBorder(segments, point, l, middle - 1)


def solution(segments, points):
    def sortByEnd(s):
        return s['end']

    sortedSegments = sorted(segments, key=sortByEnd)

    result = []

    for point in points:
        searchEnd = False
        index = findBorder(sortedSegments, point, 0, len(sortedSegments) - 1)
        count = 0;

        while searchEnd == False and index >= 0:
            if point <= sortedSegments[index]['end']:
                if point >= sortedSegments[index]['start']:
                    count = count + 1
            else:
                searchEnd = True
            index = index - 1

        result.append(count)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]

    segmentsCount = 0
    segments = []

    while segmentsCount < n:
        segments.append({
            'start': data[2*segmentsCount+2],
            'end': data[2*segmentsCount+3]
        })
        segmentsCount = segmentsCount + 1

    points = data[2 * n + 2:]

    cnt = solution(segments, points)

    for x in cnt:
        print(x, end=' ')
