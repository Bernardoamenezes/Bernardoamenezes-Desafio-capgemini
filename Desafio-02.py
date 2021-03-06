#Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios:
#Possui no mínimo 6 caracteres.
#Contém no mínimo 1 digito.
#Contém no mínimo 1 letra em minúsculo.
#Contém no mínimo 1 letra em maiúsculo.
#Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-

#Débora digitou uma string aleatória no campo de senha, 
# porém ela não tem certeza se é uma senha forte. 
# Para ajudar Débora, construa um algoritmo que informe
# qual é o número mínimo de caracteres que devem ser adicionados
# para uma string qualquer ser considerada segura.


while True:
    senha = input("Crie a sua senha: ")
    if len(senha) < 6:
        x = 6 - len(senha)
        print(f"Você digitou {len(senha)}\nÉ necessaário no mínimo 6 caracteres. \n")
    else:
        break

print("Senha validada!!")