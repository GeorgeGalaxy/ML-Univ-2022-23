# ----------------------------------------------------
# Номер студенческого оканчивается на 82 => 82%30 = 22
# Вариант 22: дек и простой выбор
#
# Сложность алгоритма по времени O(n^2)
# Сложность алгоритма по памяти O(1)
# ----------------------------------------------------


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
item2 = Item(4)
item3 = Item(2)
item4 = Item(8)
item5 = Item(10)

main_deq = Deque()
main_deq.push_last(item1)
main_deq.push_first(item2)
main_deq.push_last(item3)
main_deq.push_last(item4)
main_deq.push_last(item5)

main_deq.print()
print('-'*20)

def simple_selection_sort(deque):

    N = deque.get_size()

    for i in range(N - 1):

        min_value = deque.items[i].value
        min_index = i

        for j in range(i + 1, N):
            if min_value > deque.items[j].value:

                min_value = deque.items[j].value
                min_index = j

        if min_index != i:

            temp_value = deque.items[i].value

            deque.items[i].value = deque.items[min_index].value
            deque.items[i].prev = deque.items[min_index - 1].prev

            deque.items[min_index].value = temp_value
            deque.items[min_index].next = deque.items[min_index + 1].value
            deque.items[min_index].prev = deque.items[min_index - 1].value

            deque.items[i].next = deque.items[i + 1].value

            # Изменение соседей
            if i != 0:
                deque.items[i - 1].next = deque.items[i].value
            else:
                pass
            deque.items[i + 1].prev = deque.items[i].value
            deque.items[min_index - 1].next = deque.items[min_index].value
            deque.items[min_index + 1].prev = deque.items[min_index].value

    return deque

main_deq = simple_selection_sort(main_deq)
main_deq.print()
