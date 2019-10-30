
import unittest
from container import Stack, Queue


class TestContainter(unittest.TestCase):

    def test_stack(self):
        test_stack = Stack()
        for i in range(0, 5):
            test_stack.push(i)
        counter = 4
        while test_stack.is_empty() is not True:
            self.assertTrue(test_stack.peek() == counter)
            test_stack.pop()
            counter -= 1
        self.assertTrue(test_stack.is_empty())

    def test_queue(self):
        test_queue = Queue()
        for i in range(0, 5):
            test_queue.push(i)
        counter = 0
        while test_queue.is_empty() is not True:
            self.assertTrue(test_queue.peek() == counter)
            test_queue.pop()
            counter += 1
        self.assertTrue(test_queue.is_empty())

if __name__ == '__main__':
    unittest.main()
