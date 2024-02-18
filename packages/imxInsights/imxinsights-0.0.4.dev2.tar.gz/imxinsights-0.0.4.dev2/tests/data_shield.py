import os
from pathlib import Path
from typing import AnyStr

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()


class DataShield:
    @staticmethod
    def __generate_key():
        return Fernet.generate_key()

    @classmethod
    def _get_key(cls) -> str:
        key = os.getenv("DATA_KEY")
        if not key:
            raise ValueError("DATA_KEY is not set in the environment.")
        return key

    @staticmethod
    def _write_file(output_file: str, data: AnyStr):
        with open(output_file, "wb") as file:
            file.write(data)

    @staticmethod
    def _load_file(input_file: str) -> AnyStr:
        try:
            with open(input_file, "rb") as file:
                file_data = file.read()
            return file_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {input_file}")
        except Exception as e:
            raise Exception(f"Error loading file {input_file}: {e}")

    @classmethod
    def encrypt(cls, input_file: str) -> bytes:
        try:
            cipher_suite = Fernet(cls._get_key())
            file_data = cls._load_file(input_file)
            encrypted_data = cipher_suite.encrypt(file_data)
            return encrypted_data
        except Exception as e:
            print(f"Encryption failed: {e}")
            return bytes()

    @classmethod
    def encrypt_file(cls, input_file: str, output_file: str):
        cls._write_file(output_file, cls.encrypt(input_file))

    @classmethod
    def decrypt(cls, input_file: str) -> bytes:
        try:
            cipher_suite = Fernet(cls._get_key())
            encrypted_data = cls._load_file(input_file)
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            return decrypted_data
        except Exception as e:
            print(f"Decryption failed: {e}")
            return bytes()

    @classmethod
    def decrypt_file(cls, input_file: str, output_file: str):
        cls._write_file(output_file, cls.decrypt(input_file))


def encrypt_files(src_directory, dest_directory):
    src_path = Path(src_directory)
    dest_path = Path(dest_directory)

    if not src_path.exists() or not src_path.is_dir():
        print(f"Source directory '{src_path}' does not exist or is not a directory.")
        return

    if not dest_path.exists():
        dest_path.mkdir(parents=True, exist_ok=True)
        print(f"Destination directory '{dest_path}' created.")

    data_shield = DataShield()
    for file_path in src_path.iterdir():
        if file_path.is_file() and file_path.suffix == ".xml":
            data_shield.encrypt_file(f"{file_path}", f"{dest_path}/{file_path.stem}-encrypted.xml")


if __name__ == "__main__":
    current_directory = Path.cwd()
    source_directory = current_directory
    destination_directory = f"{current_directory}/test"
    encrypt_files(source_directory, destination_directory)
