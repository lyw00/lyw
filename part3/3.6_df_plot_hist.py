# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r'C:\Users\USER\Downloads\5674-833_4th\part3\남북한발전전력량.xlsx', engine='openpyxl')  # 데이터프레임 변환 

df_ns = df.iloc[[0, 5], 3:]            # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South','North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경

# 행, 열 전치하여 히스토그램 그리기
tdf_ns = df_ns.T
tdf_ns.astype(float).plot(kind='hist')
import matplotlib.pyplot as plt

plt.show()