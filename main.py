#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


bf = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# ### Resposta 1

# In[3]:


r1 = (len(bf.index), len(bf.columns))
r1


# ### Resposta 2

# In[4]:


M = bf[bf.Gender == 'F']
r2 = len(M[M.Age == '26-35'].index)
r2


# ### Resposta 3

# In[5]:


r3 = len(bf.groupby(['User_ID']).sum().index)
r3


# ### Resposta 4

# In[6]:


r4 = len(set(bf.dtypes))
r4


# ### Resposta 5

# In[7]:


r5 = (len(bf.index) - len(bf.dropna().index))/len(bf.index)
r5


# ### Resposta 6

# In[8]:


r6 = bf.isna().sum().max()
r6


# ### Resposta 7

# In[9]:


r7 = int(bf['Product_Category_3'].mode())
r7


# ### Resposta 8

# In[32]:


n_bf = (bf['Purchase'] - bf['Purchase'].min()) / (bf['Purchase'].max() - bf['Purchase'].min())
r8 = float(n_bf.mean())
r8


# ### Resposta 9

# In[11]:


p_bf = (bf['Purchase'] - bf['Purchase'].mean()) / bf['Purchase'].std()
r9 = len(p_bf[p_bf <= 1]) - len(p_bf[p_bf < -1])
r9


# ### Resposta 10

# In[31]:


bf = bf[bf['Product_Category_3'].notna()]
r10 = bool(bf['Product_Category_2'].isna().sum() == 0)
r10


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[13]:


def q1():
    return r1


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[14]:


def q2():
    return r2


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[15]:


def q3():
    return r3


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[16]:


def q4():
    return r4


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[17]:


def q5():
    return r5


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[18]:


def q6():
    return r6


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[19]:


def q7():
    return r7


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[20]:


def q8():
    return r8


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[21]:


def q9():
    return r9


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[22]:


def q10():
    return r10

