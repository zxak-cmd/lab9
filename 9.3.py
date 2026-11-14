from itertools import islice
from typing import Iterator
 
 
def fibonacci() -> Iterator[int]:
    """Бесконечный генератор чисел Фибоначчи."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
 
 
def main() -> None:
    """Выводит первые 10 чисел разными способами."""
    gen = fibonacci()
    print("Через next():", [next(gen) for _ in range(10)])
    print("Продолжение того же генератора:", [next(gen) for _ in range(3)])
 
    print("Через islice:", list(islice(fibonacci(), 10)))
 
    print("Через цикл с break:", end=" ")
    for i, number in enumerate(fibonacci()):
        if i == 10:
            break
        print(number, end=" ")
    print()
 
    # Первое число Фибоначчи больше миллиона — без хранения всей последовательности
    print("Первое число > 1 000 000:", next(x for x in fibonacci() if x > 1_000_000))
 
 
if __name__ == "__main__":
    main()