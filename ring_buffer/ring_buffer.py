class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #bottom of the list is the 0 index for some reason
    #resets the array so next time it is full it saves the 0 index
    if self.current is self.capacity:
  
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    temp_list = []
    for i in self.storage:
      if i is not None:
        temp_list.append(i)
    return temp_list