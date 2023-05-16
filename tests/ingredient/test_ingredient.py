from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    assert ingredient1.name == "queijo mussarela"

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient1.restrictions == expected_restrictions

    expected_repr = "Ingredient('queijo mussarela')"
    assert repr(ingredient1) == expected_repr

    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient2

    ingredient3 = Ingredient("bacon")
    assert ingredient1 != ingredient3

    assert hash(ingredient1) == hash(ingredient2)

    assert hash(ingredient1) != hash(ingredient3)

    incorrect_repr = "Ingredient queijo mussarela"
    assert repr(ingredient1) != incorrect_repr

    assert ingredient1.name == "queijo mussarela"

    incorrect_restrictions = {Restriction.LACTOSE, Restriction.GLUTEN}
    assert ingredient1.restrictions != incorrect_restrictions
