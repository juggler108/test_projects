class StrValidate:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str:
            setattr(instance, self.name, value)
        else:
            raise ValueError('Invalid value')


class ValValidate:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float):
            setattr(instance, self.name, value)
        else:
            raise ValueError('Invalid value')


class Ingredient:
    name = StrValidate()
    volume = ValValidate()
    measure = StrValidate()

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self.list_of_ingredients = list(args)

    def add_ingredient(self, ing):
        self.list_of_ingredients.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.list_of_ingredients:
            self.list_of_ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.list_of_ingredients)

    def __len__(self):
        return len(self.list_of_ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3