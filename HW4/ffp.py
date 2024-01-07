import heapq
from collections import defaultdict

class FartherInFuture:
    def __init__(self, num_in_cache, num_request):
        self.cache_size = num_in_cache
        self.request = []
        self.id_page = 0
        self.page_faults = 0

        self.step_array = [0] * num_request
        self.hash = {}
        self.hash_cache = {}
        self.p_queue_cache = []

    def set_request_sequence(self, request_sequence):
        self.request = request_sequence.split()

    def is_fault(self, new_request):
        return new_request not in self.hash_cache

    def find_step_array(self):
        for i in range(len(self.request) - 1, -1, -1):
            page = self.request[i]
            if page not in self.hash:
                self.hash[page] = i
                self.step_array[i] = float('inf')
            else:
                self.step_array[i] = self.hash[page] - i
                self.hash[page] = i

    def find_key_based_value(self, val):
        for key, value in self.hash_cache.items():
            if value == val:
                return key
        return None

    def get_new_page_request(self):
        if len(self.hash_cache) < self.cache_size:
            if self.is_fault(self.request[self.id_page]):
                self.page_faults += 1
                step = self.step_array[self.id_page] + self.id_page
                self.hash_cache[self.request[self.id_page]] = step
                heapq.heappush(self.p_queue_cache, -step)
        else:
            if self.is_fault(self.request[self.id_page]):
                self.page_faults += 1
                evicted_step = -heapq.heappop(self.p_queue_cache)
                evicted_page = self.find_key_based_value(evicted_step)
                if evicted_page is not None:
                    del self.hash_cache[evicted_page]

                current_step = self.step_array[self.id_page] + self.id_page
                self.hash_cache[self.request[self.id_page]] = current_step
                heapq.heappush(self.p_queue_cache, -current_step)
        self.id_page += 1

    def get_num_faults(self):
        while self.id_page < len(self.request):
            self.get_new_page_request()
        return self.page_faults

instance_list = []

num_instance = int(input())

for _ in range(num_instance):
    cache_size = int(input())
    num_requests = int(input())
    request_sequence = input()

    instance = FartherInFuture(cache_size, num_requests)
    instance.set_request_sequence(request_sequence)
    instance.find_step_array()
    instance_list.append(instance)

for instance in instance_list:
    print(instance.get_num_faults())
