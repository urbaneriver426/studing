class TestDynArray(unittest.TestCase):

	def setUp(self):
		self.dynarr = DynArray()

	def testInsertEmpty(self):
		self.dynarr.insert(0,0)
		assert self.dynarr[0] == 0
		assert self.dynarr.capacity == 16
	
	def testInsertHalf(self):
		for i in range(0,5):
			self.dynarr.append(i)
		self.dynarr.insert(0,12)
		assert self.dynarr[0] == 12
		assert self.dynarr.capacity == 16

	def testInsertFull(self):
		for i in range(0,16):
			self.dynarr.append(i)
		self.dynarr.insert(0,12)
		assert self.dynarr[0] == 12
		assert self.dynarr.capacity == 32

	def testInsertWrong(self):
		try:
			self.dynarr.insert(1,1)
		except IndexError:
			print('testInsertWrong: \n"Index is out of bounds"')

	def testDeleteHalf(self):
		for i in range(0,5):
			self.dynarr.append(i)
		self.dynarr.delete(0)
		assert self.dynarr[0] == 1
		assert self.dynarr.capacity == 16

	def testDeleteCapacity(self):
		for i in range(17):
			self.dynarr.append(i)
		print(self.dynarr.count)
		assert self.dynarr.capacity == 32
		for i in range(2):
			self.dynarr.delete(16-i)
		assert self.dynarr.capacity == int(32//1.5)
		print(self.dynarr.count)

	def testDeleteWrong(self):
		try:
			self.dynarr.delete(1)
		except IndexError:
			print('testDeleteWrong: \n"Index is out of bounds"')

if __name__ == '__main__':
    unittest.main()
