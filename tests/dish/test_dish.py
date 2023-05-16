from src.models.dish import Dish, Ingredient
import pytest


@pytest.fixture
def ingredient():
    return Ingredient("queijo mussarela")


# Req 2
def test_dish(ingredient):
    # Test instance creation with valid price
    dish = Dish("Pizza Margherita", 29.99)
    assert dish.name == "Pizza Margherita"
    assert dish.price == 29.99
    assert dish.recipe == {}

    # Test instance creation with invalid price (not a float)
    with pytest.raises(TypeError):
        Dish("Invalid Dish", "price")

    # Test instance creation with invalid price (less than or equal to zero)
    with pytest.raises(ValueError):
        Dish("Invalid Dish", 0)

    # Test __repr__ method
    expected_repr = "Dish('Pizza Margherita', R$29.99)"
    assert repr(dish) == expected_repr

    # Test __eq__ method with the same dish
    dish2 = Dish("Pizza Margherita", 29.99)
    assert dish.__eq__(dish2)

    # Test __eq__ method with different dishes
    dish3 = Dish("Pepperoni Pizza", 35.99)
    assert not dish.__eq__(dish3)

    # Test __hash__ method
    assert hash(dish) == hash(dish2)

    # Test add_ingredient_dependency method
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe == {ingredient: 2}

    # Test get_restrictions method
    ingredient.add_restriction("Vegan")
    assert dish.get_restrictions() == {"Vegan"}

    # Test get_ingredients method
    assert dish.get_ingredients() == {ingredient}


if __name__ == '__main__':
    pytest.main()

