class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()   # Most recently used side
        self.right = Node()  # Least recently used side

        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        """Remove node from the linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node):
        """Insert node immediately after the left dummy."""
        next_node = self.left.next

        self.left.next = node
        node.prev = self.left

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as most recently used
        self._remove(node)
        self._insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node

        # Add as most recently used
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.right.prev

            self._remove(lru)
            del self.cache[lru.key]
