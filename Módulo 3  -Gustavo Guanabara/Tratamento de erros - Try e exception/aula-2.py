# 1º opção
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    resultado = a / b
except Exception as erro:
    print(f"Erro! {erro}")
else:
    
    print(f"{resultado:.2f}")
finally:
    print("Fim!")
    
    
input("\n")

# 2° opção

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    resultado = a / b
except (ValueError, SyntaxError):
    print(f"Erro no valor: {ValueError} ou sintase: {SyntaxError}")
    
except ZeroDivisionError:
    print("Não é possível dividir por zero")

except KeyboardInterrupt:
    print("O usuário não preferiu informar os dados")
    
except Exception as erro:
    print(f"O erro não foi encontrado {erro.__cause__}")
else:
    print(f"{resultado:.2f}")
finally:
    print("Fim!")



