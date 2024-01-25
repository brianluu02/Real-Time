import numpy as np

# Dữ liệu ma trận từ bạn
data = [
    ["T", "S", "D", "O", "Z", "S", "N", "A", "P", "S", "H", "O", "T", "U", "A", "A", "K", "D", "C", "K"],
    ["T", "U", "M", "B", "L", "I", "N", "G", "Y", "J", "B", "S", "E", "B", "T", "G", "N", "Y", "O", "R"],
    ["U", "R", "E", "K", "K", "R", "O", "W", "F", "Q", "A", "N", "O", "I", "T", "P", "Y", "R", "C", "N"],
    ["H", "C", "I", "N", "C", "R", "E", "M", "E", "N", "T", "A", "L", "L", "E", "T", "A", "O", "C", "S"],
    ["T", "O", "K", "G", "T", "C", "N", "F", "A", "P", "X", "M", "L", "F", "B", "Y", "K", "V", "U", "O"],
    ["G", "N", "I", "G", "G", "O", "L", "O", "Q", "A", "M", "S", "O", "A", "Z", "U", "M", "G", "R", "U"],
    ["Q", "S", "I", "C", "E", "E", "Y", "C", "I", "U", "Z", "T", "I", "S", "R", "C", "P", "D", "R", "R"],
    ["M", "I", "O", "O", "Z", "V", "R", "H", "A", "T", "L", "E", "A", "S", "T", "O", "N", "C", "E", "C"],
    ["F", "S", "X", "N", "P", "Z", "C", "E", "U", "H", "A", "O", "M", "D", "Y", "O", "P", "R", "N", "E"],
    ["P", "T", "K", "C", "E", "K", "A", "W", "O", "E", "Y", "Z", "G", "I", "R", "L", "N", "M", "T", "K"],
    ["X", "E", "N", "E", "L", "O", "C", "N", "Q", "N", "C", "P", "I", "N", "T", "Z", "A", "C", "E", "S"],
    ["L", "N", "C", "P", "N", "Q", "N", "E", "O", "T", "E", "N", "E", "R", "I", "L", "H", "N", "E", "T"],
    ["Q", "C", "E", "T", "M", "T", "K", "V", "H", "I", "H", "W", "O", "R", "O", "L", "A", "C", "A", "R"],
    ["W", "Y", "E", "D", "W", "O", "Z", "I", "N", "C", "S", "G", "A", "Y", "L", "H", "A", "E", "G", "E"],
    ["L", "U", "T", "R", "L", "R", "K", "C", "F", "A", "O", "S", "I", "Y", "L", "O", "T", "C", "R", "A"],
    ["G", "M", "R", "I", "P", "X", "E", "T", "Z", "T", "H", "J", "I", "L", "Z", "T", "G", "U", "S", "M"],
    ["T", "V", "B", "F", "M", "I", "F", "I", "B", "I", "H", "G", "I", "M", "F", "R", "C", "L", "A", "I"],
    ["T", "Q", "B", "T", "Q", "I", "K", "O", "T", "O", "S", "D", "Y", "E", "O", "N", "T", "A", "O", "N"],
    ["V", "C", "I", "T", "B", "B", "N", "N", "K", "N", "F", "Z", "G", "I", "W", "L", "I", "G", "X", "G"],
    ["W", "X", "Q", "M", "K", "L", "E", "G", "U", "T", "A", "T", "R", "K", "C", "N", "P", "Y", "T", "E"]
]

# Từ cần tìm
target_word = "concurrent"

# Tìm vị trí của từ trong ma trận

def find_word(matrix, word):
    word_len = len(word)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # Kiểm tra từ theo đường ngang
            if col + word_len <= len(matrix[row]):
                horizontal_word = ''.join(matrix[row][col:col+word_len])
                if horizontal_word == word:
                    return (row, col, row, col + word_len - 1)
            # Kiểm tra từ theo đường chéo xuôi
            if row + word_len <= len(matrix):
                diagonal_word = ''.join(matrix[row+i][col+i] for i in range(word_len))
                if diagonal_word == word:
                    return (row, col, row + word_len - 1, col + word_len - 1)
            # Kiểm tra từ theo đường chéo ngược
            if row - word_len >= -1 and col + word_len <= len(matrix[row]):
                reverse_diagonal_word = ''.join(matrix[row-i][col+i] for i in range(word_len))
                if reverse_diagonal_word == word:
                    return (row, col, row - word_len + 1, col + word_len - 1)

    return None  # Trả về None nếu không tìm thấy từ

# Tìm vị trí của từ "concurrent"
result = find_word(data, target_word)
if result:
    print(f'Tìm thấy từ "{target_word}" tại vị trí: {result}')
else:
    print(f'Không tìm thấy từ "{target_word}" trong ma trận.')
