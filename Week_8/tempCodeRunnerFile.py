     result = 0
        for byte in data:
            result ^= byte
        return result % 256