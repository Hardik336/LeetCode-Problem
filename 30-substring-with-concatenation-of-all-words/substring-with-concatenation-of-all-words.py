from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        word_count = Counter(words)
        
        result = []

        # We check word_len different starting points
        for i in range(word_len):
            left = i
            window_count = {}
            count = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    window_count[word] = window_count.get(word, 0) + 1
                    count += 1
                    
                    # If word exceeds required count → shrink
                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If valid window
                    if count == total_words:
                        result.append(left)
                
                else:
                    # Reset window
                    window_count.clear()
                    count = 0
                    left = right + word_len
        
        return result