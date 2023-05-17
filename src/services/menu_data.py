import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.add_items_to_menu()

    def read_csv_file(self, path: str):
        with open(path, "r") as menu_file:
            reader = csv.reader(menu_file)
            return list(reader)[1:]

    def add_items_to_menu(self):
        items = self.read_csv_file(self.path)
        for line in items:
            item_name, price, ingredient_name, amount = line
            item = self.find_item_by_name(item_name)
            if not item:
                item = Dish(item_name, float(price))
                self.dishes.add(item)
            ingredient = Ingredient(ingredient_name)
            item.add_ingredient_dependency(ingredient, amount=int(amount))

    def find_item_by_name(self, item_name: str) -> Dish:
        return next(
            (item for item in self.dishes if item.name == item_name), None
        )
