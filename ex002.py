cores = {'limpa' : '\033[m', 'amarelo' : '\033[33m', 'roxo' : '\033[35m'}
nome=input("{}Qual seu nome?{} ".format(cores['amarelo'], cores['limpa']))
print("{}Prazer em conhecelo,{} Seja bem vindo!" .format(cores['roxo'],nome))
