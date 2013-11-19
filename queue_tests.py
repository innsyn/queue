# Queue Class Testing

# Importing the class
from queue_class import Queue
print
print "Queue Class Testing"
print
print "A new Queue object is created with a size of 3."

# Testing enqueue
test_queue = Queue(3) # Make new queue with capacity 3
test_queue.enqueue(1) # Enqueue 1
test_queue.enqueue(2) # Enqueue 2
test_queue.enqueue(3) # Enqueue 3
print "Attempt to enqueue 1,2 and 3:", test_queue # Expected: [1,2,3] Actual: [1,2,3]. Enqueue is working correctly.
print

# Testing enqueue when queue is full
print "Attempt to enqueue 4:", test_queue.enqueue(4) # Enqueue 4, Expected: "Queue is full" Actual: "Queue is full". Enqueue correctly detects that the queue is full and does not add the new item.
print

# Testing dequeue
print "First attempt to dequeue:", test_queue.dequeue() # Expeced: 1 Actual 1.
print "Remaining queue:", test_queue # Dequeue is correctly removing the first item in the queue

# Testing dequeue when queue is empty
print "Second attempt to dequeue:", test_queue.dequeue()
print "Third attempt to dequeue:", test_queue.dequeue()
print "Remaining queue (Queue should now be empty):", test_queue
print "Fourth attempt to dequeue:", test_queue.dequeue() # Expected: "Queue is empty" Actual: "Queue is empty". Dequeue is working correctly, detects when queue is empty.
