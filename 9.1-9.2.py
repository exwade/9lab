import os
from PIL import Image
from pathlib import Path

# Функция для обработки изображения (например, изменение размера)
def process_image(image_path, output_path, size=(800, 800)):
    with Image.open(image_path) as img:
        img = img.resize(size)
        img.save(output_path)

def process_images_in_directory(input_dir, output_dir, size=(800, 800)):
    # Создаем выходную директорию, если она не существует
    os.makedirs(output_dir, exist_ok=True)
    
    # Проходим по всем файлам в входной директории
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Проверяем, что это файл изображения (например, форматы JPG, PNG)
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_path = os.path.join(output_dir, filename)
            process_image(input_path, output_path, size)

# Пример использования
input_directory = 'images'
output_directory = 'output_images'
process_images_in_directory(input_directory, output_directory)
