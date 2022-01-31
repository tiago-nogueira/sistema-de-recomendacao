# Sistema de recomendação
Sistema de recomendação usando filtragem colaborativa baseada em itens com similaridade de cosseno, implementado em python.

Este sistema foi feito seguindo este artigo de Muffaddal Qutbuddin (com modificação no cálculo do escore):  
https://towardsdatascience.com/comprehensive-guide-on-item-based-recommendation-systems-d67e40e2b75d

O dataset usado foi o goodbooks-10k, criado por Zygmunt Zajac, disponível aqui:  
http://fastml.com/goodbooks-10k-a-new-dataset-for-book-recommendations/  
(usei apenas os arquivos 'ratings.csv' e 'books.csv')

## Descrição dos arquivos
### recomendar.py
Faz a recomendação de livros personalizada, baseado nos livros preferidos da pessoa, utilizando-se da matriz de similaridades (calculada em outro arquivo).  
Entrada: Lista com os ids dos livros preferidos, de acordo com o dataframe 'books.csv'.  
Saída: Lista com 10 tuples, com os títulos e autores dos livros indicados

### Análise_exploratória.ipynb
Análise exploratória do dataset 'ratings.csv'

### dataset_books_simplificação.ipynb
Simplifica o dataset 'books.csv', eliminando as colunas não usadas

### item_based.ipynb
Calcula a matriz de similaridades
