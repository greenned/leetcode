class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 실제 데이터를 저장할 딕셔너리
        self.order = []  # 키의 사용 순서를 저장할 리스트
        
    def _move_to_end(self, key: int):
        """키를 가장 최근 사용된 위치로 이동"""
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key: int) -> int:
        if key in self.cache:
            # 최근 사용된 위치로 이동
            self._move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 키가 이미 존재하면 갱신
            self.cache[key] = value
            self._move_to_end(key)
        else:
            # 새 키 추가
            if len(self.cache) >= self.capacity:
                # 가장 오래된 키 제거
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self.order.append(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)