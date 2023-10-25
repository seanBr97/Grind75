# Check if one word is anagram of other i.e. have same letters, diff order

def get_element_counts(l: []) -> dict:
        counts = {elem: 0 for elem in l}
        for elem in l:
            counts[elem] += 1
        return counts

def isAnagram(self, s: str, t: str) -> bool:                
        s_letter_counts = get_element_counts(s)     
        t_letter_counts = get_element_counts(t)
        
        return s_letter_counts == t_letter_counts