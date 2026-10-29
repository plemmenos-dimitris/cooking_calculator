# Cooking Calculator

A command-line Python program that rescales recipes. It helps when you want to cook
a different number of servings, or when you're short on one ingredient and need to
know how much of everything else to use.

## Features

- Scale all ingredients to the number of servings you want
- If you only have a limited amount of one ingredient, it calculates how much of everything else you need and how many servings you'll get
- Works with any recipe and any number of ingredients
- Checks the user's answers (e.g. no negative amounts or servings)

## How to run

Requires Python 3.

```
python main.py
```

## Example

Scaling a crêpe recipe (10 servings) to the single egg you have:

```
HOW MANY SERVINGS DOES THE RECIPE MAKE: 10
HOW MANY INGREDIENTS DOES IT HAVE? 3
INGREDIENT 1:
  NAME: flour
  AMOUNT: 250
  UNIT(g, ml, pcs, tbsp,...): g
INGREDIENT 2:
  NAME: eggs
  AMOUNT: 3
  UNIT(g, ml, pcs, tbsp,...): pcs
INGREDIENT 3:
  NAME: milk
  AMOUNT: 500
  UNIT(g, ml, pcs, tbsp,...): ml
1. I WANT TO CHANGE THE SERVINGS 
2. I HAVE A LIMITED AMOUNT OF ONE INGREDIENT. 
CHOOSE 1 OR 2: 2
PLEASE CHOOSE A NUMBER FROM THE LIST
1 flour
2 eggs
3 milk
WHICH INGREDIENT : 2
HOW MUCH eggs DO YOU HAVE?
- 1
FOR 1 pcs OF eggs YOU NEED (3.33 servings): 
- 83.33 g flour
- 166.67 ml milk
```

## What I learned

- Turning math into code: both features reduce to the same idea, one scaling factor (rule of three) applied to every ingredient.
- Lists and for loops: keeping names, amounts and units in parallel lists, and mapping the user’s choice (1, 2, 3…) to list positions (0, 1, 2…).
- Validating user input: while loops that keep asking until the answer makes sense, and if/elif/else to show the right message for each case.
- Refactoring: computing the factor once and sharing the output code instead of repeating it in every branch.

## Next steps

- [ ] Handle invalid input gracefully, so the program never crashes (e.g. when the user types letters instead of a number)
- [ ] Support more than one limited ingredient: find which one runs out first and scale the recipe to it
- [ ] Move repeated input checks into reusable functions
- [ ] Convert between units (g ↔ kg, ml ↔ l, tbsp ↔ tsp) and display large amounts nicely (1500 g → 1.5 kg)
- [ ] Save recipes to a file and load them later
- [ ] Build a simple graphical interface