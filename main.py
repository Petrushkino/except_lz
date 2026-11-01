from data_processor import DataProcessor

def main() -> None:
    file_name = "var3.csv"
    
    expected_cols = [
    'Участники гражданского оборота', 
    'Тип операции', 
    'Сумма операции', 
    'Вид расчета',
    'Место оплаты',
    'Терминал оплаты',
    'Дата оплаты',
    'Сумма cash-back',
    'Время оплаты',
    'Результат операции',
    'Cash-back',
    'Сумма cash-back'
    ]
    
    expected_types = {
    'Участники гражданского оборота': 'object',  
    'Тип операции': 'object',                    
    'Сумма операции': 'float64',                 
    'Вид расчета': 'object',                     
    'Место оплаты': 'object',                    
    'Терминал оплаты': 'object',                 
    'Дата оплаты': 'object',                     
    'Время оплаты': 'object',                    
    'Результат операции': 'object',              
    'Cash-back': 'object',                       
    'Сумма cash-back': 'float64'                 
    }
    



    processor = DataProcessor(file_name, expected_cols, expected_types)
    processor.process_dataset()

if __name__ == "__main__":
    main()