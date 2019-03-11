# 함수
# getEven(0, 100)
# 0 100
# for
def getEven(start, end):
	for i in range(start, end):
		if i == 0:
			continue
		elif (i % 2) == 0:
			print(i)

getEven(0, 10)