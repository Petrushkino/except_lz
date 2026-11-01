import pandas as pd
import os

class StructureMismatchError(Exception):
    """Собственное исключение для ошибок структуры датафрейма."""
    pass

class DataProcessor:
    def __init__(self, file_path: str, expected_columns: list, expected_types: dict) -> None:
        self.file_path = file_path
        self.expected_columns = expected_columns
        self.expected_types = expected_types
        self.df = None

    def process_dataset(self) -> None:
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"[Errno 2] No such file or directory: '{self.file_path}'")

            try:
                self.df = pd.read_csv(self.file_path)
            except pd.errors.EmptyDataError:
                raise ValueError("Датафрейм пуст")
            
            if self.df.empty:
                raise ValueError("Датафрейм пуст")

            errors = []
            actual_columns = list(self.df.columns)
            
            if actual_columns != self.expected_columns:
                errors.append(" - Названия столбцов не совпадают.")
                errors.append(f"Ожидаемые: {self.expected_columns}")
                errors.append(f"Фактические: {actual_columns}")
            
            for col in self.expected_columns:
                if col in actual_columns:
                    actual_type = str(self.df[col].dtype)
                    expected_type = self.expected_types.get(col)
                    
                    if expected_type and actual_type != expected_type:
                        errors.append(f" - В столбце '{col}' тип данных не соответствует ожидаемому.")
                        errors.append(f"Ожидается: {expected_type}, Фактически: {actual_type}")

            if errors:
                error_msg = "Структура датафрейма не соответствует ожидаемой:\n" + "\n".join(errors)
                raise StructureMismatchError(error_msg)

            print("Чтение датафрейма завершено успешно.")

        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")
        except ValueError as e:
            print(f"Возникла следующая ошибка: {e}")
        except StructureMismatchError as e:
            print(e)
        except Exception as e:
            print(f"Возникла неизвестная ошибка: {e}")