from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    """
    Class to handle a node of a linked list
    """
    data: Any
    next: Any = None


class LinkedList:
    """
    Class of a linked list
    """

    def __init__(self):
        self.head = None

    def add_at_head(self, new_data):
        """
        Functions to add a new node at head of linked list
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_node(self, prev, new_data):
        """
        Function to add new node in middle of linked list
        :param prev: reference to previous node in linked list
        :param new_data: Any data type to store in linked list
        :return:
        """
        if prev is None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prev.next
        prev.next = new_node


