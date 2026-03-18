import pandas as pd
import matplotlib.pyplot as plt

# 1. Criando o DataFrame com os dados da pesquisa FGVcia 2025
dados = {
    'Setor': ['Bancos', 'Serviços', 'Indústria', 'Comércio', 'Média Geral'],
    'Investimento_TI_Pct': [16, 15, 6, 5, 10],  # Porcentagem do faturamento
    'CAPU_Mil_R$': [162, 70, 45, 40, 60]       # Custo Anual por Usuário
}

df = pd.DataFrame(dados)

# 2. Análise Rápida: Relação Investimento vs. Setor
print("--- Resumo dos Indicadores de TI 2025 ---")
print(df)

# 3. Visualização Gráfica
plt.figure(figsize=(10, 6))
plt.bar(df['Setor'], df['Investimento_TI_Pct'], color='skyblue')

# Customização do gráfico
plt.title('Investimento em TI por Setor (% do Faturamento) - FGVcia 2025')
plt.xlabel('Setores')
plt.ylabel('% do Faturamento')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando uma linha de referência para a média geral
plt.axhline(y=10, color='red', linestyle='-', label='Média Geral (10%)')
plt.legend()

plt.show()

# 4. Insights Automáticos
print("\n--- Insights da Análise ---")
maior_investimento = df.iloc[df['Investimento_TI_Pct'].idxmax()]
print(f"O setor de {maior_investimento['Setor']} lidera o investimento estratégico.")