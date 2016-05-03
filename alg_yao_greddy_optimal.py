import combi
import math
import sys
from decimal import *
# Calculate Probability

f = open("log.txt",'w')

N = sys.argv[1]
s = sys.argv[2]
f.writeline(getBestM(N,15000000000,pow(2,-s)))
f.close()


def getProb(M,C,N,b,t):
	s = 0
	for k in range(1,N+1):
		#print k
		s = s+ ((pow(-1,k-1))	 * combi.above(N,k) * combi.above(M-C-k*b,t-k*b))

	return Decimal(s)/Decimal(combi.above(M,t))
	#return Decimal(s)/math.factorial(M)

def getProb2(M,C,N,a,b1,b2,t):
	s = 0
	for k in range(1,N+1):
		for x in range(0,k+1):
			s = s+ ((pow(-1,k-1))	 * combi.above(a,x) * combi.above(N-a,k-x) * combi.above(M-C-x*b1-(k-x)*b2,t-x*b1-(k-x)*b2))

	return Decimal(s)/Decimal(combi.above(M,t))

def getMin(M,C,N,b):
	t = 0
	p = 0
	for k in range(1,M-C):

		tmp_p = getProb(M,C,N,b,k)
		print "getMin","M:",M,"C:",C,"N:",N,"b:",b,"k:",k,"tmp_p:",tmp_p
		if(tmp_p > p):
			p = tmp_p
			t = k

	return (p,t)

def getMin2(M,C,N,x,b):
	t = 0
	p = 0
	
	for k in range(1,M-C):
		

		tmp_p = getProb2(M,C,N,x,b,b+1,k)
		print "getMin","M:",M,"C:",C,"N:",N,"b:",b,"k:",k,"tmp_p:",tmp_p
		if(tmp_p > p):
			p = tmp_p
			t = k
			

	return (p,t)

def getBestScheme(M,N):
	bestP = 1
	bestC = 0
	bestB = 0
	for b in range(1,(M-1)/N+1):
		C = M - b*N
		p = getMin(M,C,N,b)[0]
		print "getBestScheme",p
		if(p<bestP):
			bestB = b
			bestC = C
			bestP = p

	return (bestB,bestC,bestP)

def getBestScheme2(M,N):
	bestP = 1
	bestC = 0
	bestB = 0
	X = 0
	for b in range(1,(M-1)/N+1):
		for x in range(0,N+1):
			C = M - b*x - (b+1)*(N-x)
			if C>0:
				p = getMin2(M,C,N,x,b)[0]
				print "getBestScheme",p
				if(p<bestP):
					bestB = b
					bestC = C
					bestP = p
					X = x

	return (bestB,bestC,bestP,X)

def getBestM(N,max,eps):
	M = N+1
	compareM = -1
	for i in range(1,100):
		
		p = getBestScheme(M,N)[2]
		print "getBestM",p
		print eps
		print pow(2,-40)
		#input()
		if(p>eps):
			if compareM!=-1:
				M = (M+compareM)/2
			else:
				M = M*2
		else:
			if(M<compareM or compareM==-1):
				compareM = M
				M = M/2
			else:
				M = (M+compareM)/2

	return M

def getBestM2(N,max,eps):
	M = N+1
	compareM = -1
	for i in range(1,100):
		
		p = getBestScheme2(M,N)[2]
		print "getBestM",p
		print eps
		print pow(2,-40)
		#input()
		if(p>eps):
			if compareM!=-1:
				M = (M+compareM)/2
			else:
				M = M*2
		else:
			if(M<compareM or compareM==-1):
				compareM = M
				M = M/2
			else:
				M = (M+compareM)/2

	return M


#print getProb(1280,1088,32,6,32)
#print getProb(351,95,32,8,12)
#print getProb(351,95,32,8,27)
#print getProb(351,95,32,8,27)
#print getMin(351,95,32,8)
#print getMin(361,137,32,7)
#print getMin(1231,1071,32,5)
#print getProb2(1280,1088,32,32,6,0,32)
#x1 = getMin(1280,1088,32,6)
#x2 = getMin2(1280,1088,32,32,6)
#print x1,x2
#print getBestScheme2(391,32)

#print getBestM(1024,15000000000,pow(2,-40))