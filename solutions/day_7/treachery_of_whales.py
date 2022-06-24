import sys
from collections import defaultdict

sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')

def text_reader():
    f = open("C:\Python\check-if-want-to-pass-technical-interviews\inputs/day_7/treachery_of_whales.txt", "r")
    return [int(num) for num in f.readline().split(',')]

def treachery_of_whales(positions):
    
    pass

# 435324 < result

positions = [16,1,2,0,4,2,7,1,2,14]
positions = text_reader()
print(treachery_of_whales(positions))
