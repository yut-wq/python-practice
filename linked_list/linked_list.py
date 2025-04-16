class Node:
    """
    Node class for LinkedList.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList implementation in Python.
    A linked list is a linear data structure where elements are stored in nodes,
    and each node points to the next node in the sequence.
    """
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def size(self):
        """Get the length of the linked list."""
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count
    
    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def push_front(self, data):
        """Add a new node with the given data to the beginning of the linked list."""
        new_node = Node(data)
        
        # Set the new node's next to the current head
        new_node.next = self.head
        
        # Update the head to the new node
        self.head = new_node
    
    def push_back(self, data):
        """Add a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        
        # If the list is empty, the new node becomes the head
        if self.is_empty():
            self.head = new_node
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        # Add the new node at the end
        current.next = new_node
    
    def insert(self, data, position):
        """
        Insert a new node with the given data at the specified position.
        If position is out of range, the node is appended to the end.
        """
        # If position is 0, prepend the node
        if position == 0:
            self.push_front(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        # Traverse to the position or the end of the list
        while current and count < position - 1:
            current = current.next
            count += 1
        
        # If we reached the end of the list, append the node
        if not current:
            self.push_back(data)
            return
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        # If the list is empty, do nothing
        if self.is_empty():
            return
        
        # If the head node contains the data to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return
        
        # Search for the node to be deleted
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        # If the data was found, delete the node
        if current.next:
            current.next = current.next.next
    
    def search(self, data):
        """
        Search for a node with the given data.
        Returns True if found, False otherwise.
        """
        current = self.head
        
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def display(self):
        """Display the linked list."""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements) if elements else "Empty list"


# Example usage
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()
    
    # Append elements
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    
    # Display the list
    print("After appending 1, 2, 3:")
    print(linked_list.display())
    
    # Prepend an element
    linked_list.push_front(0)
    
    # Display the list
    print("\nAfter prepending 0:")
    print(linked_list.display())
    
    # Insert an element
    linked_list.insert(1.5, 2)
    
    # Display the list
    print("\nAfter inserting 1.5 at position 2:")
    print(linked_list.display())
    
    # Delete an element
    linked_list.delete(1.5)
    
    # Display the list
    print("\nAfter deleting 1.5:")
    print(linked_list.display())
    
    # Search for elements
    print("\nSearch for 2:", linked_list.search(2))
    print("Search for 5:", linked_list.search(5))
    
    # Get the length
    print("\nLength of the list:", linked_list.size())
