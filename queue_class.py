# Queue Class

class Queue:

    def __init__(self, size):
        """ 
        Initialize the queue.
        """
        self.queue = []
        self.size = size

    def __len__(self):
        """
        Return number of items in the queue.
        """
        return len(self.queue)
    
    def __str__(self):
        """
        Returns a string representation of the queue.
        """
        return str(self.queue)
    
    def enqueue(self, item):
        """
        Adds item to the end of the queue if it is not full.
        """  
        if self.__len__() < self.size:
            self.queue.append(item)
            return self.queue
        else:
            return "Queue is full."
    
    def dequeue(self):
        """
        Removes and returns the first item in the queue if it is not empty. 
        """
        if self.__len__() == 0:
            return "Queue is empty."
        else:  
            return self.queue.pop(0) # Return the first item in the queue (located at index 0)
        
