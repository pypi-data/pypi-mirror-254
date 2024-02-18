import os, pandas as pd, psycopg2 as pg

class path:
    def __init__(self, file):
        self.file = file

    # Caminho Dinâmico
    def caminho(self, niveis=1, pasta = ['']):
        if niveis <= 0:
            niveis = 1
        if not isinstance(pasta, list):
            pasta = [pasta]
        caminho = self.file
        for _ in range(niveis):
            caminho = os.path.dirname(caminho)
        caminho = os.path.join(caminho, *pasta)
        return caminho
