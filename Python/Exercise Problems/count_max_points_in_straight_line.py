def maxPoints(points):
		n=len(points)

		# upto two points all points will be part of the line
		if n<3:
			return n

		max_val=0

		# looping for each point
		for i in points:

			# Creating a dictionary for every new
			# point to save memory
			d = {}
			dups = 0
			cur_max = 0

			# pairing with all other points
			for j in points:
				if i!=j:
					if j[0]==i[0]: #vertical line
						slope='inf'
					else:
						slope=float(j[1]-i[1])/float(j[0]-i[0])

					# Increasing the frequency of slope and
					# updating cur_max for current point(i)
					d[slope] = d.get(slope,0)+1
					cur_max=max(cur_max, d[slope])

				# if both points are equal same increase
				# duplicates count.
				# Please note that this will also increment
				# when we map it with itself.
				# we still do it because we will not have to
				# add the extra one at the end.
				else:
					dups+=1

			max_val=max(max_val, cur_max+dups)

		return max_val

# Driver code
points = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
print(maxPoints(points))
