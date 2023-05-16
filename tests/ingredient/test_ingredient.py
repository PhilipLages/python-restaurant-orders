from src.models.ingredient import Ingredient, Restriction
from pytest import fixture


@fixture
def ingredient1():
    return Ingredient("queijo mussarela")


@fixture
def ingredient2():
    return Ingredient("queijo mussarela")


@fixture
def ingredient3():
    return Ingredient("bacon")


# Req 1
def test_ingredient(ingredient1, ingredient2, ingredient3):
    assert ingredient1.name == "queijo mussarela"

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient1.restrictions == expected_restrictions

    expected_repr = "Ingredient('queijo mussarela')"
    assert repr(ingredient1) == expected_repr

    assert ingredient1.__eq__(ingredient2)

    assert not ingredient1.__eq__(ingredient3)

    assert hash(ingredient1) == hash(ingredient2)

    assert hash(ingredient1) != hash(ingredient3)

    incorrect_repr = "Ingredient queijo mussarela"
    assert repr(ingredient1) != incorrect_repr

    assert ingredient1.name == "queijo mussarela"

    incorrect_restrictions = {Restriction.LACTOSE, Restriction.GLUTEN}
    assert ingredient1.restrictions != incorrect_restrictions
