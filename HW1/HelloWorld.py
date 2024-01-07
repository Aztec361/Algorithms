# Get the number of instances
num_instances = int(input())

# Get all strings at once
strings = [input() for _ in range(num_instances)]

# Print all greetings at once
print('\n'.join(f'Hello, {s}!' for s in strings))
