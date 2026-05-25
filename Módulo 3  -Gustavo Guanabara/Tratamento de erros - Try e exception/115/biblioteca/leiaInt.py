def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print("Erro!Digite um número inteiro válido")
        except KeyboardInterrupt:
            print("Usuário preferiu digitar esse número")
            return 0
        else:
            return numero
        
