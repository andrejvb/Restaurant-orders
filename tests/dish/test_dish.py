import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction 


# Req 2
def test_dish():
    dish = Dish("Lasanha", 35)
    dish1 = Dish("Omelete", 25)
    dish2 = Dish("Lasanha", 35)
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("carne")
    ingredient3 = Ingredient("massa de lasanha")

    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    dish.add_ingredient_dependency(ingredient3, 3)

    mock_ingredients = {
        Ingredient("queijo mussarela"),
        Ingredient("carne"),
        Ingredient("massa de lasanha"),
    }

    mock_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT, Restriction.GLUTEN}

    ingredients = dish.get_ingredients()
    restrictions = dish.get_restrictions()

    assert ingredients == mock_ingredients
    assert restrictions == mock_restrictions
    assert dish.name == "Lasanha"
    assert dish.price == 35

    assert repr(dish) == "Dish('Lasanha', R$35.00)"
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('Lasanha', '10')
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."):
        Dish('Omelete', 0)

    assert dish == dish2
    assert dish != dish1

    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish1)







