import csv

def read_csv_and_calculate_total(file_path):
    items = []
    total_sum = 0

    # Считываем данные из CSV файла
    with open(file_path, newline='', encoding='cp1251') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Пропускаем заголовок
        for row in csvreader:
            product, quantity, price = row
            quantity = int(quantity)
            price = int(price)
            items.append((product, quantity, price))
            total_sum += quantity * price

    # Выводим информацию
    print("Нужно купить:")
    for product, quantity, price in items:
        print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"Итоговая сумма: {total_sum} руб.")

# Пример использования
file_path = 'file.csv'  # Укажите путь к вашему файлу
read_csv_and_calculate_total(file_path)
