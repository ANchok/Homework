from pprint import pprint


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name: str = file_name

    def get_products(self) -> str:
        file = open(self.__file_name, 'r')
        products: str = file.read()
        file.seek(0)
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for product in products:
            file_str = file.read()
            if product.name in file_str:
                print(f'Продукт {str(product)} уже есть в магазине')
                file.seek(0)
            else:
                file.write(str(product) + '\n')
        file.close()


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())