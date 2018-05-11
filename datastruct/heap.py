class BinaryHeap(object):
    def __init__(self):
        self.current_size = 0
        self.heap_list = [0]

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]

    def insert(self, key):
        self.heap_list.append(key)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_down(self, index):
        while index * 2 <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                self.heap_list[index], self.heap_list[mc] = self.heap_list[mc], self.heap_list[index]

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if index * 2 + 1 > index * 2:
                return index * 2
            else:
                return index * 2 + 1

    def delete_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return retval

    def build_heap(self, alist):
        index = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (index > 0):
            self.percolate_down(index)
            index -= 1
