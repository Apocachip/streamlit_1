import matplotlib
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('차트 그리기 1')

    df = pd.read_csv('data2/iris.csv')

    st.dataframe(df)

    # 차트 그리기
    # sepal_length 와 sepal_width 의 관계를
    # 차트로 나타내시오

    fig = plt.figure()
    plt.scatter(data=df, x = 'sepal_length', y = 'sepal_width')
    plt.title('Sepla Length vs Width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    st.pyplot(fig)
if __name__ == '__main__' :
    main()