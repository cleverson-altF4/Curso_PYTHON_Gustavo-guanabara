def notas(*n, sit=False):
    dicionario = {
        "total": len(n),
        "maior": max(n),
        "menor": min(n),
        "media": sum(n) / len(n)
    }
    
    if sit:
        if dicionario['media'] >= 7:
            sit=True