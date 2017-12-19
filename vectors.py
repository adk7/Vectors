class LengthException(Exception):
	pass


class Vector(object):

	def __init__(self, coordinates):

		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)
		except ValueError:
			raise ValueError("Coordinates cannot be empty")
		except TypeError:
			raise TypeError("Coordinates must be iterable")

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, other):
		return self.coordinates == other.coordinates

	def __add__(self, other):
		if self.dimension != other.dimension:
			raise LengthException("The two vectors must be of same length!!")

		vector_sum = [x + y for x, y in zip(self.coordinates, other.coordinates)]
		return Vector(vector_sum)

	def __sub__(self, other):
		if self.dimension != other.dimension:
			raise LengthException("The two vectors must be of same length!!")

		vector_diff = [x - y for x, y in zip(self.coordinates, other.coordinates)]
		return Vector(vector_diff)

	def __mul__(self, other):
		if isinstance(other, int):
			vector_scaled = [x * other for x in self.coordinates]
			return Vector(vector_scaled)
		else:
			raise TypeError("Can only multipy with scalar integer")



