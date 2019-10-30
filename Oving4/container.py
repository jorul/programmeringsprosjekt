"""Super-class Container and sub-classes Stack and Queue"""
import abc


class Container:
    """Super-class"""
    def __init__(self):
        self.items = []

    def size(self):
        """Return number of elements in self.items"""
        return len(self.items)

    def is_empty(self):
        """Check if self.items is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Add item to end of self.items"""
        self.items.append(item)

    @abc.abstractmethod
    def pop(self):
        """Pop off the correct element of self.items,nand return it
        This method differs between subclasses, hence is not
        implemented in the superclass"""
        raise NotImplementedError

    def peek(self):
        """Return the top element without removing it
        This method differs between subclasses , hence is not
        implemented in the super class"""
        raise NotImplementedError


class Queue(Container):
    """Subclass"""
    def __init__(self):
        self.items = []

    def peek(self):
        # Return the first element of the list, do not delete it
        assert not self.is_empty()
        return self.items[0]

    def pop(self):
        # Pop off the first element
        assert not self.is_empty()
        return self.items.pop(0)


class Stack(Container):
    """Subclass"""
    def __init__(self):
        self.items = []

    def peek(self):
        # Return the last element of the list, do not delete it
        assert not self.is_empty()
        return self.items[-1]

    def pop(self):
        # Pop off the last element
        assert not self.is_empty()
        return self.items.pop(-1)
