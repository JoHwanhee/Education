# for i range(1, 5):
# 	for j range(1, i + 1):
# 		print('*', end='')

# 	print()


# dictionary 
book = {
	"title":"오만과편견",
	"price": 27000
}

#json(가장 인기 많다.) , xml, csv
"""
	{
		"title":"오만과편견",
		"price": 27000,
		
	}
"""


book["price"] = 1000

print(book["title"])

print(book["price"])