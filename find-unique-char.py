# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def find_unique_char(string: str) -> int:
    for char in string:
        if string.count(char) == 1:
            return string.index(char)
    return -1


string = 'aabb'
print(find_unique_char(string=string))

