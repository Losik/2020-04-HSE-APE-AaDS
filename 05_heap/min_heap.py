import sys
from io import StringIO


class MinHeap:

    def __init__(self, arr=None):
        """Creates a heap from given list if provided"""
        if arr is None:
            self.arr = []
        else:
            self.arr = arr
            self._heapify()

    def add(self, value: int):
        """Add value to the heap"""
        self.arr.append(value)
        self._sift_up(len(self.arr) - 1)

    def min(self):
        """Returns minimal element from the heap"""
        return self.arr[0]

    def extract_min(self):
        """Returns minimal element from the heap and returns its value"""
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        value = self.arr.pop()
        self._sift_down(0)
        return value

    def clear(self):
        """Removes all element from the heap"""
        self.arr.clear()

    def _sift_up(self, cur: int):
        """
        Restores heap invariants if they are possibly broken
        for cur node's parents. Meaning that cur node is a root
        of a valid heap tree but it might be less than its parent
        """
        par = (cur - 1) // 2

        while cur != 0 and self.arr[cur] < self.arr[par]:
            self.arr[cur], self.arr[par] = self.arr[par], self.arr[cur]
            cur = par
            par = (cur - 1) // 2

    def _sift_down(self, cur):
        """
        Restores heap invariant if they are possibly broken
        for cur node. Meaning that cur is grater or equal to
        its parent and both cur node's childs are valid heaps
        """
        left = 2 * cur + 1
        right = 2 * cur + 2

        while left < len(self.arr):

            min_child = left
            if right < len(self.arr) and self.arr[right] < self.arr[min_child]:
                min_child = right

            if self.arr[cur] <= self.arr[min_child]:
                break

            self.arr[cur], self.arr[min_child] = self.arr[min_child], self.arr[cur]
            cur = min_child
            left = 2 * cur + 1
            right = 2 * cur + 2

    def _heapify(self):
        """Makes self.arr into a valid heap"""
        last_inner_node = (len(self.arr) - 1) // 2
        for cur in range(last_inner_node, -1, -1):
            self._sift_down(cur)

    def __bool__(self):
        """Used in `if min_heap:` expressions"""
        return bool(self.arr)

    def __str__(self):
        string_io = StringIO()
        stack = [(0, 0)]
        while stack:
            cur, indent = stack.pop()
            if cur < len(self.arr):
                string_io.write(f"{' ' * indent}{self.arr[cur]}\n")
                stack.append((2 * cur + 2, indent + 1))
                stack.append((2 * cur + 1, indent + 1))

        return string_io.getvalue()


def main():
    min_heap = MinHeap()

    for line in sys.stdin:
        if line.startswith('ADD'):
            value = int(line.split(' ', 1)[1])
            min_heap.add(value)
        elif line.startswith('EXTRACT'):
            print(min_heap.extract_min() if min_heap else 'CANNOT')
        elif line.startswith('CLEAR'):
            min_heap.clear()
        else:
            raise RuntimeError(f'Unknown command {line}')


if __name__ == '__main__':
    main()
