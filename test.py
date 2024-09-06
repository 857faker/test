import streamlit as st
import pandas as pd
import numpy as np

st.title('我的第一个 Streamlit 应用')

st.write("这是一个简单的应用示例")

# 创建一个数据框
df = pd.DataFrame({
    '列1': [1, 2, 3, 4],
    '列2': [10, 20, 30, 40]
})

# 显示数据框
st.write(df)

# 创建一个图表
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
