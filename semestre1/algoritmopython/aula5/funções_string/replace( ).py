s = "A função replace aa substitui parte de um texto por outro texto"
s2= s.replace("aa", "123")
print("Frase original = " +s)
print("Frase alterada = " + s2)

# 'A função replace 123 substitui parte de um texto por outro texto'
print(id(s))
print(id(s2))