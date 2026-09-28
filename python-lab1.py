import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def get_decision(weather: str, transport: str) -> str:
    """Логика проверки ошибок и принятия решений."""
    weather = weather.strip().capitalize() if weather else ""
    transport = transport.strip().capitalize() if transport else ""

    if not weather or not transport:
        return ""

    is_weather_valid = weather in ["Солнце", "Дождь"]
    is_transport_valid = transport in ["Есть", "Нет"]

    if not is_weather_valid and not is_transport_valid:
        return "Вводите в поле Погода только Солнце ИЛИ Дождь, а в поле Транспорт только Есть ИЛИ Нет"
    elif not is_weather_valid:
        return "Вводите в поле Погода только Солнце ИЛИ Дождь"
    elif not is_transport_valid:
        return "Вводите в поле Транспорт только Есть ИЛИ Нет"

    if weather == "Солнце":
        return "Горы" if transport == "Есть" else "Парк"
    else:
        return "Дача" if transport == "Есть" else "Дома"


def calculate_decision():
    """Считываем текст из полей и выводим решение."""
    weather_val = entry_weather.get()
    transport_val = entry_transport.get()
    
    result = get_decision(weather_val, transport_val)
    
    if not result:
        lbl_result.configure(text="Заполните оба поля!", text_color="#E6A100")
    elif "Вводите" in result:
        lbl_result.configure(text=f"Ошибка:\n{result}", text_color="#FF4D4D")
    else:
        lbl_result.configure(text=f"Решение: {result}", text_color="#2ECC71")


app = ctk.CTk()
app.title("Программа принятия решений")
app.geometry("520x360")
app.resizable(False, False)

lbl_title = ctk.CTkLabel(app, text="Выбор решения", font=ctk.CTkFont(size=20, weight="bold"))
lbl_title.pack(pady=(20, 15))

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=10, fill="x")

lbl_weather = ctk.CTkLabel(frame, text="Погода:", font=ctk.CTkFont(size=14))
lbl_weather.grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_weather = ctk.CTkEntry(frame, placeholder_text="Солнце / Дождь / ...", width=250)
entry_weather.grid(row=0, column=1, padx=15, pady=10)

lbl_transport = ctk.CTkLabel(frame, text="Транспорт:", font=ctk.CTkFont(size=14))
lbl_transport.grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_transport = ctk.CTkEntry(frame, placeholder_text="Есть / Нет / ...", width=250)
entry_transport.grid(row=1, column=1, padx=15, pady=10)

btn = ctk.CTkButton(app, text="Решение", font=ctk.CTkFont(size=15, weight="bold"), command=calculate_decision, height=38)
btn.pack(pady=15)

lbl_result = ctk.CTkLabel(app, text="Введите данные в поля Погода и Транспорт", font=ctk.CTkFont(size=13, weight="bold"), wraplength=460)
lbl_result.pack(pady=(5, 15))

app.mainloop()