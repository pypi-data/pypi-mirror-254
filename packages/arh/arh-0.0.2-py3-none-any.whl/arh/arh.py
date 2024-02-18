from PIL import Image
from tqdm import tqdm
import pytesseract
import pandas as pd
# import easyocr
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger, PageObject
from pdf2image import convert_from_path



from multiprocessing import Process, Manager, Lock, Pool
from concurrent.futures import ThreadPoolExecutor

import os
import json
import re
import shutil


import threading
from queue import Queue






class Archivarius():

    def get_text(self, image_path, delete_file = False):
        '''Извлекаем текст с помощью Easyocr
        
        Args:
            image_path (str): полный путь до jpg файла
            
            delete_file (bool): удаление файла после извлечения текста

        Return:
            text (str): извлеченный текст с изображения 

        '''
        reader = easyocr.Reader(['ru'])
        result = reader.readtext(image_path, detail = 0)

        text = ''.join(result)
        result = text.lower()
        result = result.replace('\n', ' ')
        
        if delete_file == True:
            os.remove(image_path)
        
        return text

    def get_text_ts(
            self, image_path, delete_file = False, 
            path_tes = None,
            ):


        '''Извлекаем текст с помощью Tesseract

        Args:
            image_path (str): полный путь до jpg файла
            
            delete_file (bool): удаление файла после извлечения текста

        Return:
  
                      text (str): извлеченный текст с изображения 

            '''

        if path_tes == None:
            raise Exception ('Не указан путь до тисеракта в переменную path_tes')


        pytesseract.pytesseract.tesseract_cmd = path_tes
        Image.MAX_IMAGE_PIXELS = 9999218750

        text = pytesseract.image_to_string(image_path, lang='rus')
        text = text.lower()
        text = text.replace('\n', ' ')

        if delete_file == True:
            os.remove(image_path)

        return text

    def tiff_or_png_to_jpg(self, file, path):
        '''Конвертирует PNG-файл в JPG-файл
        
        Args:
            
            file (str): название файла 

            path (str): путь где лежит файл

        Return: None

            Сохраняет файл в тойже дериктории 
   
        '''
        try:
            # Замените 'input.tif' и 'output.jpg' на соответствующие имена ваших файлов
            input_tif = path + '\\' + file
            output_jpg = path + '\\' + file[:-4] + '.jpg'

            # Открываем TIFF-изображение
            with Image.open(input_tif) as img:
                if img.mode != "RGB":
                    img = img.convert("RGB")
                # Конвертируем и сохраняем его в формате JPEG
                img.save(output_jpg, 'JPEG')
        except Exception as exc:
            print(exc)
            pass

    def jpeg_to_jpg(self, file, path):
        '''Конвертирует JPEG-файл в JPG-файл
        
        Args:
            
            file (str): название файла 

            path (str): путь где лежит файл

        Return: None

            Сохраняет файл в тойже дериктории 

        '''
        new_filename = os.path.join(path, file.replace(".jpeg", ".jpg"))
        os.rename(os.path.join(path, file), new_filename)

    def jpg_to_pdf(self, file, path):
        '''Конвертирует JPG-файл в PDF-файл
        
        Args:
            
            file (str): название файла 

            path (str): путь где лежит файл

        Return: None

            Сохраняет файл в тойже дериктории 

        '''
        
        image_paths = os.path.join(path, file)
        pdf_path = os.path.join(path, file.replace(".jpg", ".pdf"))

        with open(pdf_path, "wb") as f:
                    f.write(img2pdf.convert(image_paths, rotation=img2pdf.Rotation.ifvalid))

