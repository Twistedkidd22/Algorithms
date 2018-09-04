#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    maxBatches = float('inf')
    for i in recipe:
        ingredient = ingredients.get(i, 0)
        batches = ingredient // recipe[i]
        if batches < maxBatches:
            maxBatches = batches
    return maxBatches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
