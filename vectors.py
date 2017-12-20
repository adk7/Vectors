from __future__ import division
import math


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
		if isinstance(other, (int, float)):
			vector_scaled = [x * other for x in self.coordinates]
			return Vector(vector_scaled)
		elif isinstance(other, Vector):
			dot_prod = math.sqrt(sum([x * x + y * y for x, y in zip(self.coordinates, other.coordinates)]))
			return dot_prod
		else:
			raise TypeError("Can only multiply vector with a scalar integer")

	def magnitude(self):
		total = 0
		for c in self.coordinates:
			total += c * c
		return math.sqrt(total)

	def normalize(self):
		mag = self.magnitude()
		normal_vector = self * (1/mag)
		return normal_vector