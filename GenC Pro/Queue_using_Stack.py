# Class to implement Queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        # stack_in is used for enqueue operations
        self.stack_in = []
        # stack_out is used for dequeue operations
        self.stack_out = []

    def enqueue(self, item):
        # Push item onto stack_in
        self.stack_in.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        # If stack_out is empty, move all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                popped = self.stack_in.pop()
                self.stack_out.append(popped)

        # If stack_out is still empty, queue is empty
        if not self.stack_out:
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            # Pop from stack_out which gives the front element of the queue
            dequeued = self.stack_out.pop()
            print(f"Dequeued: {dequeued}")
            return dequeued

    def display(self):
        # Display elements in queue order
        # Elements in stack_out are in correct dequeue order
        # Elements in stack_in need to be reversed to show correct order
        queue_elements = self.stack_out[::-1] + self.stack_in
        print("Queue:", queue_elements)


# Driver code to interact with user
queue = QueueUsingStacks()

while True:
    print("\nOptions:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        element = input("Enter element to enqueue: ")
        queue.enqueue(element)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        queue.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# 🔍 Explanation of Key Parts:
# Two stacks:

# stack_in is for enqueue operations (push new elements).

# stack_out is for dequeue operations (pop front elements).

# When dequeue is called and stack_out is empty, all elements from stack_in are moved to stack_out, reversing their order to simulate queue behavior.

# display() shows current queue order combining both stacks.