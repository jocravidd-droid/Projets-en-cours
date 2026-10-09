"""
Method to create a stack with infinite size. The stack is implemented using a list and the elements are added to the end of the list. When the stack reaches its maximum size, the first element is removed to make room for new elements.
FIFO (First In First Out) is used to remove the first element from the stack when it reaches its maximum size. The function takes a list of numbers as input and returns the modified list after adding new elements and removing the first element.

This is representation of a stack with infinite size, where the first element is removed when the stack reaches its maximum size. The function can be used to simulate a stack with infinite size by continuously adding new elements and removing the first element when the stack reaches its maximum size.
detaille : designed to demonstrate the concept of a stack with infinite size, where the first element is removed when the stack reaches its maximum size. The function can be used to simulate a stack with infinite size by continuously adding new elements and removing the first element when the stack reaches its maximum size.
"""


def stack_infini(numbers=[1, 2, 3, 4, 5]):

    for i in range(len(numbers) + 5):
        numbers.append(i)
        del numbers[0]

    return numbers


x = stack_infini()
print(x)
