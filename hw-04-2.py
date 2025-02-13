def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:  # Перевіряємо, що в рядку три елементи
                    cat_id, name, age = parts
                    cats.append({"id": cat_id, "name": name, "age": int(age)})
        return cats
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []



cats_info = get_cats_info("D:\cats_file.txt")
print(cats_info)
