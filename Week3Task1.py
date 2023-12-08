from collections import deque



# Function to process the input file and generate the final queue order
def process_queue(input_file):
    queue = deque()

    with open(input_file, 'r') as file:
        for line in file:
            command, name = line.split(maxsplit=1)
            name = name.strip()  # Remove leading/trailing whitespaces

            if command == 'JUMP':
                queue.appendleft(name)  # Add to the front of the queue
            elif command == 'JOIN':
                queue.append(name)  # Add to the end of the queue

    return list(queue)


# Replace 'input.txt' with the name of your input file
input_file = 'hw3_q1.txt'
final_queue_order = process_queue(input_file)
for name in final_queue_order:
    print(name)

"""Space complexity is primarily determined by the usage of data structures to store the queue 
and other variables.


A deque (queue) is used to store the queue of names. Deques are a part of the collections module in Python. 
They provide O(1) time complexity for adding or removing elements from both ends of the queue. Therefore, 
the space complexity for storing the queue is O(n), where 'n' is the number of elements in the queue.

Other variables like input_file, command, name, and final_queue_order are used to manage the input file,
 individual commands, names, and the final queue order. These variables occupy constant space, s
 o they don't significantly contribute to the overall space complexity.

Hence, considering the primary data structure used (deque) to store the queue of names, 
the space complexity of the code is O(n), where 'n' is the number of elements in the queue.
"""
