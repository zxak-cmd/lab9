import re
from collections import Counter
 
 
def word_frequency(text: str) -> dict:
    """Возвращает словарь «слово -> количество» (без учёта регистра и пунктуации)."""
    # \w+ находит слова (буквы и цифры), игнорируя знаки препинания
    words = re.findall(r"\w+", text.lower())
    return dict(Counter(words))
 
 
def most_common_word(freq: dict):
    """Самое частое слово и число его вхождений (None для пустого словаря)."""
    if not freq:
        return None
    word = max(freq, key=freq.get)
    return word, freq[word]
 
 
def main() -> None:
    """Демонстрация на тексте из задания и краевых случаях."""
    text = "Python это круто. Python прост. Python мощен!"
    print(f"Исходный текст: {text}\n")
    
    # Способ 1: очистка, разбиение, dict comprehension
    words = text.lower().replace(".", "").replace("!", "").split()
    word_freq = {word: words.count(word) for word in set(words)}
    print(f"1. Словарь частот (dict comprehension):\n   {word_freq}")
 
    # Способ 2: через цикл с dict.get
    loop_freq = {}
    for word in words:
        loop_freq[word] = loop_freq.get(word, 0) + 1
    print(f"2. Словарь частот (цикл, get):\n   {loop_freq}")
 
    # Способ 3: Универсальная функция (Counter + regex)
    freq = word_frequency(text)
    most_common, count = most_common_word(freq)
    print(f"3. Самое частое слово (универсальная функция):")
    print(f"   {most_common} (встречается {count} раз)\n")
 
    # Проверка краевых случаев
    print("--- Проверка краевых случаев ---")
    print("Пустой текст:", most_common_word(word_frequency("")))
    print("Регистр и пунктуация:", word_frequency("Да, да! ДА? Нет."))
 
 
if __name__ == "__main__":
    main()