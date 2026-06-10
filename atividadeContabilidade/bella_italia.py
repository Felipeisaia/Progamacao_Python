"""
Bella Itália - Análise de Custos e Ponto de Equilíbrio
Sorveteria Artesanal | Potes de 1 Litro para Supermercados
"""

# ─────────────────────────────────────────────
# DADOS DA PRODUÇÃO
# ─────────────────────────────────────────────
QUANTIDADE_PRODUZIDA = 4_000   # potes/mês
PRECO_VENDA          = 25.00   # R$ por pote

# ─────────────────────────────────────────────
# TABELA DE GASTOS
# ─────────────────────────────────────────────
#  Cada item: (descrição, valor, classificação)
#  Classificações: "CV" | "CF" | "DV" | "DF"
#    CV = Custo Variável   CF = Custo Fixo
#    DV = Despesa Variável DF = Despesa Fixa

gastos = [
    ("Leite, creme de leite e insumos base",       6.00,       "CV"),
    ("Embalagens personalizadas (pote e tampa)",    1.50,       "CV"),
    ("Aluguel do galpão da fábrica",                8_000.00,  "CF"),
    ("Energia elétrica da fábrica (maquinário)",   0.50,       "CV"),
    ("Salários da equipe de produção (fixos)",      12_000.00, "CF"),
    ("Depreciação das máquinas de gelato",          2_000.00,  "CF"),
    ("Pró-labore do Sr. Lorenzo",                   6_000.00,  "DF"),
    ("Comissão dos vendedores (por pote vendido)",  1.00,       "DV"),
    ("Marketing e anúncios locais",                 3_000.00,  "DF"),
]

LABELS = {
    "CV": "Custo Variável",
    "CF": "Custo Fixo",
    "DV": "Despesa Variável",
    "DF": "Despesa Fixa",
}

# ─────────────────────────────────────────────
# CÁLCULOS PRINCIPAIS
# ─────────────────────────────────────────────

def valor_total_mensal(tipo: str, valor: float) -> float:
    """Converte valor unitário em total mensal quando necessário."""
    if tipo in ("CV", "DV"):          # valor já é unitário → multiplica
        return valor * QUANTIDADE_PRODUZIDA
    return valor                       # valor já é mensal


# Acumuladores
custo_variavel_unitario  = 0.0   # CVU  (R$/pote)
custo_fixo_total         = 0.0   # CF   (R$/mês)
despesa_variavel_unit    = 0.0   # DVU  (R$/pote)
despesa_fixa_total       = 0.0   # DF   (R$/mês)

for _, valor, tipo in gastos:
    if tipo == "CV":
        custo_variavel_unitario += valor
    elif tipo == "CF":
        custo_fixo_total += valor
    elif tipo == "DV":
        despesa_variavel_unit += valor
    elif tipo == "DF":
        despesa_fixa_total += valor

# Custo Total por Pote  (custos de produção apenas)
custo_total_por_pote = custo_variavel_unitario + (custo_fixo_total / QUANTIDADE_PRODUZIDA)

# Margem de Contribuição Unitária
# MC = PV − CVU − DVU  (retira tudo que é variável)
margem_contribuicao_unit = PRECO_VENDA - custo_variavel_unitario - despesa_variavel_unit

# Ponto de Equilíbrio Contábil  (cobre CF + DF)
gastos_fixos_totais = custo_fixo_total + despesa_fixa_total
pec_unidades = gastos_fixos_totais / margem_contribuicao_unit

# ─────────────────────────────────────────────
# RELATÓRIO
# ─────────────────────────────────────────────

SEP = "=" * 62

def fmt(v: float) -> str:
    return f"R$ {v:>10,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(SEP)
print("       BELLA ITÁLIA — ANÁLISE DE CUSTOS MENSAIS")
print(f"       Produção: {QUANTIDADE_PRODUZIDA:,} potes | Preço: {fmt(PRECO_VENDA)}/pote")
print(SEP)

# ── 1. Classificação dos gastos ──────────────
print("\n[1] CLASSIFICAÇÃO DOS GASTOS\n")
print(f"  {'Descrição':<45} {'Classificação':<18} {'Valor Unit./Total':>16}")
print("  " + "-" * 82)
for desc, valor, tipo in gastos:
    label = LABELS[tipo]
    if tipo in ("CV", "DV"):
        v_str = f"{fmt(valor)}/pote"
    else:
        v_str = fmt(valor)
    print(f"  {desc:<45} {label:<18} {v_str:>22}")

