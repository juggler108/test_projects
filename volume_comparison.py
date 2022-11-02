class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

    def __len__(self):
        return self.dim.a * self.dim.b * self.dim.c


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError('Right operand must be Track type')
        return self.__dim_value(self) < self.__dim_value(other)

    def __le__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError('Right operand must be Track type')
        return self.__dim_value(self) <= self.__dim_value(other)

    @classmethod
    def __dim_value(cls, obj):
        return obj.a * obj.b * obj.c

    def __validate(self, obj):
        return self.MIN_DIMENSION <= obj <= self.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__validate(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__validate(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__validate(value):
            self.__c = value


sneakers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))

lst_shop = [sneakers, umbrella, fridge, chair]

lst_shop_sorted = sorted(lst_shop, key=len)

for i in lst_shop_sorted:
    print(i.name)
