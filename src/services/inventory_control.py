from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

from collections import Counter

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe):
        recipe_counter = Counter(recipe)
        inventory_counter = Counter(self.inventory)

        for ingredient, quantity in recipe_counter.items():
            if inventory_counter[ingredient] < int(quantity):
                return False

        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if not recipe:
            return

        if not self.check_recipe_availability(recipe):
            raise ValueError

        for ingredient, quantity in recipe.items():
            self.inventory[ingredient] -= int(quantity)
