import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.store = {}
        self.dishes = set()
        self._read_data(source_path)

    def _read_data(self, source_path: str) -> None:
        with open(source_path, encoding="utf-8") as file:
            arquivo_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = arquivo_reader

        for prato in data:
            self._process_prato(prato)

    def _process_prato(self, prato) -> None:
        dish_name, dish_price, ingredient_name, ingredient_amount = prato
        dish_price = float(dish_price)
        ingredient_amount = int(ingredient_amount)

        # Cria ou recupera o prato do dicionário store
        dish = self.store.get(dish_name)
        if not dish:
            dish = Dish(dish_name, dish_price)
            self.store[dish_name] = dish

        # Cria o ingrediente e adiciona à receita do prato
        ingredient = Ingredient(ingredient_name)
        dish.add_ingredient_dependency(ingredient, ingredient_amount)

        # Adiciona o prato ao conjunto de dishes
        self.dishes.add(dish)  


if __name__ == "__main__":
    menu = MenuData('data/menu_base_data.csv')
    print(menu.dishes)       