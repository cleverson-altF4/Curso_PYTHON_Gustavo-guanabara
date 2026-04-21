def notas(*n, situacao=True):
    """
        A função para analisar a sintuação das notas, ele coloca como parâmetro:
        param: *n
        param: sintuacao=False ou True
        dicionário: ele lê o total de notas, maior, menor, media e a sintuacao do aluno se encontra
    """
    
    dicionario = {
        "total": len(n),
        "maior": max(n),
        "menor": min(n),
        "media": sum(n) / len(n)
    }
    
    if situacao:
        if dicionario['media'] >= 7:
            dicionario['situacao'] ='Boa'
        elif dicionario['media'] >= 5:
            dicionario['situacao']= 'Razoável'
        elif dicionario['media'] < 5:
            dicionario['situacao']= 'Ruim'
    return dicionario
            
            
resposta = notas(5.5,6.4,11)
print(resposta)

help(notas)
    