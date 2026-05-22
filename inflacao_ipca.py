import requests

class ConsultaIPCA:
    def __init__(self, ano):
        self.ano = ano

    def buscar(self):
        url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/{self.ano}&dataFinal=31/12/{self.ano}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            print(f"\nIPCA mensal - {self.ano}")
            print("-" * 25)
            for item in dados:
                print(f"{item['data']}  ->  {item['valor']}%")
        else:
            print("Erro ao buscar dados.")

if __name__ == "__main__":
    ipca = ConsultaIPCA(ano=2024)
    ipca.buscar()
