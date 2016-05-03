
import math
from decimal import Decimal
		

def above(a,b):
	if a-b < 0 or a<0 or b<0:
		return 0
	return (math.factorial(a) / (math.factorial(b)*math.factorial(a-b)))
