import streamlit as st

st.title("Выбор решения")

weather = st.text_input("Погода:", placeholder="Солнце / Дождь / ...")
transport = st.text_input("Транспорт:", placeholder="Есть / Нет / ...")

if st.button("Решение"):
    w = weather.strip().capitalize() if weather else ""
    t = transport.strip().capitalize() if transport else ""

    if not w or not t:
        st.warning("Заполните оба поля!")
    else:
        is_w_valid = w in ["Солнце", "Дождь"]
        is_t_valid = t in ["Есть", "Нет"]

        if not is_w_valid and not is_t_valid:
            st.error("Вводите в поле Погода только Солнце ИЛИ Дождь, а в поле Транспорт только Есть ИЛИ Нет")
        elif not is_w_valid:
            st.error("Вводите в поле Погода только Солнце ИЛИ Дождь")
        elif not is_t_valid:
            st.error("Вводите в поле Транспорт только Есть ИЛИ Нет")
        else:
            res = "Горы" if t == "Есть" else "Парк" if w == "Солнце" else ("Дача" if t == "Есть" else "Дома")
            st.success(f"Решение: {res}")
