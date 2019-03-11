# 클래스 클래스명
class Person:
	# 메소드
	def __init__(self, number, name, height):
		# 멤버변수
		self.myNumber = number
		self.name = name
		self.height = height

arr = [ ]
number = 1
while number == 1:
	number = input('너의 번호는..')
	name = input('너의 이름은..')
	height = input('너의 키는..')

	arr.append(Person(number, name, height))

	for person in arr:
		print(person.myNumber)
		print(person.name)
		print(person.height)
