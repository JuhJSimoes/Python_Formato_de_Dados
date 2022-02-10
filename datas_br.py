from datetime import datetime, timedelta
from xmlrpc.client import DateTime

class DatasBr:
    
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.format_data()
        
    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março", 
            "Abril", "Maio", "Junho", "Julho",
            "Agosto", "Setembro", "Outubro", 
            "Novembro", "Dezembro"
        ]
        mes_cadastrado = self.momento_cadastro.month -1
        return meses_do_ano[mes_cadastrado]
    
    def dia_semana(self):
        dias_semana = [
            "Segunda","Terça", "Quarta",
            "Quinta", "Sexta", "Sabbado", "Domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_de_cadastro = (datetime.today() + timedelta(days=15)) - self.momento_cadastro
        return tempo_de_cadastro