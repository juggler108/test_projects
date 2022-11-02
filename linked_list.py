class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.__next = self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        if type(value) in (ObjList, type(None)):
            self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if type(value) in (ObjList, type(None)):
            self.__next = value


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_indx(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj_by_indx(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n

        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_indx(indx)
        return obj.data if obj else None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev