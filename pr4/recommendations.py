from math import sqrt
from scipy.stats import pearsonr

critics = {
 'Кот Матроскин': {
    'Зима в Простоквашино': 2.5,
    'Каникулы в Простоквашино': 3.5,
    'Ёжик в тумане': 3.0,
    'Винни-Пух': 3.5,
    'Ну, погоди!': 2.5,
    'Котёнок по имени Гав': 3.0
 },
 'Пёс Шарик': {
    'Зима в Простоквашино': 3.0,
    'Каникулы в Простоквашино': 3.5,
    'Ёжик в тумане': 1.5,
    'Винни-Пух': 5.0,
    'Котёнок по имени Гав': 3.0,
    'Ну, погоди!': 3.5
 },
 'Почтальон Печкин': {
    'Зима в Простоквашино': 2.5,
    'Каникулы в Простоквашино': 3.0,
    'Винни-Пух': 3.5,
    'Котёнок по имени Гав': 4.0
 },
 'Корова Мурка': {
    'Каникулы в Простоквашино': 3.5,
    'Ёжик в тумане': 3.0,
    'Котёнок по имени Гав': 4.5,
    'Винни-Пух': 4.0,
    'Ну, погоди!': 2.5
 },
 'Телёнок Гаврюша': {
    'Зима в Простоквашино': 3.0,
    'Каникулы в Простоквашино': 4.0,
    'Ёжик в тумане': 2.0,
    'Винни-Пух': 3.0,
    'Котёнок по имени Гав': 3.0,
    'Ну, погоди!': 2.0
 },
 'Галчонок': {
    'Зима в Простоквашино': 3.0,
    'Каникулы в Простоквашино': 4.0,
    'Котёнок по имени Гав': 3.0,
    'Винни-Пух': 5.0,
    'Ну, погоди!': 3.5
 },
 'Дядя Фёдор': {
    'Каникулы в Простоквашино': 4.5,
    'Ну, погоди!': 1.0,
    'Винни-Пух': 4.0
 }
}

def euclidian_distance(vector1, vector2):
    summa = sum([(vector1[i] - vector2[i])**2 for i in range(len(vector1))])
    return sqrt(summa)


def sim_distance(critics, name1, name2):
    # Находим общие фильмы, которые оценены обоими критиками
    common_films = set(critics[name1].keys()) & set(critics[name2].keys())
    
    if common_films:
        v1 = [critics[name1][film] for film in common_films]
        v2 = [critics[name2][film] for film in common_films]
    
        distance = euclidian_distance(v1, v2)
        similarity = 1 / (1 + distance)
        return similarity
    else:
        return 0

def sim_pearson(critics, name1, name2):
    common_films = set(critics[name1].keys()) & set(critics[name2].keys())
    if not common_films:
        return 0
    
    scores1 = [critics[name1][film] for film in common_films]
    scores2 = [critics[name2][film] for film in common_films]
    
    correlation, _ = pearsonr(scores1, scores2)
        
    if correlation == 0:
        return 0
    
    return correlation

def top_matches(critics, name):
    critics_list = []
    for critic in critics:
        if critic == name:
            continue

        common_films = set(critics[critic].keys()) & set(critics[name].keys())

        if not common_films:  # Пропускаем критиков без общих фильмов
            continue
        
        scores1 = [critics[critic][film] for film in common_films]
        scores2 = [critics[name][film] for film in common_films]
        
        correlation = pearsonr(scores1, scores2)[0]
        
        if correlation == 0:
            continue
        
        critics_list.append((critic, correlation))

    critics_list.sort(reverse=True, key=lambda item:item[1])

    if critics_list:
        # Выводим наиболее и наименее похожих
        print(f'Наиболее похожие оценки с критиком {name} у критика {critics_list[0][0]} со схожестью {critics_list[0][1]},')
        print(f'Наименее похожие у {critics_list[-1][0]} со схожестью {critics_list[-1][1]}')
    
    return critics_list
