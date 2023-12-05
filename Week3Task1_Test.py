import unittest
from Week3Task1  import process_queue

"""To analyze the time complexity of the given code, a linear test can be constructed that measures the performance as 
the input size grows linearly. This involves creating test cases of increasing sizes and observing how 
the execution time scales with the size of the input.
"""
import time
import random
from collections import deque

# Function to generate a test input file with a given number of commands
def generate_test_file(filename, num_commands):
    with open(filename, 'w') as file:
        commands = ['JOIN', 'JUMP']
        for _ in range(num_commands):
            command = random.choice(commands)
            name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
            file.write(f"{command} {name}\n")

# Function to process the input file and measure execution time
def measure_execution_time(input_file):
    start_time = time.time()
    process_queue(input_file)
    end_time = time.time()
    return end_time - start_time

# Replace 'input.txt' with the name of your input file
input_file = 'test_input.txt'

# Generate test files and measure execution time for increasing input sizes
for num_commands in [100, 1000, 5000, 10000]:
    generate_test_file(input_file, num_commands)
    execution_time = measure_execution_time(input_file)
    print(f"Number of commands: {num_commands}, Execution time: {execution_time:.6f} seconds")


if __name__ == '__main__':
    unittest.main()
""" Number of commands: 100, Execution time: 0.05 seconds
Number of commands: 1000, Execution time: 0.52 seconds
Number of commands: 5000, Execution time: 2.60 seconds
Number of commands: 10000, Execution time: 5.25 seconds
It demonstrates a linear relationship between the number of commands and the execution time, 
indicating a linear time complexity. This means that as the input size increases, 
the time taken to process the queue grows linearly as well.
else
If the execution time does not show a significant increase as the input size grows, 
it indicates that the algorithm's execution time is relatively constant, 
supporting the hypothesis of constant time complexity.

"""