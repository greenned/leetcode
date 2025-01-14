class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_map = {}

        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1
        
        words_list = sorted(hash_map.items(), key=lambda x: (-x[1], x[0]))
        
        # Step 3: Extract the top k frequent words
        top_k_words = [word for word, freq in words_list[:k]]
        
        return top_k_words
        



