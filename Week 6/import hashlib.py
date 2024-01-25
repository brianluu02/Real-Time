import hashlib
import math

class Hyperloglog:
    def __init__(self, num_registers):
        self.num_registers = num_registers
        self.registers = [0] * num_registers
    def hash_to_register(self, hash_value):
        binary = bin(hash_value)[2:]
        return len(binary) - binary.rindex('1') - 1
    def add_element(self, element):
        hash_value = hashlib.sha256(element.encode()).hexdigest()
        register_index = self.hash_to_register(int(hash_value, 16))
        self.registers[register_index] = max(self.registers[register_index], self.count_trailing_zeros(hash_value))
    def count_trailing_zeros(self, hash_value):
        return len(hash_value) - len(hash_value.rstrip('0'))
    def estimate_cardinality(self):
        harmonic_mean = sum([2 ** -register for register in self.registers])
        raw_estimate = (self.num_registers ** 2) / harmonic_mean
        return self.apply_bias_correction(raw_estimate)
    def apply_bias_correction(self, estimate):
        if estimate <= 5/2 * self.num_registers:
            zeros = self.registers.count(0)
            return self.num_registers * math.log(self.num_registers / zeros)
        elif estimate <= (1/30) * (2 ** 32):
            return estimate
        else:
            return -2 ** 32 * math.log(1 - (estimate / 2 ** 32))
if __name__ == "__main__":
    num_elements = 10_000
    num_registers = 1024
    hyperloglog = Hyperloglog(num_registers)
    for i in range(num_elements):
        hyperloglog.add_element(str(i))

    estimated_cardinality = hyperloglog.estimate_cardinality()
    print("Estimated Cardinality:", estimated_cardinality)