# ── 2. Custo do Produto ───────────────────────
print(f"\n{SEP}")
print("[2] CUSTO DO PRODUTO")
print(SEP)

print(f"\n  Custo Variável Unitário (CVU)")
print(f"    Insumos base                {fmt(6.00)}/pote")
print(f"    Embalagens                  {fmt(1.50)}/pote")
print(f"    Energia elétrica            {fmt(0.50)}/pote")
print(f"    ─────────────────────────────────────")
print(f"    TOTAL CVU                   {fmt(custo_variavel_unitario)}/pote")

print(f"\n  Custo Fixo Total (CF/mês)")
print(f"    Aluguel do galpão          {fmt(8_000)}")
print(f"    Salários de produção       {fmt(12_000)}")
print(f"    Depreciação das máquinas   {fmt(2_000)}")
print(f"    ─────────────────────────────────────")
print(f"    TOTAL CF                   {fmt(custo_fixo_total)}")

cf_unit = custo_fixo_total / QUANTIDADE_PRODUZIDA
print(f"\n  Custo Fixo Unitário          {fmt(cf_unit)}/pote")
print(f"  (R$ {custo_fixo_total:,.0f} ÷ {QUANTIDADE_PRODUZIDA:,} potes)")

print(f"\n  Custo Total por Pote         {fmt(custo_total_por_pote)}/pote")
print(f"  (CVU {fmt(custo_variavel_unitario)} + CF unit. {fmt(cf_unit)})")

# ── 3. Margem de Contribuição ─────────────────
print(f"\n{SEP}")
print("[3] MARGEM DE CONTRIBUIÇÃO UNITÁRIA")
print(SEP)
print(f"\n  Preço de Venda               {fmt(PRECO_VENDA)}/pote")
print(f"  (−) CVU                      {fmt(custo_variavel_unitario)}/pote")
print(f"  (−) Despesa Variável Unit.   {fmt(despesa_variavel_unit)}/pote  ← comissão vendedor")
print(f"  ──────────────────────────────────────────")
print(f"  Margem de Contribuição (MC)  {fmt(margem_contribuicao_unit)}/pote")

# ── 4. Ponto de Equilíbrio ────────────────────
print(f"\n{SEP}")
print("[4] PONTO DE EQUILÍBRIO CONTÁBIL (PEC)")
print(SEP)
print(f"\n  Gastos Fixos Totais")
print(f"    Custos Fixos (CF)          {fmt(custo_fixo_total)}")
print(f"    Despesas Fixas (DF)        {fmt(despesa_fixa_total)}")
print(f"    ─────────────────────────────────────")
print(f"    Total Fixo                 {fmt(gastos_fixos_totais)}")
print(f"\n  PEC = Gastos Fixos ÷ MC")
print(f"      = {fmt(gastos_fixos_totais)} ÷ {fmt(margem_contribuicao_unit)}")
print(f"      = {pec_unidades:,.2f} potes")
print(f"      ≈ {int(-(-pec_unidades // 1)):,} potes/mês  (arredondando para cima)")

# ── 5. Diagnóstico ────────────────────────────
pec_int = int(-(-pec_unidades // 1))
receita_atual = QUANTIDADE_PRODUZIDA * PRECO_VENDA
lucro_atual   = (margem_contribuicao_unit * QUANTIDADE_PRODUZIDA) - gastos_fixos_totais

print(f"\n{SEP}")
print("[5] DIAGNÓSTICO ESTRATÉGICO")
print(SEP)
print(f"\n  Preço de venda atual         {fmt(PRECO_VENDA)}/pote")
print(f"  Custo total por pote         {fmt(custo_total_por_pote)}/pote")
print(f"  Margem líquida por pote      {fmt(PRECO_VENDA - custo_total_por_pote)}/pote")
print(f"\n  Produção atual               {QUANTIDADE_PRODUZIDA:,} potes")
print(f"  Ponto de equilíbrio          {pec_int:,} potes")

if QUANTIDADE_PRODUZIDA >= pec_int:
    folga = QUANTIDADE_PRODUZIDA - pec_int
    print(f"  Margem de segurança          {folga:,} potes acima do PEC  ✓")
else:
    deficit = pec_int - QUANTIDADE_PRODUZIDA
    print(f"  ATENÇÃO: faltam {deficit:,} potes para cobrir todos os custos!")

print(f"\n  Lucro/Prejuízo atual         {fmt(lucro_atual)}/mês")


print(f"\n{SEP}\n")
