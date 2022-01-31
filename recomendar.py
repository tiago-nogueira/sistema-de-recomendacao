import numpy as np
import pandas as pd

NUM_LIVROS = 10000
NUM_USUARIOS = 53424

def recomendar(livros_preferidos):
    similaridades = np.loadtxt(
        './similaridades.csv',
        delimiter=',')
    assert similaridades.shape == (NUM_LIVROS, NUM_LIVROS), \
        ('Forma da matriz de similaridades deveria ser %' % (NUM_LIVROS, NUM_LIVROS))

    escore = np.zeros(10000)
    for i in range(10000):
        for livro_id in livros_preferidos:
            escore[i] += similaridades[i][livro_id - 1]
    
    escore_indices = [(a, i+1) for i, a in enumerate(escore)]
    escore_indices.sort(key=lambda l: l[0], reverse=True)

    livros = pd.read_csv('./books-simpl.csv')
    recomendacoes_ids = [b for (a, b) in escore_indices if b not in livros_preferidos][0:10]
    recomendacoes = []
    for id in recomendacoes_ids:
        livro = livros.iloc[id]
        recomendacoes.append((livro['title'], livro['authors']))
        
    return recomendacoes
