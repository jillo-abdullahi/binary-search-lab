class binarySearch(list):

	"""Boiler plate for a binary search class"""
	def __init__(self,size,step):
		self.size = size
		self.step = step

		#Generate list based off of size supplied
		if self.size in self.toTwenty():
			self.number_list = self.toTwenty()

		elif self.size in self.toForty():
			self.number_list = self.toForty()

		elif self.size in self.toOneThousand():
			self.number_list = self.toOneThousand()

		self.length = len(self.number_list)

	#This method enables us return a list from the class instantiation.
	#Helped me make sense of these two lines of code:
	#self.one_to_twenty = binarySearch(20, 1)
	#self.one_to_twenty[0]
	def __getitem__(self,index):
		return self.number_list[index]


	#Methods to return lists using list comprehension
	def toTwenty(self):
		return [x for x in range(1,21)]
	def toForty(self):
		return [x for x in range(2,41,2)]
	def toOneThousand(self):
		return [x for x in range(10,1001,10)]

	#Binary search function
	def search(self,number):
		firstIndex = 0
		lastIndex = len(self.number_list) - 1 # 19
		count = 0
		index = -1
		found = False

		#First test if number we are looking is on the first index
		#then test if it's on the last index
		#If found, no need to loop
		if number == self.number_list[firstIndex]:
			index = firstIndex
			found = True
		elif number == self.number_list[lastIndex]:
			found = True
			index = lastIndex

		#At this point the number we are looking for is not on the first or last index
		#Halve our list and check if the number we are looking for is at the mid-point
		#Keep halving and checking if number is equal to midpoint
		while found == False and firstIndex <= lastIndex:
			count += 1
			midpoint = (firstIndex + lastIndex) // 2

			if number == self.number_list[midpoint]:
				found = True
				return {'count': count, 'index': midpoint}
			elif self.number_list[midpoint] < number:
				firstIndex = midpoint + 1
			else:
				lastIndex = midpoint - 1
		#Return -1 as index by default
		return {'count': 0, 'index': index}
