class Solution:
	def readBinaryWatch(self, turnedOn: int) -> List[str]:
		res = []
		hm = [1,2,4,8,1,2,4,8,16,32]
		for i in range(1024):   # 10 digit -> 2**10 = 1024
			ibin = format(i,'b').zfill(10)   # convert i to binary
			if ibin.count('1') == turnedOn:
				h = m = 0
				for j in range(10):
					if ibin[j] == '1':
						if j < 4:
							h += hm[j]
						else:
							m += hm[j]
				if h < 12 and m < 60:
					res.append(str(h)+':'+str(m).zfill(2))
		return res
