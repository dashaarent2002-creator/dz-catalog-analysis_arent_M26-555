import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},  # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# ---------- Этап 1. Переменные, числа, math ----------


def average_rating(movies):
    """Средняя оценка по каталогу, округленная до одного знака."""
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Кортеж: (самый старый фильм в годах, самый новый в годах, средний возраст)."""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    rest_minutes = minutes % 60
    return f"{hours}ч {rest_minutes}м"

# ---------- Этап 2. Условия и match ----------


def rating_tier(rating):
    """Категория фильма по оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        # тернарный оператор
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Метка по году выпуска через match."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

# ---------- Этап 3. Циклы ----------


def print_not_comedy(movies):
    """Печатает названия всех фильмов, кроме комедий (for + continue)."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies, threshold=9.0):
    """Ищет первый фильм с рейтингом выше threshold (while + break + else)."""
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > threshold:
            print(f"Первый шедевр: {movie['title']} ({movie['rating']})")
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Количество фильмов длиннее threshold минут (накопление в цикле)."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

# ---------- Этап 4. Строки ----------


def normalize_title(title):
    """Приводит строку к Title Case без str.title()."""
    words = title.split(" ")
    new_words = []
    for word in words:
        if word:
            new_words.append(word[0].upper() + word[1:])
    return " ".join(new_words)


def make_slug(title):
    """Превращает название в слаг вида the-quiet-algorithm."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Единая строка с описанием фильма."""
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )

# ---------- Этап 5. Списки ----------


def titles_sorted_by_rating(movies):
    """Список названий по убыванию рейтинга (исходный список не меняется)."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Список из n кортежей (title, rating) — топ по рейтингу."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

# ---------- Этап 6. Словари ----------


def count_by_genre(movies):
    """Словарь {жанр: количество фильмов} через цикл и dict.get()."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Словарь {актер: [список названий фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            films = filmography.get(actor, [])
            films.append(movie["title"])
            filmography[actor] = films
    return filmography


def above_average_ratings(movies):
    """Словарь {title: rating} только для фильмов с рейтингом выше среднего."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

# ---------- Этап 7. Множества ----------


def all_genres(movies):
    """Множество всех уникальных жанров каталога (объединение множеств)."""
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Актеры, снимавшиеся в обоих фильмах (пересечение множеств)."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры, которые есть в movies_a, но нет в movies_b (разность множеств)."""
    return all_genres(movies_a) - all_genres(movies_b)
