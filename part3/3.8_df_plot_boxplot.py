# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv(r'C:\Users\USER\Downloads\5674-833_4th\part3\auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 열을 선택하여 박스 플롯 그리기
df[['mpg','cylinders']].plot(kind='box')

import matplotlib.pyplot as plt

plt.show()