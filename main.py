from missions import *

def main():
    show_missions(MISSIONS)

if __name__ == "__main__":
    main()

direction = input("Введите направление для поиска: ")
results = find_missions_by_direction(direction)

if results:
    print("=== Результаты поиска ===")
    for i, m in enumerate(results, start=1):
        print(f"{i}. {m['name']}")
        print(f"Год запуска: {m['year']}")
        print(f"Направление: {m['direction']}")
        print()
else:
    print("Миссии по такому направлению не найдены.")