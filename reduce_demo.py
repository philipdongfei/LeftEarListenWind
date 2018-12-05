num = [2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]
positive_num = filter(lambda x: x>0, num)
average = reduce(lambda x, y: x+y, positive_num)/len(positive_num)
print average
