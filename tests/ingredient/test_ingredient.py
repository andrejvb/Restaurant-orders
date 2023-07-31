from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente1 = Ingredient("queijo mussarela")
    ingrediente2 = Ingredient("farinha") 
    expected_repr = "Ingredient('queijo mussarela')"
    
    assert ingrediente1.restrictions == {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingrediente2.restrictions == {Restriction.GLUTEN}
    assert repr(ingrediente1) == expected_repr
    assert ingrediente1 != ingrediente2

    ingrediente1a = Ingredient("ovo")
    ingrediente1b = Ingredient("ovo")

    assert ingrediente1a.name == "ovo"
    assert ingrediente1a == ingrediente1b
    assert hash(ingrediente1a) == hash(ingrediente1b)
    assert hash(ingrediente1a) != hash(ingrediente2)



