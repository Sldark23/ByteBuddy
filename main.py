#as funções
class AmiguinhoVirtual:
    
    def __init__(self):
        self.nome = "ByteBuddy"
        self.idade = 1
    
    def cumprimentar(self):
        print(f"Olá! Eu sou {self.nome} e tenho {self.idade} anos.")
    
    def envelhecer(self, anos=1):
        self.idade += anos
        print(f"{self.nome} agora tem {self.idade} anos.")
        


    def piu_piu(params):
      print('haha vc não me asertou')
        
      
 
        
      # Criando uma instância do AmiguinhoVirtual
amiguinho = AmiguinhoVirtual()

# Loop para executar as funções enquanto o usuário quiser
while True:
    comando = input("({•_•}) :")

    if comando == "cumprimentar":
        amiguinho.cumprimentar()

    elif comando == "envelhecer":
        anos = input("Quantos anos você quer que eu envelheça?")
        amiguinho.envelhecer(int(anos))

    elif comando == "sair":
        print("Tchau!")
        break
    elif comando == "piu":
      print('haha vc não me asertou')
    elif comando == "go home":
      print('carregando')
      break
    elif comando == "help":
      print('meu site para ajuda vc a usar os meu comandos : https://ByteBuddyweb.hostsitemaker.repl.co')
    else:
        print("Desculpe, eu não entendi o que você quer que eu faça.")
