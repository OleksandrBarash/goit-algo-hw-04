def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")

        if not salaries:
            return 0, 0  # Якщо немає валідних зарплат, повертаємо (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0


# Приклад використання:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")