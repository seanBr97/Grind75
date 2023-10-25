"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letter_counts = {char: 0 for char in ransomNote}
        magazine_letter_counts = {char: 0 for char in magazine}

        for char in ransomNote:
            ransom_letter_counts[char] += 1

        for char in magazine:
            magazine_letter_counts[char] += 1

        for char in ransom_letter_counts.keys():
            if magazine_letter_counts.get(char) != None and magazine_letter_counts[char] >= ransom_letter_counts[char]:
                continue
            else:
                return False

        return True

# same but diff collection of counts. Slightly faster I would think		
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letter_counts = {}
        magazine_letter_counts = {}

        for char in ransomNote:
            if ransom_letter_counts.get(char) != None:
                ransom_letter_counts[char] += 1
            else:
                ransom_letter_counts[char] = 0

        for char in magazine:
            if magazine_letter_counts.get(char) != None:
                magazine_letter_counts[char] += 1
            else:
                magazine_letter_counts[char] = 0

        for char in ransom_letter_counts.keys():
            if magazine_letter_counts.get(char) != None and magazine_letter_counts[char] >= ransom_letter_counts[char]:
                continue
            else:
                return False

        return True
        
# cleaner and faster with Counters
from collections import Counter

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letter_counts = Counter(ransomNote)
        magazine_letter_counts = Counter(magazine)
        
        for char in ransom_letter_counts.keys():
            if magazine_letter_counts.get(char) != None and magazine_letter_counts[char] >= ransom_letter_counts[char]:
                continue
            else:
                return False

        return True