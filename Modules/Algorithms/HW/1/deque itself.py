class Item:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push_first(self, item):
        self.items.insert(0, item)

        if self.get_size() > 1:
            self.items[0].next = self.items[1].value
            self.items[1].prev = self.items[0].value
        else:
            pass


    def push_last(self, item):
        self.items.append(item)

        if self.get_size() > 1:
            self.items[-1].prev = self.items[-2].value
            self.items[-2].next = self.items[-1].value
        else:
            pass

    def remove_first(self):
        self.items.pop(0)
        self.items[0].prev = None

    def remove_last(self):
        self.items.pop()
        self.items[-1].next = None

    def get_size(self):
        return len(self.items)

    def print(self):
        for i, el in enumerate(self.items):
            print(f'"{i}" element is {el.value} '
                  f'(prev = {el.prev}, next = {el.next})')

item1 = Item(1)
item2 = Item(2)
item3 = Item(3)
item4 = Item(8)

# main_deq = Deque()
# main_deq.push_last(item1)
# main_deq.push_first(item2)
# main_deq.push_last(item3)
# main_deq.push_last(item4)
#
# main_deq.print()
# print()
#
# main_deq.remove_last()
#
# main_deq.print()
# print()
#
# main_deq.remove_first()
#
# main_deq.print()
# print()
