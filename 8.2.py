def unique_sorted(ips: list) -> list:
    """Уникальные адреса, отсортированные лексикографически (как std::set в C++)."""
    return sorted(set(ips))
 
 
def unique_sorted_numeric(ips: list) -> list:
    """Уникальные адреса, отсортированные по числовым значениям октетов."""
    return sorted(set(ips), key=lambda ip: tuple(int(part) for part in ip.split(".")))
 
 
def main() -> None:
    """Демонстрация на примере журнала запросов."""
    ips = [
        "192.168.1.10", "10.0.0.2", "192.168.1.10", "10.0.0.10",
        "172.16.0.5", "10.0.0.2", "192.168.1.1", "172.16.0.5",
    ]
    print(f"Всего записей: {len(ips)}, уникальных: {len(set(ips))}")
    print("Множество (порядок не гарантирован):", len(set(ips)), "элементов")
    print("Лексикографически:", unique_sorted(ips))
    print("По числовым октетам:", unique_sorted_numeric(ips))
    print("Пустой список:", unique_sorted([]))
 
 
if __name__ == "__main__":
    main()