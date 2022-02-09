import numpy as np

def np_reverse_range(N):
    return np.array(list(reversed(range(0, N))))

print(np_reverse_range(10))

def np_diag_reverse(N):
    return np.diag(np_reverse_range(10))

print(np_diag_reverse(10))
print(np_diag_reverse(10).diagonal().sum())

# сделаем универсальное решение системы линейных уравнений с 3 переменными
def sys_line_eq_3_var(x1, y1, z1, c1, x2, y2, z2, c2, x3, y3, z3, c3):
    m1 = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
    m2 = np.array([c1, c2, c3])
    return np.linalg.solve(m1, m2)

# а теперь решим уравнение с нашими данными
# 4x + 2y + z = 4, x + 3y = 12, 5y + 4z = -3
print(sys_line_eq_3_var(4, 2, 1, 4, 1, 3, 0, 12,  0, 5, 4, -3))

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])


def cosine(a, b):
    """
    Подсчет косинуса угла между векторами a, b по их координатам
    """
    # длины векторов
    aLength = np.linalg.norm(a)
    bLength = np.linalg.norm(b)
    return np.dot(a, b) / (aLength * bLength)

def find_most_like_user(users_stats, next_user_stats):
    cos_proximities = {}
    like_users = {}
    for i in range(0, len(users_stats)):
        cos_proximities[i] = cosine(users_stats[i], next_user_stats)
    for i, proximity in cos_proximities.items():
        if proximity == max(cos_proximities.values()):
            like_users[i] = [proximity, users_stats[i]]
    return like_users

like_users = find_most_like_user(users_stats, next_user_stats)
print(f'Найдено {len(like_users)} пользователей с одинаковым наилучшим косинусным сходством с пользователем {next_user_stats}')
for (key, value) in like_users.items():
    print(f'ID пользователя: {key}, косинусная близость: {value[0]}, данные этого пользователя: {value[1]}')

