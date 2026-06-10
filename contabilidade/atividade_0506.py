gastos = [
    {"desc": "Salário da equipe de programadores",        "valor": 6000.00, "tipo": "Custo",   "comportamento": "Fixo"},
    {"desc": "Comissão do vendedor (5% receita)",          "valor":  750.00, "tipo": "Despesa", "comportamento": "Variável"},
    {"desc": "Estagiário para o administrativo",           "valor": 1200.00, "tipo": "Despesa", "comportamento": "Fixo"},
    {"desc": "Licenças de software (por usuário ativo)",   "valor":  800.00, "tipo": "Custo",   "comportamento": "Variável"},
    {"desc": "ISS (5% sobre o faturamento)",               "valor":  750.00, "tipo": "Despesa", "comportamento": "Variável"},
    {"desc": "Pró-labore do Lucas",                        "valor": 3000.00, "tipo": "Despesa", "comportamento": "Fixo"},
    {"desc": "Conta de internet dedicada",                 "valor":  250.00, "tipo": "Custo",   "comportamento": "Fixo"},
    {"desc": "Material de escritório e limpeza",           "valor":  150.00, "tipo": "Despesa", "comportamento": "Fixo"},
]

faturamento = 15_000.00

# ── Questão 1: Custo vs Despesa ──────────────────────────────────────────────
print("=" * 60)
print("QUESTÃO 1 — CUSTO vs. DESPESA")
print("=" * 60)

for categoria in ["Custo", "Despesa"]:
    itens = [g for g in gastos if g["tipo"] == categoria]
    total = sum(g["valor"] for g in itens)
    print(f"\n{'CUSTOS' if categoria == 'Custo' else 'DESPESAS'}:")
    for g in itens:
        print(f"  {g['desc']:<45} R$ {g['valor']:>8,.2f}")
    print(f"  {'Subtotal':<45} R$ {total:>8,.2f}")

# ── Questão 2: Fixo vs Variável ───────────────────────────────────────────────
print("\n" + "=" * 60)
print("QUESTÃO 2 — FIXO vs. VARIÁVEL")
print("=" * 60)

for comportamento in ["Variável", "Fixo"]:
    itens = [g for g in gastos if g["comportamento"] == comportamento]
    total = sum(g["valor"] for g in itens)
    print(f"\n{comportamento.upper()}:")
    for g in itens:
        print(f"  [{g['tipo']:<7}] {g['desc']:<40} R$ {g['valor']:>8,.2f}")
    print(f"  {'Subtotal':<49} R$ {total:>8,.2f}")

# ── Questão 3: Margem de Contribuição e Ponto de Equilíbrio ──────────────────
total_variavel = sum(g["valor"] for g in gastos if g["comportamento"] == "Variável")
total_fixo     = sum(g["valor"] for g in gastos if g["comportamento"] == "Fixo")
total_gastos   = total_variavel + total_fixo

mc_reais   = faturamento - total_variavel
mc_pct     = mc_reais / faturamento
pe         = total_fixo / mc_pct
lucro      = mc_reais - total_fixo
lucro_pct  = lucro / faturamento * 100
margem_seg = faturamento - pe

print("\n" + "=" * 60)
print("QUESTÃO 3 — MARGEM DE CONTRIBUIÇÃO E PONTO DE EQUILÍBRIO")
print("=" * 60)

print(f"""
  Faturamento                        R$ {faturamento:>9,.2f}
  (-) Gastos Variáveis               R$ {total_variavel:>9,.2f}
  (=) Margem de Contribuição         R$ {mc_reais:>9,.2f}  ({mc_pct*100:.2f}%)
  (-) Gastos Fixos                   R$ {total_fixo:>9,.2f}
  (=) Lucro Operacional              R$ {lucro:>9,.2f}  ({lucro_pct:.2f}%)

  Ponto de Equilíbrio                R$ {pe:>9,.2f}
  Margem de Segurança                R$ {margem_seg:>9,.2f}
""")

# ── Análise Crítica ───────────────────────────────────────────────────────────
print("=" * 60)
print("ANÁLISE CRÍTICA")
print("=" * 60)
if lucro > 0:
    print(f"\n  O contrato é LUCRATIVO: gera R$ {lucro:,.2f}/mês ({lucro_pct:.1f}% de margem).")
    print(f"  O faturamento supera o PE em R$ {margem_seg:,.2f} (margem de segurança).")
    if lucro_pct < 20:
        print("  Atenção: margem estreita. Reajuste do contrato é recomendado.")
else:
    print(f"  O contrato gera PREJUÍZO de R$ {abs(lucro):,.2f}/mês.")
print()
