# Is reversed string = normal string?

# Reverse + compare
def isPalindrome(self, s: str) -> bool:
        stripped_str = (re.sub(r'[^0-9a-zA-Z]+', '', s)).lower()
        print(stripped_str)

        reversed_str = stripped_str[::-1]

        for i in range(len(stripped_str)):
            if stripped_str[i] != reversed_str[i]:
                return False
        
        return True
		
# Inplace
def isPalindrome(self, s: str) -> bool:
        stripped_str = (re.sub(r'[^0-9a-zA-Z]+', '', s)).lower()        

        N = len(stripped_str)
        right_index = N-1

        for i in range(N):
            if stripped_str[i] != stripped_str[right_index]:
                return False
            
            right_index -= 1            
            
        return True

# Inplace + sliding window style. Stop in the middle, no need to 'cross over' and keep comparing since we're comparing two sides
def isPalindrome(self, s: str) -> bool:
        stripped_str = (re.sub(r'[^0-9a-zA-Z]+', '', s)).lower()        

        N = len(stripped_str)
        left_index = 0
        right_index = N-1

        while left_index < right_index: # <= works as well but not necessary == --> same character anyway, no need to check
            if stripped_str[left_index] != stripped_str[right_index]:
                return False
            
            left_index += 1
            right_index -= 1            
            
        return True
		
