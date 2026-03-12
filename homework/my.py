import math

# Словарь разрешенных функций, чтобы math.sqrt можно было писать просто как sqrt
safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

print("--- Продвинутый текстовый калькулятор ---")
print("Можно использовать: +, -, *, /, **, sqrt, sin, cos, pi и т.д.")
print("Введите 'exit' для выхода.")

while True:
    user_input = input("\nВведите пример: ").lower().replace('^', '**')

    if user_input == 'exit':
        break

    try:
        # eval вычисляет строку как код, safe_dict дает доступ к math
        result = eval(user_input, {"__builtins__": None}, safe_dict)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка в расчетах: {e}")
