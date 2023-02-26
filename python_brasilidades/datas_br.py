from datetime import datetime

class DatasBr:
    def __init__(self):
        self.time_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        mes_cadastro = self.time_cadastro.month
        return mes_cadastro

    def dia_semana(self):
        dia_semana = self.time_cadastro.weekday()
        return dia_semana

    def format_data(self):
        data_formatada = self.time_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_de_cadastro(self):
        tempo_cadastro = datetime.today() - self.time_cadastro #exemplo: 19:31 15 sec - 19:30 12 sec
        return tempo_cadastro