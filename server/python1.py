class BlossomFilter:
    def __init__(self, size, hash_count):
        self.size = size  # Size of the bit array
        self.hash_count = hash_count  # Number of hash functions
        self.bit_array = [0] * size  # Initialize all bits to 0

    def _hash(self, item, seed):
        # Create hash using Python's hash() function with a given seed
        return (hash(item) + seed) % self.size

    def add(self, item):
        for seed in range(self.hash_count):
            index = self._hash(item, seed)
            self.bit_array[index] = 1

    def check(self, item):
        for seed in range(self.hash_count):
            index = self._hash(item, seed)
            if self.bit_array[index] == 0:
                return False
        return True

# Example usage:
blossom_filter = BlossomFilter(size=100, hash_count=3)  # Using 3 hash functions

# Add items to the filter
blossom_filter.add("example")
blossom_filter.add("test")
blossom_filter.add("python")

# Check items
print(blossom_filter.check("example"))  # Expected: True
print(blossom_filter.check("test"))     # Expected: True
print(blossom_filter.check("python"))   # Expected: True
print(blossom_filter.check("java"))     # Expected: False (may show as False or False positive)
