# Funções para métricas
def calcular_métricas(VP, VN, FP, FN):
    # Cálculos com verificação para evitar divisão por zero
    sensibilidade = VP / (VP + FN) if (VP + FN) != 0 else 0
    especificidade = VN / (FP + VN) if (FP + VN) != 0 else 0
    acurácia = (VP + VN) / (VP + VN + FP + FN)
    precisão = VP / (VP + FP) if (VP + FP) != 0 else 0
    f_score = (2 * precisão * sensibilidade) / (precisão + sensibilidade) if (precisão + sensibilidade) != 0 else 0

    return {
        "Sensibilidade (Recall)": sensibilidade,
        "Especificidade": especificidade,
        "Acurácia": acurácia,
        "Precisão": precisão,
        "F-score": f_score
    }

# Exemplo: valores arbitrários da matriz de confusão
VP = 70  # Verdadeiros positivos
VN = 50  # Verdadeiros negativos
FP = 10  # Falsos positivos
FN = 20  # Falsos negativos

# Cálculo das métricas
resultados = calcular_métricas(VP, VN, FP, FN)

# Exibição
for metrica, valor in resultados.items():
    print(f"{metrica}: {valor:.2f}")
