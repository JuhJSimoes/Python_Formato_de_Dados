from cpf_cnpj import CpfCnpj

#cpf_um = Cpf("05801021736")
#print(cpf_um)

exemplo_cnpj = "78190140000167"
documento = CpfCnpj(exemplo_cnpj, 'cnpj')

print(documento)

