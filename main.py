import numpy as np


def main():
    alph = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ё': 6, 'Ж': 7, 'З': 8,
            'И': 9, 'Й': 10, 'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16,
            'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х': 22, 'Ц': 23, 'Ч': 24, 'Ш': 25,
            'Ы': 26, 'Я': 27, ' ': 28}
    key = np.array([[8, 0], [3, 5]])
    s1_ish = "Томатный суп"
    s2_ish = "Проросший уд"
    n = key.shape[0]
    s1e = np.array([], dtype='i', ndmin=n)
    s2e = np.array([], dtype='i', ndmin=n)

    j1 = np.array([])
    j2 = np.array([])
    # encrypting
    for i in range(0, 12, n):
        s1n = np.array([], dtype='i', ndmin=n)
        s2n = np.array([], dtype='i', ndmin=n)
        syms1 = s1_ish[i:i+n].upper()
        for j in range(len(syms1)):
            s1n = np.append(s1n, np.array([alph[syms1[j]]], ndmin=n), axis=j-1)
        syms2 = s2_ish[i:i + n].upper()
        for j in range(len(syms2)):
            s2n = np.append(s2n, np.array([alph[syms2[j]]], ndmin=n), axis=j-1)
        j1 = np.append(j1, s1n)
        j2 = np.append(j2, s2n)
        s1ne = np.dot(s1n.transpose(), key)
        s2ne = np.dot(s2n.transpose(), key)
        s1e = np.append(s1e, s1ne)
        s2e = np.append(s2e, s2ne)

    # decrypting
    for i in range(0, 6, n):
        s1 = np.array([], dtype='i', ndmin=n)
        s2 = np.array([], dtype='i', ndmin=n)
        j1n = np.array([], dtype='i', ndmin=n)
        j2n = np.array([], dtype='i', ndmin=n)
        for j in range(n):
            s1 = np.append(s1, np.array([s2e[j+i*2]], ndmin=n), axis=1)
            s2 = np.append(s2, np.array([s2e[j+i*2+2]], ndmin=n), axis=1)
            j1n = np.append(j1n, np.array([j2[j+i*2]], ndmin=n), axis=1)
            j2n = np.append(j2n, np.array([j2[j+i*2+2]], ndmin=n), axis=1)
        s = np.array([s1, s2], dtype='i')
        s = s.reshape(2, 2)
        j = np.array([j1n, j2n], dtype='i')
        j = j.reshape(2, 2)

        if np.linalg.det(j) != 0:
            k = np.dot(np.linalg.inv(j), s)
    print("Исходный текст1:", s1_ish)
    print("Зашифрованный текст1:", s1e%29)
    print("Исходный текст2:", s2_ish)
    print("Зашифрованный текст2", s2e%29)
    print("Найденный ключ:", k)

if __name__ == '__main__':
    main()

