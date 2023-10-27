
def get_element_counts(l: str) -> dict:
        counts = {elem: 0 for elem in l}
        for elem in l:
            counts[elem] += 1
        return counts

def longestPalindrome(self, s: str) -> int:
        char_counts = get_element_counts(s)        
        longest_palindrome_length = 0        
        have_middle = False
        
        for char in char_counts.keys():
            if char_counts[char] % 2 == 0:
                longest_palindrome_length += char_counts[char]                        
            
            else:
                longest_palindrome_length += char_counts[char] - 1
                have_middle = True
        
        if have_middle:
            longest_palindrome_length += 1
            
        return longest_palindrome_length