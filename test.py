import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Функция для чтения и отображения данных
def load_and_visualize(file):
    data = pd.read_excel(file)
    
    st.write("Первые несколько строк данных:")
    st.write(data.head())

    # Соотношение классов объектов
    st.write("Соотношение классов объектов:")
    class_counts = data['Класс объектов'].value_counts()
    fig, ax = plt.subplots()
    class_counts.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Соотношение классов объектов')
    ax.set_xlabel('Класс объектов')
    ax.set_ylabel('Количество')
    st.pyplot(fig)

    # Компании по году основания
    st.write("Компании по году основания:")
    year_counts = data['Год основания'].value_counts().sort_index()
    fig, ax = plt.subplots()
    year_counts.plot(kind='bar', color='lightgreen', ax=ax)
    ax.set_title('Компании по году основания')
    ax.set_xlabel('Год основания')
    ax.set_ylabel('Количество компаний')
    st.pyplot(fig)

    # Распределение минимальной цены
    st.write("Распределение минимальной цены за кв.м:")
    fig, ax = plt.subplots()
    data['Минимальная цена за кв.м'].plot(kind='hist', bins=10, color='lightcoral', ax=ax)
    ax.set_title('Распределение минимальной цены за кв.м')
    ax.set_xlabel('Минимальная цена за кв.м')
    ax.set_ylabel('Частота')
    st.pyplot(fig)

    # Распределение средней цены
    st.write("Распределение средней цены кв.м:")
    fig, ax = plt.subplots()
    data['Средняя цена кв.м'].plot(kind='hist', bins=10, color='lightblue', ax=ax)
    ax.set_title('Распределение средней цены кв.м')
    ax.set_xlabel('Средняя цена кв.м')
    ax.set_ylabel('Частота')
    st.pyplot(fig)

    # Минимальная и Средняя цена за кв.м по компаниям
    st.write("Минимальная и Средняя цена за кв.м по компаниям:")
    labels = data['Компания']
    min_prices = data['Минимальная цена за кв.м']
    avg_prices = data['Средняя цена кв.м']

    x = range(len(labels))  # X координаты для меток

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x, min_prices, width=0.4, label='Минимальная цена за кв.м', align='center', color='lightcoral')
    ax.bar(x, avg_prices, width=0.4, label='Средняя цена кв.м', align='edge', color='lightblue')
    ax.set_xlabel('Компания')
    ax.set_ylabel('Цена за кв.м')
    ax.set_title('Минимальная и Средняя цена за кв.м по компаниям')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation='vertical')
    ax.legend()
    st.pyplot(fig)

# Заголовок приложения
st.title("Анализ данных по модульному строительству")

# Загрузка файла
uploaded_file = st.file_uploader("Загрузите файл Excel", type="xlsx")

if uploaded_file is not None:
    load_and_visualize(uploaded_file)

