from django.db import models
import json

class BlossomFilter:
    def __init__(self, size):
        self.size = size
        self.hash_count = 3
        self.bit_array = [0] * size  

    def _hash(self, item, seed):
        return hash(str(seed) + item) % self.size

    def _hash_multiple(self, item):
        return [self._hash(item, seed) for seed in range(self.hash_count)]

    def add(self, item):
        for index in self._hash_multiple(item):
            self.bit_array[index] = 1

    def check(self, item):
        positions = self._hash_multiple(item)
        return all(self.bit_array[pos] for pos in positions)

    def serialize(self):
        return json.dumps(self.bit_array)  

    def deserialize(self, data):
        self.bit_array = json.loads(data) 

class UniqueNumberCount(models.Model):
    count = models.PositiveIntegerField(default=0)

    def increment_count(self):
        self.count += 1
        self.save()

class BlossomFilterRecord(models.Model):
    unique_number_count = models.ForeignKey(UniqueNumberCount, on_delete=models.CASCADE)
    blossom_filter = models.TextField(null=False, blank=False)

    def load_blossom_filter(self):
        filter_instance = BlossomFilter(size=100)
        if self.blossom_filter:
            filter_instance.deserialize(self.blossom_filter)
            return filter_instance
        return filter_instance

    def save_blossom_filter(self, filter_instance):
        self.blossom_filter = filter_instance.serialize()
        self.save()

