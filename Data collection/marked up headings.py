"""

# Размеченные заголовки
"""

import pandas as pd

with open ('Starhit', 'r') as file:
  lines1 = file.readlines()

with open ('Forbes', 'r') as file:
  lines2 = file.readlines()

with open ('Woman', 'r') as file:
  lines3 = file.readlines()

with open ('interfax', 'r') as file:
  lines4 = file.readlines()

with open ('lenta', 'r') as file:
  lines5 = file.readlines()

lines = lines1 + lines2 + lines3 + lines4 + lines5
lines = list(set(lines))

df = pd.DataFrame(lines)

column_name = ['Заголовок']
df.columns = column_name

# @ - не кликбейт, * - кликбейт
def check_symbols(line):
    if '@' in line:
        return 0
    elif '*' in line:
        return 1

new_column = df.applymap(check_symbols)

df['Кликбейт/не кликбейт'] = new_column.max(axis=1).fillna(-1).astype(int)

index = ~((df == -1).any(axis=1))
df = df[index]
df = df.replace({'\*': '', '@': '', '\n': ''}, regex=True)

counts = df['Кликбейт/не кликбейт'].value_counts()

"""1 - кликбейт, 0 - не кликбейт"""

df.to_csv('data.csv', index=False)

"""#Создание датасета, состоящего только из кликбейт-заголовков"""

import pandas as pd

with open ('Starhit', 'r') as file:
  lines1 = file.readlines()

with open ('Forbes', 'r') as file:
  lines2 = file.readlines()

with open ('Woman', 'r') as file:
  lines3 = file.readlines()

with open ('interfax', 'r') as file:
  lines4 = file.readlines()

with open ('lenta', 'r') as file:
  lines5 = file.readlines()

lines = lines1 + lines2 + lines3 + lines4 + lines5
lines = list(set(lines))

df = pd.DataFrame(lines)

column_name = ['Заголовок']
df.columns = column_name

# @ - не кликбейт, * - кликбейт
def check_symbols(line):
    if '@' in line:
        return 0
    elif '*' in line:
        return 1

new_column = df.applymap(check_symbols)

df['Кликбейт/не кликбейт'] = new_column.max(axis=1).fillna(-1).astype(int)

index = ~((df == -1).any(axis=1))
df = df[index]

df = df.replace({'\*': '', '@': '', '\n': ''}, regex=True)

counts = df['Кликбейт/не кликбейт'].value_counts()

"""1 - кликбейт, 0 - не кликбейт"""

clickbait_df = df[df['Кликбейт/не кликбейт'] == 1].copy()

clickbait_df.drop(columns=['Кликбейт/не кликбейт'], inplace=True)

clickbait_df.to_csv('clickbait_data.csv', index=False)

"""# Разделение датасета на тренировочный и тестовый

Разделение исходного датасета на тренировочный и тестовый в соотношении 80% к 20%
"""

train_size = int(len(clickbait_data) * 0.8)
test_size = len(clickbait_data) - train_size

train_df = clickbait_data.sample(n=train_size, random_state=42)
test_df = clickbait_data.drop(train_df.index)

train_df.to_csv('random_sample.csv', index=False)
test_df.to_csv('test_sample.csv', index=False)
