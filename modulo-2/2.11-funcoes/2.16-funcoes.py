def exemplo(*args, **kwargs):
    print("Args (posicionais):", args)  # Tupla
    print("Kwargs (nomeados):", kwargs)  # Dicionário

exemplo(1, 2, 3, nome="João", idade=30)