class PDF_Toolbox():
    ''' Класс для работы с пдф файлами

        Metods :
            two_in_one_list_pdf_soft : Создает файл pdf 2 листа на одном в новой директории.
            
            extract_text_from_pdf : Возращает текст из файла pdf.

            split_pdf : Разделяет по стронично PDF файл

            merge_pdfs : Объединяет два файла PDF в один

            f103 : Разделяет файл на 3 листа первая середина и последняя.

    '''


    def two_in_one_list_pdf_soft(self, path, new_path):
        '''Создает файл pdf 2 листа на одном в новой директории

        Args:
            path (str): путь до файла.

            new_path (str): путь куда сохранить новый файл

        Return:
            Сохраняет файл по новому пути.
        
        '''

        # Проверка на пустой файл
        if os.path.getsize(path) == 0:
            print(f"Ошибка: Файл {path} пустой.")
            return

        reader = PdfFileReader(open(path, 'rb'), strict=False)
        writer = PdfFileWriter()
        num = 0
        pageNum = reader.numPages
        if pageNum > 1:
            while num < pageNum-1:
                min_page = reader.getPage(num)

                big_page = PageObject.createBlankPage(None, min_page.mediaBox.getWidth()*2, min_page.mediaBox.getHeight())
                #mergeScaledTranslatedPage(page2, scale, tx, ty, expand=False)
                big_page.mergeScaledTranslatedPage(reader.getPage(num), 1, 0, 0)
                if num + 1 < pageNum:
                    if reader.getPage(num + 1).mediaBox.getWidth() > 600:

                        big_page.mergeScaledTranslatedPage(reader.getPage(num + 1), 1, float(min_page.mediaBox.getWidth()), 0)
                        writer.addPage(big_page)
                    else:
                        big_page.mergeScaledTranslatedPage(reader.getPage(num + 1), 1, float(min_page.mediaBox.getWidth()), 0)
                        writer.addPage(big_page)
                num = num + 2
            if pageNum % 2 == 1:
                min_page = reader.getPage(num)
                big_page = PageObject.createBlankPage(None, min_page.mediaBox.getWidth() * 2, min_page.mediaBox.getHeight())
                big_page.mergeScaledTranslatedPage(reader.getPage(num), 1, 0, 0)
                writer.addPage(big_page)

            file_name = os.path.basename(path)
            new_path = os.path.join(new_path, file_name)

            with open(new_path[:-4] + '_2for1.pdf', 'wb') as f:
                writer.write(f)
        else:
            shutil.copy(path, new_path)

    def extract_text_from_pdf(self, pdf_path):
        ''' Возращает текст из файла pdf.
        
        Args:
            pdf_path (str): путь к pdf файлу.

        Return:
            text (str): текст из файла pdf.
        '''
        text = ""

        # Открывает pdf файл
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfFileReader(file)
            num_pages = pdf_reader.numPages

        # Получаем текст из всех страниц
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()

        # Возращаем текст
        return text

    def split_pdf(self, input_pdf_path, output_folder):
        '''Разделяет по стронично PDF файл
        
        Args:
            input_pdf_path (str): Файл pdf для разделения.

            output_folder (str): Путь к папке для сохранения.

        Return:
            Ничего

        '''

        # Открываем PDF-файл для чтения
        with open(input_pdf_path, 'rb') as pdf_file:
            # Создаем объект для работы с PDF
            pdf_reader = PdfFileReader(pdf_file)

            # Проходим по каждой странице и создаем отдельные PDF-файлы
            for page_num in range(pdf_reader.numPages):
                # Создаем новый объект для записи в новый файл
                pdf_writer = PdfFileWriter()

                # Получаем текущую страницу
                page = pdf_reader.getPage(page_num)

                # Добавляем страницу к новому файлу
                pdf_writer.addPage(page)

                # Создаем имя нового файла
                output_file_path = f"{output_folder}/page_{page_num + 1}.pdf"

                # Открываем новый файл для записи
                with open(output_file_path, 'wb') as output_pdf:
                    # Записываем страницу в новый файл
                    pdf_writer.write(output_pdf)

    def merge_pdfs(self, input_pdf1, input_pdf2, output_pdf):
        '''Объединяет два файла PDF в один

        Args:
            input_pdf1 (str): Путь до первого файла   

            input_pdf2 (str): Путь до второго файла

            output_pdf (str): Путь куда сохранить файл и его название

        Return:
            None
    
        '''

        merger = PdfMerger()

        # Добавляем первый PDF
        merger.append(input_pdf1)

        # Добавляем второй PDF
        merger.append(input_pdf2)

        # Сохраняем объединенный PDF
        merger.write(output_pdf)

        # Закрываем объединитель
        merger.close()

    def f103(self, input_path:str, output_path:str):
        '''Разделяет файл на 3 листа первая середина и последняя.
        
        Args:
            input_path (str): прямой путь к файлу;\n

            output_path (str): в какую папку сохранить файл.\n

        Return: None

            Сохраняет файл в новой папке

        '''
        file = input_path.split('\\')[-1]
        filename = file.split('.')[-2]

        try:
            with open(input_path, 'rb') as file:
                pdf_reader = PdfFileReader(file)
                
                if pdf_reader.numPages <= 0:
                    print("Ошибка: Пустой файл")
                    return

                for num in range(1, pdf_reader.numPages-1):
                    pdf_writer = PdfFileWriter()

                    page = pdf_reader.getPage(0)
                    pdf_writer.addPage(page)

                    page = pdf_reader.getPage(num)
                    pdf_writer.addPage(page)

                    page = pdf_reader.getPage(pdf_reader.numPages-1)
                    pdf_writer.addPage(page)

                    # Открываем файл для записи объединенного PDF
                    with open(f'{output_path}\{filename}_{num+1}.pdf', 'wb') as output_file:
                        # Записываем содержимое PdfFileWriter в выходной файл
                        pdf_writer.write(output_file)

                pdf_writer = PdfFileWriter()

                page = pdf_reader.getPage(0)
                pdf_writer.addPage(page)

                page = pdf_reader.getPage(pdf_reader.numPages-1)
                pdf_writer.addPage(page)

                # Открываем файл для записи объединенного PDF
                with open(f'{output_path}\{filename}_{1}.pdf', 'wb') as output_file:
                    # Записываем содержимое PdfFileWriter в выходной файл
                    pdf_writer.write(output_file)

            print(f"Успешно создан новый PDF-файл")

        except FileNotFoundError:
            print(f"Ошибка: Файл не найден: {input_path}")
        except PermissionError:
            print(f"Ошибка: Недостаточно прав для доступа к файлу: {input_path}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def pdf_to_jpg(self, file, path):
        '''Конвертирует pdf файл в jpg
        
            Args:
                file (str): название файла

                path (str): путь где лежит файл

            Returns: None

                Сохраняет картинку в той же папке
        '''
        try:
            # Конвертируем PDF в изображения
            images = convert_from_path(path + '\\' +  file, poppler_path=r'M:\Analytics\a.shulegin\job\liberty\poppler-23.08.0\Library\bin')

            # Перебираем каждую страницу и сохраняем ее как отдельное изображение
            for i, image in enumerate(images):
                output_file = f'{file[:-4]}_page_{i + 1}.jpg'  # Создаем уникальное имя для каждой страницы
                image.save(path + '\\' + output_file, 'JPEG')
        except Exception as exc:
            print(exc)
            pass


class Model_Tolboox(Archivarius, PDF_Toolbox):

    def convert_file(self, file, path):
        '''Конвертирует файл в jpg
        
        Сейчас потдерживает такие форматы как:

            - PNG

            - TIF

            - JPEG

        Args:

            file (str): название файла

            path (str): директория в которой он лежит

        Return: None

            Сохраняет файл в исходной директории 

        '''
        if 'pdf' in file:
            self.pdf_to_jpg(file, path)
        if 'png' in file or 'tif' in file:
            self.tiff_or_png_to_jpg(file, path)
        if '.jpeg' in file:
            self.jpeg_to_jpg(file, path)

    def get_text_in_image_pdf(self, path):
        '''Конвертирует все файлы в директории в JPG-файлы 
        и извлекает из них тектст, сохраняет в TXT-файл в формате:
        {'Полный путь': 'Текст из фотографии'}

        Args:
            
        path (str): путь до директории где лежат файлы

        Returns: None

            Сохраняет результат в result.txt

        '''

        print('[!] Конвертация файлов')
        for direct, folder, files in os.walk(path):
            for file in tqdm(files):
                self.convert_file(file, direct)
        print('[!] Конвертация файлов завершена')


        print('[!] Идет извлечение текста')
        for direct, folder, files in os.walk(path):
            for file in tqdm(files):
                if 'jpg' in file:
                    fullpath = os.path.join(direct, file)
                    text = self.get_text_ts(fullpath)
                    
                    with open('result.txt', 'a', encoding='utf-8') as f:
                        f.write(str({fullpath: text}))
                        f.write('\n')
        print('[!] Извлечение текста закончено')

    def get_text_in_pdf(self, path):
        '''Извлекает текст из PDF-файла и сохраняет в TXT-файл
        в формате: {'Полный путь': 'Текст из фотографии'}

        Args:
            
            path (str): путь до директории где лежат файлы

        Returns: None

            Сохраняет результат в result.txt

        '''


        print('[!] Идет извлечение текста')
        for direct, folder, files in os.walk(path):
            for file in tqdm(files):
                if 'pdf' in file:
                    fullpath = os.path.join(direct, file)
                    text = self.extract_text_from_pdf(fullpath)
                    
                    if text:
                        with open('result.txt', 'a', encoding='utf-8') as f:
                            f.write(str({fullpath: text}))
                            f.write('\n')
                    else:
                        print(f'У файла {fullpath} нет текста')

        print('[!] Извлечение текста закончено')

    def res_sorted(self, file, cl_class, cl_path):
        '''Открывает итоговый файл и сортирует файлы по классам
        
        В нем должено содержаться:

            - Колонка с полным путем до файла

            - Колонка с номером класса к которому относиться файл

        Args:

            file (str): путь до Excel-файла

            cl_class (str): Название колонки с классами

            cl_path (str): Название колонки с полными путями к файлам

        Return: None

            Создает в текущей дериктории папку promes_resulte_*name с классифицированными делами

        '''
        df = pd.read_excel(file)
        path_list = {}
        clases = {}
        name = file.split('\\')[-1]
        name = name.split('.')[0]
        for path, clas in tqdm(zip(df['path'], df['class_name'])):
            '''Сортеруем файлы по классу название папки = номер класса'''
            try:    
                file = path.split('\\')
                fio = file[-3].split('_')
                fio = fio[-1]
                
                folder_path = f'promes_resulte_{name}' + '\\' + fio + '\\' + str(clas)
                
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                shutil.copy2(path, folder_path + '\\' + file[-1])
                path_list[folder_path] = fio
                clases[folder_path] = clas
            except Exception as exc:
                passs


class Model_Tolboox_mult(Archivarius, PDF_Toolbox):

    def process_files_in_directory(self, path):
        print('[!] Идет извлечение текста')

        def process_file(file):
            if 'pdf' in file:
                fullpath = os.path.join(path, file)
                text = self.extract_text_from_pdf(fullpath)

                if text:
                    with self.lock:
                        with open('result.txt', 'a', encoding='utf-8') as f:
                            f.write(str({fullpath: text}))
                            f.write('\n')
                else:
                    print(f'У файла {fullpath} нет текста')

        with ThreadPoolExecutor(max_workers=28) as executor:
            files = [os.path.join(direct, file) for direct, _, files in os.walk(path) for file in files]
            list(tqdm(executor.map(process_file, files), total=len(files)))

        print('[!] Извлечение текста закончено')

    def process_files_in_directory2(self, path):
        print('[!] Идет извлечение текста')

        def process_file(fullpath):
            try:
                if 'pdf' in fullpath:
                    text = self.extract_text_from_pdf(fullpath)

                    if text:
                        with open('result2.txt', 'a', encoding='utf-8') as f:
                            f.write(str({fullpath: text}))
                            f.write('\n')
                    else:
                        print(f'У файла {fullpath} нет текста')
            except Exception as e:
                print(f'Ошибка при обработке файла {fullpath}: {e}')

        files = [os.path.join(direct, file) for direct, _, files in os.walk(path) for file in files]
        threads = []

        for file in tqdm(files, total=len(files)):
            thread = threading.Thread(target=process_file, args=(file,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print('[!] Извлечение текста закончено')

    # def process_image(self, file):
    #     print('5')

    #     text = self.extract_text_from_pdf(file)

    #     if text:
    #         with open('result2.txt', 'a', encoding='utf-8') as f:
    #             f.write(str({file: text}))
    #             f.write('\n')
    #     print('6')

#     def МУЛЬТИПОТОЧНОСТЬ!!!!!!!!!!!!!!!!!!(self, files_list:list):

#         with tqdm(total=len(files_list)) as pbar:
#             def update(*a):
#                 pbar.update()


#         print('3')
#         # Создаем пул процессов и отслеживаем прогресс; Pool(*), где *- это кол-во потоков
#         with Pool(8) as pool:
#             for _ in pool.imap_unordered(self.process_image, files_list):
#                 update()
#         print('4')


# if __name__ == '__main__':
#     model = Model_Tolboox_mult()
#     path = r'M:\Документы БД\_2024 Прикрепление файлов клиентов\01.09 ГК_16 досье\ГК_16\приложение\приложение к договору уступки ФАЛКОН_ГЛ 30.11.2023'
#     result = []

#     print('1')
#     for direct, folder, files in os.walk(path):
#         for file in files:
#             if 'pdf' in file:
#                 fullpath = os.path.join(direct, file)
#                 result.append(fullpath)
#     print('2')

#     model.xz(result)
