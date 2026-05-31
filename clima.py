import requests

API_KEY = "87ba7ccf317728d761b4d0b0c8d0e39b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

CIDADES = ["São Paulo", "London", "Tokyo", "New York", "Paris"]


class CidadeClima:

    def __init__(self, nome: str, temperatura: float, umidade: int, condicao: str):
        self.__nome = nome
        self.__temperatura = temperatura
        self.__umidade = umidade
        self.__condicao = condicao

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @property
    def umidade(self) -> int:
        return self.__umidade

    @property
    def condicao(self) -> str:
        return self.__condicao

    def __str__(self) -> str:
        return (
            f"  Cidade     : {self.__nome}\n"
            f"  Temperatura: {self.__temperatura:.1f} °C\n"
            f"  Umidade    : {self.__umidade}%\n"
            f"  Condição   : {self.__condicao.capitalize()}"
        )


def buscar_clima(cidade: str) -> CidadeClima | None:
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }

    try:
        resposta = requests.get(BASE_URL, params=parametros, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        nome = dados["name"]
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        condicao = dados["weather"][0]["description"]

        return CidadeClima(nome, temperatura, umidade, condicao)

    except requests.exceptions.ConnectionError:
        print(f"  [ERRO] Sem conexão com a internet ao buscar '{cidade}'.")
    except requests.exceptions.Timeout:
        print(f"  [ERRO] Tempo de resposta esgotado para '{cidade}'.")
    except requests.exceptions.HTTPError as erro:
        if erro.response.status_code == 404:
            print(f"  [ERRO] Cidade '{cidade}' não encontrada na API.")
        elif erro.response.status_code == 401:
            print("  [ERRO] Chave de API inválida ou ainda não ativada.")
        else:
            print(f"  [ERRO] Erro HTTP ao buscar '{cidade}': {erro}")
    except (KeyError, ValueError):
        print(f"  [ERRO] Resposta inesperada da API para '{cidade}'.")

    return None


def coletar_relatorio(cidades: list[str]) -> list[CidadeClima]:
    relatorio_clima = []

    for cidade in cidades:
        print(f"Buscando dados de '{cidade}'...")
        objeto_cidade = buscar_clima(cidade)

        if objeto_cidade is not None:
            relatorio_clima.append(objeto_cidade)

    return relatorio_clima


def exibir_relatorio(relatorio_clima: list[CidadeClima]) -> None:
    separador = "=" * 45

    print("\n" + separador)
    print("   RELATÓRIO CLIMÁTICO — CIDADES DO MUNDO")
    print(separador)

    if not relatorio_clima:
        print("  Nenhum dado disponível para exibir.")
        print(separador)
        return

    for i, cidade in enumerate(relatorio_clima, start=1):
        print(f"\n  [{i}]")
        print(cidade)
        print()

    print(separador)
    print(f"  Total de cidades consultadas com sucesso: {len(relatorio_clima)}")
    print(separador + "\n")


if __name__ == "__main__":
    relatorio_clima = coletar_relatorio(CIDADES)
    exibir_relatorio(relatorio_clima)
