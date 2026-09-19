import math

class Calculator:
    """Универсальный калькулятор с поддержкой базовых и инженерных операций."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Ошибка: Деление на ноль невозможно!")
        return a / b

    def power(self, base: float, exp: float) -> float:
        return math.pow(base, exp)

    def square_root(self, val: float) -> float:
        if val < 0:
            raise ValueError("Ошибка: Извлечение корня из отрицательного числа!")
        return math.sqrt(val)


def main():
    calc = Calculator()
    print("=== Smart Calculator CLI ===")
    print("Доступные операции: +, -, *, /, ^ (степень), sqrt (корень)")
    
    while True:
        try:
            op = input("\nВведите операцию (+, -, *, /, ^, sqrt) или 'exit' для выхода: ").strip()
            if op.lower() == 'exit':
                print("Завершение работы.")
                break

            if op in ['+', '-', '*', '/', '^']:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                
                if op == '+':
                    print(f"Результат: {calc.add(a, b)}")
                elif op == '-':
                    print(f"Результат: {calc.subtract(a, b)}")
                elif op == '*':
                    print(f"Результат: {calc.multiply(a, b)}")
                elif op == '/':
                    print(f"Результат: {calc.divide(a, b)}")
                elif op == '^':
                    print(f"Результат: {calc.power(a, b)}")

            elif op == 'sqrt':
                a = float(input("Введите число: "))
                print(f"Результат: {calc.square_root(a)}")

            else:
                print("Неизвестная операция, попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
