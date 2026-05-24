class formatBRL():
    @staticmethod
    def preco_formatado(preco : float) -> str:
        preco_em_str = f'{preco:.2f}'

        if (preco > 999.99):  # irá precisar do ponto separador dos milhares
            # transforma em str e separa os reais dos centavos
            [reais, centavos] = preco_em_str.split(".")

            # adiciona o ponto separador dos milhares
            reais = list(reais)
            for i in range(len(reais) - 3, 0, -3):
                reais.insert(i, ".")

            return f'R$ {"".join(reais)},{centavos}'
        else:
            return f'R$ {preco_em_str.replace(".", ",")}'