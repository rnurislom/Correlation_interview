# Necessary libraries
import pandas as pd
import numpy as np
# Import data and remove unnecessary data
df = pd.read_csv(r'C:\\Users\\user\\Downloads\\stock_screneer.csv')
df = df.loc[:,~df.columns.str.startswith('Unnamed')]
df = df.loc[:,~df.columns.str.startswith('No')]
df['Change'] = df['Change'].str.replace('%','').astype(float)

# Correlation by Pearson method -> get upper triangle of correlation matrix -> get strong correlations by pearson method
corr = df.corr(method='pearson')
print("strong correlations of Price by pearson method")
print(list(corr['Price'][corr['Price'] > 0.8].index))
print("strong correlations of Change by pearson method")
print(list(corr['Change'][corr['Change'] > 0.8].index))
up_triag = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))
strong = [column for column in up_triag.columns if any(up_triag[column] > 0.8)]
print("strong correlations by pearson method")
print(strong)

# Correlation by Kendall method -> get upper triangle of correlation matrix -> get strong correlations by kendall method
corr = df.corr(method='kendall')
print("strong correlations of Price by kendall method")
print(list(corr['Price'][corr['Price'] > 0.8].index))
print("strong correlations of Change by kendall method")
print(list(corr['Change'][corr['Change'] > 0.8].index))
up_triag = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))
strong = [column for column in up_triag.columns if any(up_triag[column] > 0.95)]
print("strong correlations by kendall method")
print(strong)

# Correlation by Spearman method -> get upper triangle of correlation matrix -> get strong correlations by spearman method
corr = df.corr(method='spearman')
print("strong correlations of Price by spearman method")
print(list(corr['Price'][corr['Price'] > 0.8].index))
print("strong correlations of Change by spearman method")
print(list(corr['Change'][corr['Change'] > 0.8].index))
up_triag = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))
strong = [column for column in up_triag.columns if any(up_triag[column] > 0.95)]
print("strong correlations by spearman method")
print(strong)
