import matplotlib.pyplot as plt
import random

# --- НАСТРОЙКИ ---
start_length = 10000    # Начальная длина
critical_limit = 500    # Предел Хейфлика (смерть)
max_divisions = 100     # Сколько делений мы симулируем (чтобы не было бесконечного цикла)

# --- 1. СИМУЛЯЦИЯ ОБЫЧНОЙ КЛЕТКИ ---
normal_telomere = start_length
normal_history = [normal_telomere]

for i in range(max_divisions):
    # Клетка теряет кусок теломеры
    loss = random.randint(50, 150) 
    normal_telomere = normal_telomere - loss
    
    # Если умерла - останавливаем запись
    if normal_telomere <= critical_limit:
        normal_telomere = critical_limit # Чтобы график не улетал в минус
        normal_history.append(normal_telomere)
        break 
    
    normal_history.append(normal_telomere)

# --- 2. СИМУЛЯЦИЯ РАКОВОЙ КЛЕТКИ (Telomerase Active) ---
cancer_telomere = start_length
cancer_history = [cancer_telomere]

for i in range(max_divisions):
    loss = random.randint(50, 150)
    # Раковая клетка имеет фермент ТЕЛОМЕРАЗУ, который восстанавливает длину
    growth = random.randint(50, 150) 
    
    # Формула: Старое - потеря + восстановление
    cancer_telomere = cancer_telomere - loss + growth
    
    cancer_history.append(cancer_telomere)

# --- 3. РИСУЕМ ГРАФИКИ ---
plt.figure(figsize=(10, 6)) # Размер картинки

# График обычной клетки (Синий)
plt.plot(normal_history, label='Обычная клетка (Somatic)', color='blue', linewidth=2)

# График раковой клетки (Красный)
plt.plot(cancer_history, label='Раковая клетка (Immortal)', color='red', linewidth=2)

# Линия смерти (Предел Хейфлика)
plt.axhline(y=critical_limit, color='black', linestyle='--', label='Предел Хейфлика')

plt.title("Сравнение: Старение vs Бессмертие (Теломераза)")
plt.xlabel("Количество делений (Поколения)")
plt.ylabel("Длина теломеры (bp)")
plt.legend() # Показать подписи
plt.grid(True) # Сетка
plt.show()
