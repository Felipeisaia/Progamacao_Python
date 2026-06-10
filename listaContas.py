Receita_merc =	320000
Receita_serv =	80000
faturamento = Receita_merc + Receita_serv
Devolucao_Abatimentos	= 5500
Simples_Nacional =	34000
cmv	= 145000
csp = 15000
pro_labore = 18000
salario = 35000
fgts = 2800
aluguel = 12000
material = 1500
internet = 850
vendas = 4200
taxas = 6500
propaganda = 9000
honorario = 2200
reparos = 1800
rendimentos = 1500
juros_multa  = 3500
tarifas = 2500

receita_liquida = (
    Receita_merc
    +Receita_serv
    -Devolucao_Abatimentos
    -Simples_Nacional
)

conta_custo = (
   receita_liquida
    -cmv
    -csp 
    -pro_labore 
    -salario 
    -fgts 
    -aluguel 
    -material 
    -internet 
    -vendas 
    -taxas 
    -propaganda
    -honorario 
    -reparos 
)

resultado_operacional = (
    conta_custo
    + rendimentos
    -juros_multa
    -tarifas

)

print("-" * 40)
print(f"Receita Líquida: R$ {receita_liquida:,.2f}")
print("-" * 40)
print(f"Margem de contribuicao: R$ {conta_custo:,.2f}")
print("-" * 40)
print(f"Resultado operacional: R$ {resultado_operacional:,.2f}")
print("-" * 40)
print(f"{(resultado_operacional / faturamento ) * 100:,.1f}%")
print("-" * 40)