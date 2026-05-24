from urllib import request

def verificar_site(url):
    try:
        site = request.urlopen(url)
        
    except request.HTTPError:
    
        print('\033[31mO site não está acessível no momento. :(\033[m')
    else:

        print('\033[32mConsegui acessar o site com sucesso! :)\033[m')
        
        return site

# Execução
verificar_site('https://www.youtube.com/')