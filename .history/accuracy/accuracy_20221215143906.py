import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, 'C:/Users/PC/Desktop/webCategorization-main')
from config import datasetPath
from main import x

df = pd.read_csv(datasetPath)
df = df.rename(columns={'main_category:confidence': 'main_category_confidence'})
df = df[['url', 'main_category', 'main_category_confidence']]

df = df[(df['main_category'] != 'Not_working') & (df['main_category_confidence'] >= 0.5)]

X_train, X_test, y_train, y_test = train_test_split(df['url'], df['main_category'],test_size=0.2, random_state = 0)

print(y_test)

df.drop
# display train data
# df.main_category.value_counts().plot(figsize=(12, 5), kind='bar', color='green')
# plt.xlabel('Category')
# plt.ylabel('Total Number Of Individual Category for Training')
# plt.show()

# display test data
# dt =pd.DataFrame({'url':X_test,'main_category':y_test})
# dt.main_category.value_counts().plot(figsize=(12, 5), kind='bar', color='green')
# plt.xlabel('Category')
# plt.ylabel('Total Number Of Individual Category for Training')
# plt.show()

# y_pred=[]
# for i in X_test:
#     res=x(i)
#     if type(res)==tuple:
#         a=res[0]
#         y_pred.append(a)
#     else:
#         y_pred.append('None')

# array=y_test.array
# count=0
# countN=0

# for j in range(len(y_pred)):
#     if y_pred[j]=='None':
#         countN+=1
#     elif y_pred[j]==array[j]:
#         count+=1

# acc=count/(len(y_pred)-countN)
# print(f'Eslesen eleman sayisi : {count}')
# print(f'None eleman sayisi : {countN}')
# print(f'Accuracy Degeri : {acc}')