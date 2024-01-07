import heapq

def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort intervals by end times
    min_heap = []

    for interval in intervals:
        start, end = interval
        if min_heap and start >= min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)

    return len(min_heap)

def main():
    num_instances = int(input().strip())

    for _ in range(num_instances):
        num_jobs = int(input().strip())
        jobs = []

        for _ in range(num_jobs):
            start, end = map(int, input().strip().split())
            jobs.append((start, end))

        result = interval_scheduling(jobs)
        print(result)

if __name__ == "__main__":
    main()
