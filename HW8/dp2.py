def knapsack(num_instances, instances):
    results = []
    
    for _ in range(num_instances):
        n, W, items = instances.pop(0)
        
        # Create a 2D DP table with (n+1) rows and (W+1) columns
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
        # Fill in the DP table
        for i in range(1, n + 1):
            weight, value = items[i - 1]
            for w in range(1, W + 1):
                if weight > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        
        results.append(dp[n][W])
    
    return results

# Sample input parsing
num_instances = int(input())
instances = []
for _ in range(num_instances):
    n, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    instances.append((n, W, items))

# Calculate and print the results
results = knapsack(num_instances, instances)
for result in results:
    print(result)
