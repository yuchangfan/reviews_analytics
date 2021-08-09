# reviews_analytics

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('資料讀取完了，總共有', len(data), '筆留言。')

# 計算留言平均長度

sum_len = 0
for review in data:
	sum_len += len(review) # sum_len = sum_len + len(review)

print('每則留言平均有', sum_len / len(data), '個字')