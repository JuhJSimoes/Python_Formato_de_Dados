from validate_docbr import CPF, CNPJ

class Documento:
    
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digito inválida!")
        

#VALIDANDO CPF
class DocCpf:
    
    #INSTANCIANDO
    def __init__(self, documento):
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")
    
    def __str__(self):
        return self.format_cpf()
                  
  
    def cpf_valido(self,documento):
            validador = CPF()
            return validador.validate(documento)
        
                       
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)    
  
           
    
#VALIDANDO CNPJ

class DocCnpj:
    
    def __init__(self, documento):
        if self.cnpj_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")
            
    
    def __str__(self):
        return self.format_cnpj()
    
    
    def cnpj_valido(self,documento):
        validador = CNPJ()
        return validador.validate(documento)
        
    
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)    
