class CountMinSketch:
    # Khởi tạo độ rộng, độ sâu, ma trận đếm và các hàm bảng băm
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.count_matrix = [[0] * width for _ in range(depth)]
        self.hash_functions = [self.crc8, self.sum8, self.xor8]

    # Định nghĩa hàm bảng băm crc8
    def crc8(self, data):
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x01:
                    crc = (crc >> 1) ^ 0x8C
                else:
                    crc >>= 1
        return crc

    # Định nghĩa hàm bảng băm sum8
    def sum8(self, data):
        return sum(data) % 256

    # Định nghĩa hàm bảng băm xor8
    def xor8(self, data):
        result = 0
        for byte in data:
            result ^= byte
        return result

    # Định nghĩa hàm để cập nhật khi xử lý dữ liệu tiếp theo
    def update(self, element, count=1):
        for i in range(self.depth):
            hash_value = self.hash_functions[i](str(element).encode())
            index = hash_value % self.width
            self.count_matrix[i][index] += count

    # Định nghĩa hàm để truy vấn và trả về giá trị đếm nhỏ nhất
    def query(self, element):
        min_count = float('inf')
        for i in range(self.depth):
            hash_value = self.hash_functions[i](str(element).encode())
            index = hash_value % self.width
            min_count = min(min_count, self.count_matrix[i][index])
        return min_count

width = 10
depth = 3 # Phải bằng với giá trị số lượng bảng băm

cms = CountMinSketch(width, depth)

# Chuyển dãy đã nhập thành mảng các ký tự đơn lẻ
data_stream = [*(str(input('Nhập vào dãy số liền nhau (Ví dụ: 123456): ')))]

for element in data_stream:
    cms.update(element)

for data in sorted(set(data_stream)):
    print(f'Frequency of {data}: ', cms.query(data))