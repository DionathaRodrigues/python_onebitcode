# String = str
# String é uma sequência de caracteres
# Exemplo de uso de string

email = "joao.silva@example.com"
usuario = email.split("@")[0]
dominio = email.split("@")[1]

print("E-mail:", email)
print(f"Usuário: {usuario}, Domínio: {dominio}")

print("\n" + "=" * 20 + "\n")


# Lista = list
# Lista é uma coleção de itens que podem ser alterados
# Exemplo de uso de lista

tarefas = ["Responder e-mails", "Reunião com equipe", "Revisar relatório"]

tarefas.append("Planejar campanha")
tarefas.remove("Reunião com equipe")

for t in tarefas:
    print("Próxima tarefa:", t)

print("\n" + "=" * 20 + "\n")

# Tupla = tuple
# Tupla é uma coleção de itens que não podem ser alterados
# Exemplo de uso de tupla

coordenadas = (40.7128, -74.0060)  # Latitude e Longitude de Nova York

print("Latitude:", coordenadas[0])
print("Longitude:", coordenadas[1])

print("\n" + "=" * 20 + "\n")

# Dicionário = dict
# Dicionário é uma coleção de pares chave-valor
# Exemplo de uso de dicionário

cliente = {
    "nome": "Ana",
    "idade": 32,
    "email": "ana@example.com"
}

print(cliente["nome"], "tem", cliente["idade"], "anos.")

print("\n" + "=" * 20 + "\n")

# Conjunto = set
# Conjunto é uma coleção de itens únicos
# Exemplo de uso de conjunto

convidados = ["Ana", "João", "Ana", "Carlos", "João"]
convidados_unicos = set(convidados)

print(convidados_unicos)

