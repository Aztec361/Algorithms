def weighted_interval_scheduling(jobs):
    # Sort jobs according to finish times
    jobs.sort(key = lambda x: x[1])
    n = len(jobs)
    
    # Create an array to store solutions of subproblems
    dp = [0 for _ in range(n)]
    dp[0] = jobs[0][2]
    
    # Fill entries in dp[] using recursive property
    for i in range(1, n):
        # Find profit including the current job
        inclProf = jobs[i][2]
        l = binarySearch(jobs, i)
        if (l != -1):
            inclProf += dp[l]
 
        # Store maximum of including and excluding
        dp[i] = max(inclProf, dp[i - 1])
 
    return dp[n-1]

# A Binary Search based function to find the latest job (before current job) that doesn't conflict with current job.
def binarySearch(job, start_index):
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start_index - 1
 
    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid][1] <= job[start_index][0]:
            if job[mid + 1][1] <= job[start_index][0]:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

# Driver code to test above function
if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n_jobs = int(input())
        jobs = []
        for _ in range(n_jobs):
            i, j, k = map(int, input().split())
            jobs.append((i, j, k))
        print(weighted_interval_scheduling(jobs))
