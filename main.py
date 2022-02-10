#from cpf_cnpj import Documento
#from telefoneBr import TelefonesBr
from datas_br import DatasBr

#Bloco de teste CNPJ e CPF
'''exemplo_cnpj = "78190140000167"
documento = Documento.cria_documento(exemplo_cnpj)
exemplo_cpf = "05801021736"
documento = Documento.cria_documento(exemplo_cpf)
print(documento)'''


#Bloco de teste telefones / necessario ajusto quando for celular
'''telefone = '552133091008'
telefone_obj = TelefonesBr(telefone)
print(telefone_obj)'''


#Bloco de teste datas

cadastro = DatasBr()
'''print(cadastro.mes_cadastro())
print(cadastro.dia_semana())'''

#Formatando datas
#print(cadastro)
print(cadastro.tempo_cadastro())
