import array

# Define CRC-8 hash function
def crc8_hash(data):
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x07
            else:
                crc <<= 1
    return crc

# Define Sum8 hash function
def sum8_hash(data):
    return sum(data) & 0xFF

# Define Xor8 hash function
def xor8_hash(data):
    result = 0
    for byte in data:
        result ^= byte
    return result

# Simple approach
def simple_frequency_count(data_stream):
    """
    Calculate the frequency of all elements in the data stream.

    :param data_stream: The input data stream.
    :return: A dictionary with element frequencies.
    """
    element_frequencies = {}
    for data in data_stream:
        if data in element_frequencies:
            element_frequencies[data] += 1
        else:
            element_frequencies[data] = 1
    return element_frequencies

class CountMinSketch:
    """
    Count-Min Sketch is a probabilistic data structure for estimating the frequency of elements in a data stream.

    :param d: Number of hash functions.
    :param w: Width of the hash table.
    :param hash_functions: List of custom hash functions.
    """
    def __init__(self, d, w, hash_functions):
        self.d = d
        self.w = w
        self.hash_functions = hash_functions
        self.A = [array.array('l', [0] * w) for _ in range(d)]

    def update(self, data):
        """
        Update the Count-Min Sketch with a new data point.

        :param data: The data point to update the sketch.
        """
        for i in range(self.d):
            data_bytes = [data]
            hash_value = self.hash_functions[i](data_bytes) % self.w
            self.A[i][hash_value] += 1

    def estimate_frequency(self, element_to_estimate):
        """
        Estimate the frequency of a specific element using the Count-Min Sketch.

        :param element_to_estimate: The element to estimate its frequency.
        :return: The estimated frequency of the element.
        """
        min_count = float('inf')
        for i in range(self.d):
            element_bytes = [element_to_estimate]
            hash_value = self.hash_functions[i](element_bytes) % self.w
            min_count = min(min_count, self.A[i][hash_value])
        return min_count

# Input data stream
data_stream = list(map(int, input("Enter data stream (comma-separated): ").split(',')))

# Count-Min Sketch
d = 3  # Number of hash functions
w = 10  # Width of the hash table

# Use hash functions
hash_functions = [crc8_hash, sum8_hash, xor8_hash]

cms = CountMinSketch(d, w, hash_functions)

# Update CMS with data stream
for data in data_stream:
    cms.update(data)

# Calculate the frequency of all elements in the data stream
element_frequencies = simple_frequency_count(data_stream)

# Print the frequencies of all elements
for element, frequency in element_frequencies.items():
    estimated_frequency = cms.estimate_frequency(element)
    print(f"The frequency of {element}: \n- With simple approach is {frequency} \n- With Count-min approach is {estimated_frequency}")
