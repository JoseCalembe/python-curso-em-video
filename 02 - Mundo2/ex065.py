sexo=str(input("Informe o sexo [M/F]:")).strip().upper()
while sexo not in "MmFf":
      sexo=str(input("Dados invalido, porfavor informe o seu sexo[M/F]:")).strip().upper()
print("Sexo {} registrado com sucesso".format(sexo))