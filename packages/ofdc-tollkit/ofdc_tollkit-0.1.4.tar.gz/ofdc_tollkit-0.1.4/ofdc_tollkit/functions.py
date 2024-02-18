import os, pandas as pd, psycopg2 as pg, pickle, time
from datetime import datetime, timedelta

class path:
    """Classe de Geração de caminhos dinâmicos"""
    def __init__(self, file):
        self.file = file

    # Caminho Dinâmico
    def caminho(self, niveis=1, pasta = ['']):
        """Função de transito de caminhos"""
        if niveis <= 0:
            niveis = 1
        if not isinstance(pasta, list):
            pasta = [pasta]
        caminho = self.file
        for _ in range(niveis):
            caminho = os.path.dirname(caminho)
        caminho = os.path.join(caminho, *pasta)
        return caminho
    
    # Arquivo Dinâmico
    def conexao(self, caminho):
        credenciais = pd.read_excel(caminho)
        host = credenciais.iloc[0, 1]
        database = credenciais.iloc[1, 1]
        user = credenciais.iloc[2, 1]
        password = credenciais.iloc[3, 1]
        return pg.connect(host=host, database=database, user=user, password=password)

    # Schema
    def schema(self, caminho):
        credenciais = pd.read_excel(caminho)
        schema = credenciais.iloc[4, 1]
        return schema


def tabela(modo, conn, schema, nome,  pk, dias, tdata, output):
    """Função de cópia do banco para um Datalake"""
    InicioExecucao =  time.time()
    if os.path.exists(os.path.join(output, nome + '.plk')):
        with open(os.path.join(output, nome + '.plk'), 'rb') as file:
            tabela = pickle.load(file)
            dataframe = tabela[0]
    else:
        dataframe = pd.DataFrame()
        modo = 'reset'

    data = datetime.strptime(tabela[1].iloc[0, 0], '%Y-%m-%d').date() - timedelta(days=dias) if modo != 'reset' else datetime(2000,1,1)
    filtro = '' if tdata == None else f"WHERE {tdata} >= '{data}'"
    query = f"SELECT * FROM {schema}.{nome} {filtro}"
    new = pd.read_sql_query(query, conn)
    asd = pd.concat([new, dataframe], ignore_index=False) if modo != 'reset' else new
    asd = asd.drop_duplicates(subset=pk)
    tabela = [asd, pd.DataFrame({'Descrição': ['Data última atualização:', 'Modo Execução:'], '': [str(datetime.now().date()), modo]}).set_index('Descrição')]
    pickle.dump(tabela, open(os.path.join(output, nome + '.plk'), 'wb'))

    FimExecucao = time.time() - InicioExecucao
    print(f'[{str(datetime.now())[0:19]}] {nome} -> OK | TED: {FimExecucao:.2f}s')

def ler_datalake(path, pk):
    """Leitura de arquivos .plk"""
    df = pd.read_pickle(path)[0]
    df = df.astype({pk:str})
    return df

def definir_pk(dataframe, pk):
    dataframe = dataframe.astype({pk:str})
    return dataframe