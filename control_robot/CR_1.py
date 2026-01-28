fruits = ["диня", "банан", "мандарин", "груша", "ківі"]
print("Перший фрукт: ", fruits[0])
print("Останній фрукт: ", fruits[-1])

fruits.append("манго")
print("Новий список фруктів: ", fruits)

friends_colors = {
    "Артем": "черний",
    "Вова": "червоний",
    "Валерія": "білий",
}

print("Улюблений колір Артема: ", friends_colors["Артем"])
friends_colors["Валентин"] = "червоний"
print("Оновлений словник: ", friends_colors)

numbers = (15, 16, 17)
print("Сума чисел у кортежі: ", sum(numbers))

#sum() — рахуе суму чисел у кортежі

friends_colors["Артем"] = {
    "колір": "черний",
    "фрукти": [fruits[0], fruits[1]]
}

print("Оновлений словник з фруктами: ", friends_colors)