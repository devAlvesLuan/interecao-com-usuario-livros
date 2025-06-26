def leituras_cinco_anos(livros_digitais_ano, livros_fisicos_ano):
    return (livros_digitais_ano + livros_fisicos_ano) * 5

def horas_por_ano(horas_semanais):
    return horas_semanais * 52

def meta_leitura_ideal(idade_usuario):
    idade_inicial = 15
    if idade_usuario < idade_inicial:
        return "Você ainda está começando sua jornada como leitor. Aproveite!"
    anos_de_leitura = idade_usuario - idade_inicial
    meta = anos_de_leitura * 10  # meta de 10 livros por ano
    return f"Se tivesse lido 10 livros por ano desde os {idade_inicial}, você teria lido cerca de {meta} livros até agora."

def classificacao_leitor(total_livros):
    if total_livros <= 5:
        return "Leitor iniciante"
    elif total_livros <= 20:
        return "Leitor casual"
    elif total_livros <= 40:
        return "Leitor frequente"
    else:
        return "Leitor voraz"

print("============= Cadastro =============")

nome_usuario = input("| Qual seu nome: ")
idade_usuario = int(input("| Qual sua idade: "))
cidade_estado = input("| Em qual cidade e estado você vive: ")
livros_digitais_ano = int(input("| Quantos livros digitais você leu no último ano? "))
livros_fisicos_ano = int(input("| Quantos livros físicos você leu no último ano? "))

# Coletando preferência de leitura corretamente
while True:
    print("| Qual sua preferência de leitura:\n 1. Digital\n 2. Físico")
    preferencia = input("> ").strip()
    if preferencia == "1":
        preferencia_leitura = "Digital"
        break
    elif preferencia == "2":
        preferencia_leitura = "Físico"
        break
    else:
        print("Digite um número válido (1 ou 2).")

# Entradas de horas
horas_estudos = float(input("| Quantas horas dedica aos livros para estudo por semana? "))
horas_entretenimento = float(input("| Quantas horas dedica aos livros para entretenimento por semana? "))

# Mensagem de boas-vindas
print(f"\n============= Seja bem-vindo, {nome_usuario}! =============")
print(f"É ótimo ver alguém de {idade_usuario} anos lendo em {cidade_estado}. Ler é uma forma poderosa de aprendizado e entretenimento.")

# Estimativa de leitura em 5 anos
estimativa_total = leituras_cinco_anos(livros_digitais_ano, livros_fisicos_ano)
print(f"\n📚 Estimativa: Nos próximos 5 anos, você pode ler cerca de {estimativa_total} livros.")

# Feedback com base na estimativa
if estimativa_total <= 10:
    print("⚠️ Você está começando bem, mas pode aumentar suas leituras nos próximos anos!")
elif 25 <= estimativa_total <= 30:
    print("✅ Você tem uma ótima frequência de leitura, continue assim!")
else:
    primeiro_nome = nome_usuario.split()[0]
    print(f"🎉 Você ama livros de verdade, {primeiro_nome}! Ler faz parte da sua essência, parabéns!")

# Cálculo de horas por ano
horas_estudo_ano = horas_por_ano(horas_estudos)
horas_entretenimento_ano = horas_por_ano(horas_entretenimento)

print(f"\n🧠 Você dedica cerca de {horas_estudo_ano} horas por ano aos estudos.")
print(f"🎯 E cerca de {horas_entretenimento_ano} horas por ano à leitura por lazer.")

# Funções extras:
if idade_usuario > 15:
    meta = meta_leitura_ideal(idade_usuario)
    print(meta)
else:
    print("Você ainda está no começo da sua jornada como leitor. Continue lendo e aproveite!")

classificacao = classificacao_leitor(livros_digitais_ano + livros_fisicos_ano)

print(f"🏷️ Classificação do seu perfil de leitor: {classificacao}")
