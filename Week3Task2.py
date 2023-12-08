#QUESTION 2: Number In Sequence
"""
    Generates a sequence of numbers based on the formula: N1 = 8, Ni = Ni-1 + 7 for i > 1.
    N1=8
    N2=N1+7
    N3=N2+7 еtс.
    or
    N1 = 8, Ni = Ni-1 + 7 for i > 1.
    """

def num_in_seq1(n):
    if n == 1:
        return 8

    else:
        return num_in_seq(n - 1) + 7


"""
   alternative function
   set the parameters for the number n == 1 and n == 2
   Generates a sequence of numbers based on the formula:
   N1=8
   N2=15
   N3=(N2-N1)+N2 N3=(15-8)+15=22
   N4=(N3-N2)+N3 N4=(22-15)+22=29   etc
   or
   N1 = 8, N2 = 15, Ni = ((Ni-2) - (Ni-3)) + (Ni-2) for i > 2.
    """

# Initialize an empty list to store values for sequence generation
values = []


# Recursive function to calculate the value of a number in the sequence
def num_in_seq(n: int) -> int:
    # If the value at index n is already calculated, return it from the list
    if len(values) > n:
        return values[n]

    # Base cases for n = 0, 1, and 2
    if n == 0:
        values.append(0)
        return 0
    if n == 1:
        values.append(8)
        return 8
    if n == 2:
        values.append(15)
        return 15

    # Calculate the value for other indices in the sequence
    seq_number = (num_in_seq(n - 2) - num_in_seq(n - 3)) + num_in_seq(n - 2)
    values.append(seq_number)

    return seq_number


# Test cases for values of N1 to N5
if __name__ == '__main__':
    print ('Result for first function Num-in-seg1')
    print(f"num_in_seq1(1) =", num_in_seq1(1))
    print(f"num_in_seq1(2) =", num_in_seq1(2))
    print(f"num_in_seq1(3) =", num_in_seq1(3))
    print(f"num_in_seq1(4) =", num_in_seq1(4))
    print(f"num_in_seq1(5) =", num_in_seq1(5))

    print('Result for alternative function Num-in-seg')
    print(f"num_in_seq(1) =",num_in_seq(1))
    print(f"num_in_seq(2) =",num_in_seq(2))
    print(f"num_in_seq(3) =",num_in_seq(3))
    print(f"num_in_seq(4) =",num_in_seq(4))
    print(f"num_in_seq(5) =",num_in_seq(5))