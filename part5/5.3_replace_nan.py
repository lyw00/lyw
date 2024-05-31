# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import seaborn as sns
import numpy as np


# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# age 열의 첫 10개 데이터 출력 (5 행에 NaN 값)
print(df['age'].head(10))
print('\n')

# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis=0)   # age 열의 평균 계산 (NaN 값 제외)
df['age'].fillna(mean_age, inplace=True)

# age 열의 첫 10개 데이터 출력 (5 행에 NaN 값이 평균으로 대체)
print(df['age'].head(10))

df['horsepower'].replace('?', np.nan, inplace=True)
#
# horsepower_dummies = pd.get_dummies(df['hp_bin'])
# 한개만 뜨겁게 변환0 off0 oon2.b=it