# minha_biblioteca.py

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import csv


class Predatamaker():
    """
    Uma biblioteca de funções para manipulação e análise de dados, focada em ajudar no aprendizado
    basico da progamação em IA e ajudando a lidar com dados.

    Methods:
        organizar_dados(dados, tipo_estrutura, chave_ordenacao=None, novo_arquivo=None): Organiza dados em diferentes estruturas.
        gerar_curvas_avaliacao(y_true, y_probabilidades, tipos_graficos=['roc', 'precision_recall', 'confusion_matrix'], titulo='Curvas de Avaliação', mostrar_diagonal=True): Gera e exibe curvas de avaliação.
        extrair_caracteristicas_relevantes(X, y, metodo='selecao', k=5, num_componentes=2): Extrai características relevantes de um conjunto de dados.
        gerar_tabelas(num_tabelas=1, num_colunas=2, num_amostras=100, modelo='linear', coeficientes=None): Gera tabelas simuladas para experimentação.
    """

    @staticmethod
    def organizar_dados(dados, tipo_estrutura, chave_ordenacao=None, novo_arquivo=None):
        """
        Organiza dados em diferentes estruturas.

        Parameters:
        -----------
        dados : list, dict, str
            Dados a serem organizados.
        tipo_estrutura : str
            Tipo de estrutura para organização ('lista', 'dicionario', 'csv').
        chave_ordenacao : str, optional
            Chave para ordenar os dados (opcional).
        novo_arquivo : str, optional
            Nome do novo arquivo CSV (opcional).

        Returns:
        --------
        list, dict, None
            Dados organizados na estrutura desejada ou None em caso de erro.
        """
        codificacoes = ['utf-8', 'latin-1', 'cp1252']

        def chave_ordenacao_func(x):
            valor = x[chave_ordenacao]
            if chave_ordenacao and isinstance(valor, str) and valor.isdigit():
                return int(valor)
            else:
                return valor

        if tipo_estrutura == 'lista':
            dados_organizados = sorted(dados, key=lambda x: chave_ordenacao_func(x))

        elif tipo_estrutura == 'dicionario':
            dados_organizados = {chave: dados[chave] for chave in sorted(dados)}

        elif tipo_estrutura == 'csv':
            for encoding in codificacoes:
                try:
                    with open(dados, 'r', encoding=encoding) as arquivo_csv:
                        leitor_csv = csv.DictReader(arquivo_csv)
                        dados_organizados = sorted(leitor_csv, key=lambda x: chave_ordenacao_func(x))
                    break  # Se a leitura foi bem-sucedida, saia do loop
                except FileNotFoundError:
                    print(f"Erro: Arquivo '{dados}' não encontrado.")
                    return None
                except UnicodeDecodeError:
                    print(f"Tentando codificação {encoding}...")
                    continue  # Tente a próxima codificação

            if 'dados_organizados' not in locals():  # Se nenhum encoding funcionou
                print("Erro: Não foi possível decodificar o arquivo. Verifique a codificação do arquivo.")
                return None

            # Escrever os dados ordenados em um novo arquivo, se fornecido
            if novo_arquivo:
                with open(novo_arquivo, 'w', newline='', encoding='utf-8') as arquivo_saida:
                    escritor_csv = csv.DictWriter(arquivo_saida, fieldnames=leitor_csv.fieldnames)
                    escritor_csv.writeheader()
                    escritor_csv.writerows(dados_organizados)

        else:
            print("Erro: Tipo de estrutura não suportado.")
            return None

        return dados_organizados



    @staticmethod
    def gerar_curvas_avaliacao(y_true, y_probabilidades, tipos_graficos=['roc', 'precision_recall', 'confusion_matrix'], titulo='Curvas de Avaliação', mostrar_diagonal=True):
        """
        Gera e exibe curvas de avaliação. Podendo exibir diferentes tipos de graficos a partir do que o usuario
        deseja, com tambem pequenas customizaçoes possiveis

        Parameters:
        -----------
        y_true : array-like
            Rótulos reais.
        y_probabilidades : array-like
            Probabilidades previstas.
        tipos_graficos : list, optional
            Tipos de gráficos a serem gerados ('roc', 'precision_recall', 'confusion_matrix').
        titulo : str, optional
            Título dos gráficos.
        mostrar_diagonal : bool, optional
            Mostrar diagonal na curva ROC (opcional).

        Returns:
        --------
        None
        """
        try:
            for tipo_grafico in tipos_graficos:
                if tipo_grafico == 'roc':
                    fpr, tpr, _ = roc_curve(y_true, y_probabilidades)
                    roc_auc = auc(fpr, tpr)

                    plt.figure(figsize=(8, 6))
                    plt.plot(fpr, tpr, linestyle='-', color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')

                    if mostrar_diagonal:
                        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')

                    plt.xlabel('False Positive Rate')
                    plt.ylabel('True Positive Rate')
                    plt.title(titulo + ' - ROC Curve')
                    plt.legend(loc='lower right')
                    plt.show()

                elif tipo_grafico == 'precision_recall':
                    precision, recall, _ = precision_recall_curve(y_true, y_probabilidades)
                    avg_precision = average_precision_score(y_true, y_probabilidades)

                    plt.figure(figsize=(8, 6))
                    plt.plot(recall, precision, linestyle='-', color='darkorange', lw=2, label=f'Precision-Recall curve (area = {avg_precision:.2f})')

                    plt.xlabel('Recall')
                    plt.ylabel('Precision')
                    plt.title(titulo + ' - Precision-Recall Curve')
                    plt.legend(loc='upper right')
                    plt.show()

                elif tipo_grafico == 'confusion_matrix':
                    cm = confusion_matrix(y_true, np.round(y_probabilidades))
                    plt.figure(figsize=(6, 6))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, annot_kws={'size': 14})
                    plt.xlabel('Predicted')
                    plt.ylabel('True')
                    plt.title(titulo + ' - Confusion Matrix')
                    plt.show()

        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def extrair_caracteristicas_relevantes(X, y, metodo='selecao', k=5, num_componentes=2):
        """
        Extrai características relevantes de um conjunto de dados dados por
        um usuario que serve para ajudar no treinamento e teste das ias.

        Parameters:
        -----------
        X : DataFrame
            Conjunto de dados.
        y : array-like
            Rótulos.
        metodo : str, optional
            Método de extração de características ('selecao', 'pca', 'correlacao').
        k : int, optional
            Número de características a serem selecionadas (para 'selecao').
        num_componentes : int, optional
            Número de componentes principais a serem mantidos (para 'pca').

        Returns:
        --------
        DataFrame
            Conjunto de dados com características relevantes.
        """
        try:
            if metodo == 'selecao':
                seletor = SelectKBest(score_func=f_regression, k=k)
                X_relevante = seletor.fit_transform(X, y)
                colunas_selecionadas = X.columns[seletor.get_support()]
                return pd.DataFrame(X_relevante, columns=colunas_selecionadas)

            elif metodo == 'pca':
                scaler = StandardScaler()
                X_padronizado = scaler.fit_transform(X)
                pca = PCA(n_components=num_componentes)
                X_pca = pca.fit_transform(X_padronizado)
                colunas_pca = [f'Componente_{i+1}' for i in range(num_componentes)]
                return pd.DataFrame(X_pca, columns=colunas_pca)

            elif metodo == 'correlacao':
                matriz_correlacao = X.corr()
                colunas_correlacionadas = set()
                for i in range(len(matriz_correlacao.columns)):
                    for j in range(i):
                        if abs(matriz_correlacao.iloc[i, j]) > 0.8:
                            coluna = matriz_correlacao.columns[i]
                            colunas_correlacionadas.add(coluna)
                return X.drop(columns=colunas_correlacionadas)

            else:
                print("Erro: Método de extração de características não suportado.")
                return None

        except Exception as e:
            print(f"Erro: {e}")
            return None

    @staticmethod
    def gerar_tabelas(num_tabelas=1, num_colunas=2, num_amostras=100, modelo='linear', coeficientes=None):
        """
        Gera tabelas simuladas para experimentação.

        Parameters:
        -----------
        num_tabelas : int, optional
            Número de tabelas a serem geradas.
        num_colunas : int, optional
            Número de colunas em cada tabela.
        num_amostras : int, optional
            Número de amostras em cada tabela.
        modelo : str, optional
            Modelo para gerar dados ('linear', 'quadratic', 'random').
        coeficientes : list, optional
            Coeficientes para o modelo linear ou quadrático.

        Returns:
        --------
        list of DataFrame
            Tabelas simuladas.
        """
        try:
            tabelas_simuladas = []
            for _ in range(num_tabelas):
                if modelo == 'linear':
                    if coeficientes:
                        X = np.random.rand(num_amostras, num_colunas)
                        y = np.dot(X, coeficientes) + np.random.normal(scale=0.1, size=num_amostras)
                        tabela_simulada = pd.DataFrame(np.column_stack((X, y)), columns=[f'X{i+1}' for i in range(num_colunas)] + ['Y'])
                    else:
                        print("Erro: Coeficientes não fornecidos para o modelo linear.")
                        return None

                elif modelo == 'quadratic':
                    if coeficientes:
                        X = np.random.rand(num_amostras, num_colunas)
                        y = np.dot(X**2, coeficientes) + np.random.normal(scale=0.1, size=num_amostras)
                        tabela_simulada = pd.DataFrame(np.column_stack((X, y)), columns=[f'X{i+1}' for i in range(num_colunas)] + ['Y'])
                    else:
                        print("Erro: Coeficientes não fornecidos para o modelo quadrático.")
                        return None

                elif modelo == 'random':
                    tabela_simulada = pd.DataFrame(np.random.rand(num_amostras, num_colunas + 1), columns=[f'X{i+1}' for i in range(num_colunas)] + ['Y'])

                else:
                    print("Erro: Modelo não suportado.")
                    return None

                tabelas_simuladas.append(tabela_simulada)

            return tabelas_simuladas

        except Exception as e:
            print(f"Erro: {e}")
            return None
