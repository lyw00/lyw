# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# Excel 데이터를 데이터프레임으로 변환
df = pd.read_excel(r'C:\Users\USER\Downloads\5674-833_4th\part4\시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

# 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# x, y축 데이터를 plot 함수에 입력
plt.figure(figsize=(14, 5))  # 그래프 크기 설정
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)  # 마커 추가

# 그래프 제목 및 레이블 설정
plt.title('서울 -> 경기도 인구 이동')
plt.xlabel('연도')
plt.ylabel('이동 인구수')

# 눈금 레이블 회전 설정 (x축)
plt.xticks(rotation=45)

# 판다스 객체를 plot 함수에 입력 (또는 위에서 한 것처럼 직접 입력 가능)
plt.plot(sr_one, marker='o', markersize=10)

# 그래프 표시
plt.show()
