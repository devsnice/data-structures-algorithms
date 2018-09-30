# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Queue:
    def __init__(self, size):
        self.container = []
        self.size = size

    def add(self, element):
        self.container.append(element)

    def get(self):
        return self.container.pop(0)

    def getLast(self):
        if not self.isEmpty():
            return self.container[len(self.container) - 1]
        else:
            return -1

    def seeBeforeGet(self):
        return self.container[0]

    def isFull(self):
        return len(self.container) == self.size

    def isEmpty(self):
        return len(self.container) == 0


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finishTimeQueue = Queue(size)

    def Process(self, request):
        arrived_time = request.arrival_time

        hasProcessElements = True
        requestProcessingFinishTime = -1
        requestProcessingStartTime = -1
        nextQueueFinishTime = -1

        # remove elements from buffer, which was processed at the arrived_time of new packet
        while hasProcessElements and not self.finishTimeQueue.isEmpty():
            nextFinishTime = self.finishTimeQueue.seeBeforeGet()

            if nextFinishTime <= arrived_time:
                self.finishTimeQueue.get()
            else:
                hasProcessElements = False
                nextQueueFinishTime = nextFinishTime

        # when buffer has space, we can add a new packet to it
        if not self.finishTimeQueue.isFull():
            nextQueueFinishTime = self.finishTimeQueue.getLast()

            # default, when processor hasn't task, we can start processing at the arrival time
            requestProcessingFinishTime = request.process_time + request.arrival_time;
            requestProcessingStartTime = request.arrival_time

            # when processor has tasks, we need to await
            if nextQueueFinishTime != -1:
                if nextQueueFinishTime > request.arrival_time:
                    requestProcessingFinishTime = nextQueueFinishTime + request.process_time
                    requestProcessingStartTime = nextQueueFinishTime

            # add to buffer
            self.finishTimeQueue.add(requestProcessingFinishTime)

            return Response(False, requestProcessingStartTime)

        # otherwise, we need drop this request
        else:
            # dropped
            return Response(True, -1)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []

    for request in requests:
        responses.append(buffer.Process(request))

    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
