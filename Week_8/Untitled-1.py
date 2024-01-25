import hashlib
import functools

# Define hash functions
def crc8(data):
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x07  # Updated CRC-8 polynomial (0x07)
            else:
                crc <<= 1
    return crc

def sum8(data):
    return sum(data) % 256

def xor8(data):
    result = 0
    for byte in data:
        result ^= byte
    return result

# Initialize Count-Min Sketch
def init_count_min_sketch(width, depth):
    count_matrix = [[0] * width for _ in range(depth)]
    hash_functions = [crc8, sum8, xor8]
    return count_matrix, hash_functions

# Update Count-Min Sketch
def update_count_min_sketch(cms, element, count=1):
    count_matrix, hash_functions = cms
    for i in range(len(count_matrix)):
        hash_value = hash_functions[i](str(element).encode())
        index = hash_value % len(count_matrix[i])
        count_matrix[i][index] += count

# Query Count-Min Sketch
def query_count_min_sketch(cms, element):
    count_matrix, hash_functions = cms
    min_count = float('inf')
    for i in range(len(count_matrix)):
        hash_value = hash_functions[i](str(element).encode())
        index = hash_value % len(count_matrix[i])
        min_count = min(min_count, count_matrix[i][index])
    return min_count

# Check data integrity
def check_data_integrity(data_stream, width, depth):
    cms = init_count_min_sketch(width, depth)
    cms_copy = init_count_min_sketch(width, depth)

    for element in data_stream:
        update_count_min_sketch(cms, element)
    for element in data_stream:
        update_count_min_sketch(cms_copy, element)

    for element in set(data_stream):
        if query_count_min_sketch(cms, element) != query_count_min_sketch(cms_copy, element):
            print(f'không đảm bảo tính toàn vẹn dữ liệu {element}')
            return False

    print('dữ liệu nhập vào đảm bảo tính toàn vẹn dữ liệu')
    return True

# Your code for data input and integrity check remains the same
width = 10
depth = 3
data_stream = [int(digit) for digit in input('Nhập vào dãy số bất kì: ')]
data_integrity = check_data_integrity(data_stream, width, depth)

if data_integrity:
    for data in sorted(set(data_stream)):
        print(f'Đếm tần số xuất hiện {data}: ', query_count_min_sketch(init_count_min_sketch(width, depth), data))
else:
    print('không đảm bảo tính toàn vẹn dữ liệu.')
