"""
- Go to any project
- create a file called test.py
- and paste following code
- make sure you are in current working directory (where test.py exists)
- then run `pytest <file-name>`
"""
 
 
import pytest
 
 
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False
 
    def cube(self):
        self.cubed = True
 
 
class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()
 
    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()
 
 
# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]
 
 
def test_fruit_salad(fruit_bowl):
 
    breakpoint()
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)
 
    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
 
 
def random_method(fruit_bowl):
    breakpoint()

