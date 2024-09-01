from random import randint

class Node(object):
    """ A Doubly-linked lists' node. """
    def __init__(self, data=None, next=None, prev=None):
        # Initialize the node with data, next pointer, and previous pointer
        self.data = data
        self.next = next
        self.prev = prev
        # Time Complexity: O(1)
        # Space Complexity: O(1)

class Queue(object):
    """ A doubly-linked list. """
    def __init__(self):
        # Initialize the queue with head and tail as None and count as 0
        self.head = None
        self.tail = None
        self.count = 0
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def enqueue(self, data):
        """ Append an item to the list. """
        # Create a new node with the given data
        new_node = Node(data, None, None)
        if self.head is None:
            # If the queue is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = self.head
        else:
            # If the queue is not empty, add the new node to the end of the queue
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # Increment the count of elements in the queue
        self.count += 1
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def dequeue(self):
        """ Remove elements from the front of the list"""
        current = self.head
        if self.count == 1:
            # If there is only one element in the queue, remove it and set head and tail to None
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            # If there are more than one elements in the queue, remove the head element
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
        return current
        # Time Complexity: O(1)
        # Space Complexity: O(1)

# Create a new queue
queue = Queue()

# Measure the time taken to enqueue and dequeue 100,000 elements
import time
start_time = time.time()
for i in range(100000):
    queue.enqueue(i)
for i in range(100000):
    queue.dequeue()
print("--- %s seconds ---" % (time.time() - start_time))

class Track:
    def __init__(self, title=None):
        # Initialize the track with a title and a random length between 5 and 10 seconds
        self.title = title
        self.length = randint(5, 10)
        # Time Complexity: O(1)
        # Space Complexity: O(1)

# Create track instances
track1 = Track("white whistle")
track2 = Track("butter butter")
print(track1.length)
print(track2.length)

class MediaPlayerQueue(Queue):
    def add_track(self, track):
        # Add a track to the media player queue
        self.enqueue(track)

    def play(self):
        # Play tracks from the media player queue
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)

# Create track instances
track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")

# Create a media player queue and add tracks to it
media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)

# Play the tracks in the media player queue
media_player.play()




##################################################################################



### Detailed Explanation

#### Node Class

# """The `Node` class represents a node in the doubly linked list used to implement the queue.

# - **`__init__`**: Initializes the node with data, and sets the next and previous pointers to `None`.

# #### Queue Class

# The `Queue` class implements a queue using a doubly linked list.

# - **`__init__`**: Initializes the queue with `head` and `tail` as `None` and `count` as `0`.

# - **`enqueue`**: Adds a new element to the end of the queue.
#   - Creates a new node with the given data.
#   - If the queue is empty, sets the new node as both `head` and `tail`.
#   - If the queue is not empty, adds the new node to the end of the queue and updates the `tail`.
#   - Increments the count of elements in the queue.

# - **`dequeue`**: Removes an element from the front of the queue.
#   - If there is only one element in the queue, removes it and sets `head` and `tail` to `None`.
#   - If there are more than one elements in the queue, removes the `head` element and updates the `head`.
#   - Decrements the count of elements in the queue.

# #### Track Class

# The `Track` class represents a music track with a title and a random length between 5 and 10 seconds.

# - **`__init__`**: Initializes the track with a title and a random length.

# #### MediaPlayerQueue Class

# The `MediaPlayerQueue` class extends the `Queue` class to manage a queue of music tracks.

# - **`add_track`**: Adds a track to the media player queue.
#   - Calls the `enqueue` method of the `Queue` class to add the track.

# - **`play`**: Plays tracks from the media player queue.
#   - While there are tracks in the queue, dequeues a track and plays it for its length.

# ### Visual Representations

# 1. **After Enqueueing 4**:
# ```
# Head -> [4] <- Tail
# ```

# 2. **After Enqueueing 'dog'**:
# ```
# Head -> [4] <-> ['dog'] <- Tail
# ```

# 3. **After Enqueueing 'True'**:
# ```
# Head -> [4] <-> ['dog'] <-> ['True'] <- Tail
# ```

# 4. **After Dequeueing**:
# ```
# Head -> ['dog'] <-> ['True'] <- Tail
# ```

# ### Time and Space Complexities

# - **Node class**:
#   - `__init__`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)

# - **Queue class**:
#   - `__init__`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)
#   - `enqueue`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)
#   - `dequeue`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)

# - **Track class**:
#   - `__init__`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)

# - **MediaPlayerQueue class**:
#   - `add_track`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)
#   - `play`: 
#     - Time Complexity: \(O(n \cdot t)\) (where \(n\) is the number of tracks and \(t\) is the average length of a track)
#     - Space Complexity: \(O(1)\)"""