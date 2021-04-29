def groupingDishes(dishes):
    ingredients = {}
    res = []
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredients.get(ingredient) == None:
                ingredients[ingredient] = [dish[0]]
            else:
                ingredients[ingredient] += [dish[0]]
    ings = sorted(ingredients.keys())
    while ings:
        ing = ings.pop(0)
        if len(ingredients[ing]) >= 2:
            res.append([ing] + sorted(ingredients[ing]))
    return res

print(groupingDishes([["Salad","Tomato","Cucumber","Salad","Sauce"],
 ["Pizza","Tomato","Sausage","Sauce","Dough"],
 ["Quesadilla","Chicken","Cheese","Sauce"],
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]))
