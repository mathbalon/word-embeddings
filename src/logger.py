from datetime import datetime

header_text = """

Autor: Matheus Balonecker

Configurações da máquina:
-- MacBook Pro Ventura 13.1
-- Memória 16 GB
-- Armazendamento 500 GB SSD
-- Processador Apple M1 Pro 16 núcleos
-- GPU Integrada

"""

execution_time_section = "Tempos de execução das funções:\n"

def format_settings(settings:dict) -> str:
    settings_text = ""
    for key, value in settings.items():
        settings_text += "  {}, {}\n".format(key, value)
    return settings_text

def init_logger_file(settings:dict) -> str:
    now = datetime.now()

    logger_file_name = now.strftime("%d-%m-%Y--%H:%M:%S__") + str(now.timestamp())

    logger_file = open("logs/"+logger_file_name, "a")

    experiment_date = "Data do experimento: {}".format(now.strftime("%d-%m-%Y %H:%M:%S"))

    experiment_settings = """Configurações do experimento:\n\n{}\n\n""".format(format_settings(settings))

    logger_file.write(experiment_date + 
    header_text + 
    experiment_settings +
    execution_time_section
    )
    
    logger_file.close()

    return logger_file_name

def logger(logger_file_name: str, function_name:str, time:float):
    logger_file = open("logs/"+logger_file_name, "a")
    logger_file.write("• {}: {} segundos\n".format(function_name, time))
    logger_file.close()