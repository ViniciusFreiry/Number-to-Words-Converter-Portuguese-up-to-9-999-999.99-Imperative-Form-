# Dicionários para conversão
unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas_simples = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

# Função que retorna números por extenso de 0 a 999
def numero_para_extenso(n):
    if n == 100:
        return "cem"
    partes = []
    c = n // 100
    d = (n % 100) // 10
    u = n % 10
    if c:
        partes.append(centenas[c])
    if d == 1:
        partes.append(dezenas_simples[u])
    else:
        if d:
            partes.append(dezenas[d])
        if u:
            partes.append(unidades[u])
    return " e ".join(partes)

# Verifica entre milhôes e milhares
def monta_bloco(numero, escala_singular, escala_plural):
    if numero == 0:
        return ""
    elif numero == 1:
        return numero_para_extenso(numero) + " " + escala_singular
    else:
        return numero_para_extenso(numero) + " " + escala_plural

# Escreve o números por extenso utilizando as últimas duas funções
def escrever_numero_por_extenso(valor):
    inteiro = int(valor)
    decimal = int(round((valor - inteiro) * 100))

    milhao = inteiro // 1_000_000
    milhar = (inteiro % 1_000_000) // 1_000
    unidades_milhar = inteiro % 1_000

    partes = []

    if milhao:
        partes.append(monta_bloco(milhao, "milhão", "milhões"))
    if milhar:
        if milhar == 1:
            partes.append("mil")
        else:
            partes.append(numero_para_extenso(milhar) + " mil")
    if unidades_milhar or not partes:
        partes.append(numero_para_extenso(unidades_milhar))

    resultado = " e ".join([p for p in partes if p])

    if decimal > 0:
        if decimal < 10:
            resultado += ", vírgula, zero " + numero_para_extenso(decimal)
        else:
            resultado += ", vírgula, " + numero_para_extenso(decimal)

    return resultado

# Entrada e validação
while True:
    entrada = input("Digite um número entre 0 e 9999999,99: ").replace(",", ".")
    try:
        valor = float(entrada)
        if 0 <= valor <= 9999999.99:
            break
        else:
            print("Número fora do intervalo permitido.")
    except ValueError:
        print("Entrada inválida. Digite um número no formato correto.")

# Saída
extenso = escrever_numero_por_extenso(valor)
print("\nNúmero por extenso:")
print(extenso.capitalize())