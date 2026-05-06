import urllib.request

def verificar_site(url):
    try:
        # Tenta abrir o site informado
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        # Caso ocorra um erro de conexão (site offline ou sem internet)
        print('\033[31mO site não está acessível no momento. :(\033[m')
    else:
        # Se o site abrir com sucesso
        print('\033[32mConsegui acessar o site com sucesso! :)\033[m')
        # Opcional: imprimir o conteúdo html do site
        # print(site.read()) 

# Execução
verificar_site('http://www.pudim.com.br')