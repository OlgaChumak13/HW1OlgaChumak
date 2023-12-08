# Define the base URL and set the initial URL to the base URL
base_url = "https://codefirstgirls.com/"
current_url = base_url

# Loop to simulate clicking around the website until an exit is forced
while True:
    # Display the current URL
    print(f"You are currently on the URL {current_url}")
    print("Where are you clicking?")  # Prompt the user for their next action

    # Check the current URL and provide options accordingly
    if current_url == base_url:  # If on the base URL
        print("Options: Courses, Opportunities")
        user_input = input().lower()

        # Update the URL based on user input
        if user_input == "courses":
            current_url = base_url + "courses"
        elif user_input == "opportunities":
            current_url = base_url + "opportunities"

    elif current_url == base_url + "courses":  # If on the courses URL
        print("Options: CFGDegree, Back")
        user_input = input().lower()

        # Update the URL based on user input
        if user_input == "cfgdegree":
            current_url = base_url + "courses/cfgdegree"
        elif user_input == "back":
            current_url = base_url

    elif current_url == base_url + "opportunities":  # If on the opportunities URL
        print("Options: Ambassadors, Back")
        user_input = input().lower()

        # Update the URL based on user input
        if user_input == "ambassadors":
            current_url = base_url + "opportunities/ambassadors"
        elif user_input == "back":
            current_url = base_url

    elif current_url == base_url + "courses/cfgdegree" or current_url == base_url + "opportunities/ambassadors":
        # If on the sub-category URLs
        print("Options: Back")
        user_input = input().lower()

        # Update the URL based on user input
        if user_input == "back":
            if "courses" in current_url:
                current_url = base_url + "courses"
            elif "opportunities" in current_url:
                current_url = base_url + "opportunities"

    else:
        print("Invalid URL")  # Display for any invalid URL

    # Check if the user wants to exit the loop
    if user_input.lower() == "exit":
        break  # Exit the loop if the user enters 'exit'


#Code for Timing
import timeit

# Function to simulate the provided solution
"""Create test cases with different scenarios:
Small navigation paths (few clicks)
Medium-sized navigation paths (moderate number of clicks)
Large navigation paths (many clicks)
Measure the execution time using the timeit module for each test case.
"""
def simulate_navigation():
    # Include the provided solution here
    pass

# Measure execution time for varying input sizes
small_time = timeit.timeit(simulate_navigation, number=1000)
medium_time = timeit.timeit(simulate_navigation, number=10000)
large_time = timeit.timeit(simulate_navigation, number=100000)

print("Execution Time - Small Input:", small_time)
print("Execution Time - Medium Input:", medium_time)
print("Execution Time - Large Input:", large_time)

"""Space Complexity: 
The space complexity remains probably O(1) as the memory usage remains constant regardless of the size
 of the website or navigation depth. T
 The primary memory usage involves storing fixed-size variables like 
 base_url, current_url, and user_input, 
 contributing to a constant space requirement.

Overall,  time complexity fluctuates based on  navigation depth, 
while the space complexity remains constant, 
reflecting a moderate level of efficiency for this navigation simulation algoritm.
"""