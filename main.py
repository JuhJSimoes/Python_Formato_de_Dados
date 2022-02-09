#from cpf_cnpj import Documento
from telefoneBr import TelefonesBr



#Bloco de teste CNPJ e CPF

#exemplo_cnpj = "78190140000167"
#documento = Documento.cria_documento(exemplo_cnpj)
#exemplo_cpf = "05801021736"
#documento = Documento.cria_documento(exemplo_cpf)
#print(documento)

#Bloco de teste telefones / necessario ajusto quando for celular
telefone = '552133091008'

telefone_obj = TelefonesBr(telefone)
print(telefone_obj)


