import os
import shutil

folder_path = "zmExport_710990"

# Получаем список всех файлов и папок в папке zmExport_710990
content_list = os.listdir(folder_path)

# Проходимся по каждому объекту в списке
for item in content_list:
    item_path = os.path.join(folder_path, item)  # Получаем полный путь к объекту
    
    # Проверяем тип объекта (файл или папка)
    if os.path.isfile(item_path):
        # Проверяем, является ли файл видео (расширение .mp4 или .avi)
        if item.endswith(".mp4") or item.endswith(".avi"):
            # Перемещение файла в папку zmExport_710990
            shutil.move(item_path, folder_path)
    elif os.path.isdir(item_path):
        # Проходимся рекурсивно по содержимому внутри папки
        for sub_item in os.listdir(item_path):
            sub_item_path = os.path.join(item_path, sub_item)  # Получаем полный путь к объекту внутри папки
            
            # Проверяем тип объекта (файл или папка)
            if os.path.isfile(sub_item_path):
                # Проверяем, является ли файл видео (расширение .mp4)
                if sub_item.endswith(".mp4"):
                    # Перемещение файла в папку zmExport_710990
                    shutil.move(sub_item_path, folder_path)