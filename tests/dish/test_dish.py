from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
from pytest import fixture, raises


@fixture
def ingredient1():
    return Ingredient("queijo mussarela")


@fixture
def ingredient2():
    return Ingredient("farinha")


@fixture
def ingredient3():
    return Ingredient("ovo")


@fixture
def dish1():
    return Dish("Pizza Margherita", 29.99)


@fixture
def dish2():
    return Dish("Pizza Margherita", 29.99)


@fixture
def dish3():
    return Dish("Alfredo", 25.80)


# Req 2
def test_dish(dish1, dish2, dish3, ingredient1, ingredient2, ingredient3):
    dish = Dish("Pizza", 10.99)
    assert dish1.name == "Pizza Margherita"
    assert dish1.price == 29.99
    assert dish1.recipe == {}

    assert dish1 == dish2
    assert hash(dish1) == hash(dish2)

    assert dish1 != dish3
    assert hash(dish1) != hash(dish3)

    assert repr(dish1) == "Dish('Pizza Margherita', R$29.99)"

    with raises(TypeError):
        Dish("Pizza", "10.99")

    with raises(ValueError):
        Dish("Pizza", -10.99)

    dish1.add_ingredient_dependency(ingredient1, 2)
    dish2.add_ingredient_dependency(ingredient2, 1)
    dish3.add_ingredient_dependency(ingredient3, 3)

    assert dish1.recipe.get(ingredient1) == 2
    assert dish2.recipe.get(ingredient2) == 1
    assert dish3.recipe.get(ingredient3) == 3

    dish1.add_ingredient_dependency(ingredient1, 2)
    dish2.add_ingredient_dependency(ingredient2, 1)
    dish3.add_ingredient_dependency(ingredient3, 3)

    restrictions = dish1.get_restrictions()
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert restrictions == expected_restrictions

    dish1.add_ingredient_dependency(ingredient1, 2)
    dish2.add_ingredient_dependency(ingredient2, 1)
    dish3.add_ingredient_dependency(ingredient3, 3)

    ingredients = dish1.get_ingredients()
    expected_ingredients = {ingredient1}
    assert ingredients == expected_ingredients
