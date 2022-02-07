from validate_docbr import CPF, CNPJ


class CpfCnpj:
    
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == 'cpf':
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == tipo_documento:
            if self.tipo_documento == 'cnpj':
                if self.cnpj_valido(documento):
                    self.cnpj = documento
                else:
                    raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento invalido")

        
  
    def cpf_valido(self,cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digito inválida!")
               
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)    
           
    def __str__(self):
        return self.format_cpf()

    def cnpj_valido(self,cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de digito inválida!")
    
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)    
           
    def __str__(self):
        return self.format_cnpj()
            