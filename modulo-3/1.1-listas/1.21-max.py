numeros = [1, 2, 3, 4, 5]
maior = max(numeros)
print(maior)

linguagens = ["python", "js", "c", "java", "csharp"]
maior = max(linguagens, key=lambda x: len(x))
print(maior)
