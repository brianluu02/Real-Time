class CountMinSketch:
    # ... (code khởi tạo và các hàm băm)
# Khởi tạo độ rộng, độ sâu, ma trận đếm và các hàm bảng băm
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.count_matrix = [[0] * width for _ in range(depth)]
        self.hash_functions = [self.crc8, self.sum8, self.xor8]

    # Định nghĩa hàm bảng băm crc8
    def crc8(self, data):  # Add self as the first parameter
            crc = 0
            for byte in data:
                crc ^= byte
                for _ in range(8):
                    if crc & 0x80:
                        crc = (crc << 1) ^ 0x07  # Updated CRC-8 polynomial (0x07)
                    else:
                        crc <<= 1
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
   
    def update(self, element, count=1):
        for i in range(self.depth):
            hash_value = self.hash_functions[i](str(element).encode())
            index = hash_value % self.width
            self.count_matrix[i][index] += count
    def query(self, element):
        min_count = float('inf')
        for i in range(self.depth):
            hash_value = self.hash_functions[i](str(element).encode())
            index = hash_value % self.width
            min_count = min(min_count, self.count_matrix[i][index])
        return min_count   
    # Kiểm tra tính toàn vẹn dữ liệu
    def check_data_integrity(self, data_stream):
        # Tạo một bản sao của CountMinSketch để so sánh
        cms_copy = CountMinSketch(self.width, self.depth)

        # Cập nhật CountMinSketch ban đầu với dữ liệu
        for element in data_stream:
            self.update(element)

        # Duyệt qua dữ liệu ban đầu và cập nhật bản sao của CountMinSketch
        for element in data_stream:
            cms_copy.update(element)

        # So sánh kết quả của CountMinSketch và bản sao
        for element in set(data_stream):
            if self.query(element) != cms_copy.query(element):
                print(f'không đảm bảo tính toàn vẹn dữ liệu {element}')
                return False

        print('dữ liệu nhập vào đảm bảo tính toàn vẹn dữ liệu')
        return True

# Sử dụng CountMinSketch để kiểm tra tính toàn vẹn dữ liệu
width = 10
depth = 3 
cms = CountMinSketch(width, depth)

# Chuyển dãy đã nhập thành mảng các ký tự đơn lẻ
data_stream = [*(str(input('Nhập vào dãy số bất kì.')))]

# Kiểm tra tính toàn vẹn dữ liệu
data_integrity = cms.check_data_integrity(data_stream)



if data_integrity:
    for data in sorted(set(data_stream)):
        print(f'Đếm tần số xuất hiện {data}: ', cms.query(data))
else:
    print('không đảm bảo tính toàn vẹn dữ liệu.')
