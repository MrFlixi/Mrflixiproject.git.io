import math
from tabulate import tabulate

def line(x) :
	print("".center(50, x))
	print()
	return line

print(" Statistics ".center(50, "="))
print(" Grouped data ".center(50, "="))
print()

dataGroup = []
data2 = []
dataGroup = input("Enter data group using commas without spaces = \n").split(",")

n = len(dataGroup)
print(f"\nData length = {n}")

for i in range(n):
	dataGroup[i] = float(dataGroup[i])

sort = []
sort = sorted(dataGroup)

totaldata = 0
for i in range(n) :
	totaldata += dataGroup[i]
	
print(f"Data population = \n{dataGroup}")
print(f"\nSorted data = \n{sort}")
print(f"Total population data = {totaldata}\n")

 #Number ofclasses
print(" Count the number of classes ".center(50, "="))
print("k = 1 + (3.3 (log(n)))")
k = 1 + (3.3 * (math.log10(n)))
K = math.ceil(k)
print(f"k = 1 + (3.3 ({math.log10(n)}))")
print(f"K = {k} ==> {K}")
line("-")

 #Calculating Range
print(" Calculating Range ".center(50, "="))
print("Range = xmax - xmin")
r = max(dataGroup) - min(dataGroup)
print(f"Range = {r}")
line("-")

 #Calculating class Width
print(" Calculating Class Width ".center(50, "="))
print("C = R / K")
c = r  / K
C = math.ceil(c)
print(f"C = {c} ==> {C}")
line("-")

 #automation of end and start value ranges
initialValue = []
#value = []
endValue = []
end = sort[0]
for i in range(K) :
	if i < 1 :
		end += C - 1
	if i >= 1 :
		end += C
	endValue.append(end)

 #automation ofinitial value range
for i in range(K) :
	start = endValue[i] - C + 1
	initialValue.append(start)

 #createa list of 2 value ranges
tbk = []
originalValue = []
newValue = []
dataxi = []
datavalue = []
for i in range(K) :
	sample = []
	dataRange = f"{initialValue[i]} - {endValue[i]}"
	#value.append(dataRange)
	sample = (initialValue[i] +endValue[i]) / 2
	p = (endValue[i] - initialValue[i]) + 1
	tbk2 = initialValue[i] - 0.5
	tbk.append(tbk2)
	newValue = [dataRange]
	originalValue.append(newValue)
	datavalue.append(dataRange)
	dataxi.append(sample)

 #calculate how many value share in a certain range
def countRange(x, min, max) :
	ctr = 0
	for i in x :
		if min <= i <= max :
			ctr += 1
	return ctr
 
 #create a list of the count range that has been created

f1 = []
for i in range(K) :
	initialFreq = countRange(dataGroup, initialValue[i], endValue[i])
	f1.append(initialFreq)


print(" Standard Deviation(S) & Diversity(S²) ".center(50, "="))

totalf1 = 0
for i in range(K) :
	totalf1 = totalf1 + f1[i]

totalxi = 0
for i in range(K) :
	totalxi += dataxi[i]

fixi = []
for i in range(K) :
	newfixi = f1[i] * dataxi[i]
	fixi.append(newfixi)

totalfixi = 0
for i in range(K) :
	totalfixi += fixi[i]

xbar = totalfixi / totalf1

xbarinput = round(xbar, 2)

xi_xbar = []
xi_xbar2 = []
fixbar = []

for i in range(K) :
	xnew2 = dataxi[i] - xbarinput
	xi_xbar.append(round(xnew2, 2))

for i in range(K) :
	xnew = (dataxi[i] - xbarinput)**2
	xi_xbar2.append(xnew)

for i in range(K) :
	fibar = f1[i] *xi_xbar2[i]
	fixbar.append(fibar)

totalxixbar = 0
totalxixbar2 = 0
totalfixbar = 0
for i in range(K) :
	totalxixbar += xi_xbar[i]
for i in range(K) :
	totalxixbar2 += xi_xbar2[i]
for i in range(K) :
	totalfixbar += fixbar[i]

s2 = totalfixbar / (totalf1 - 1)
s = round(math.sqrt(s2), 2)

print(f"Total xbar = fi*xi / fi = {round(xbar, 2)}")
print("S² = fi(xi - xbar)² / totalfi - 1")
print(f"S² = {round(s2, 2)}")
print("S = √S²")
print(f"S = {s}")
line("-")

#average deviation
print(" Average Deviation ".center(50, "="))
absolute = []
sr = []
totalsr = 0
for i in range(K):
	cth = abs(xi_xbar[i])
	absolute.append(cth)
for i in range(K):
	cth2 = f1[i] *absolute[i]
	sr.append(cth2)
for i in range(K) :
	totalsr += sr[i]
SR = totalsr / totalf1
print(f"SR = ΣF|xi - xbar| / ΣF")
print(f"SR = {round(totalsr, 2)} / {totalf1}")
print(f"SR = {round(SR, 2)}")
line("-")

#Quartile median modus
print(" Quartile Formula ".center(50, "="))
print(f"Quartiles = Lo + c (in / 4 - F) / f")
print("""Lo : lower limit of quartile class
c : class width
F : sum of the frequencies of all classes before the quartile class Q
f : quartile class frequency Q""")

fk = []
totalfreq = 0

for i in range(K) :
	totalfreq += f1[i]
	fk.append(totalfreq)

def quartile(q) :
	hitn = (q / 4) * totalf1
	print(f"{q} / 4 * ΣF = {hitn}")
	ket3 = []
	maks = 0
	for i in range(K) :
		ket1 = fk[i] <= hitn
		if ket1 == True :
			ket3.append(fk[i])
			maks = max(ket3)
	
	for i in range(K) :
		ket2 = fk[i] > hitn
		if ket2 == True :
			tbm = tbk[i]
			sigf = fk[i]
			fi = f1[i]
			break
	
	print("Cumulative frequency value before interval =", f"{maks}")
	print("Actual class interval value =", f"{sigf}")
	print("At frequency =".rjust(29), f"{fi}")
	print("p value =".rjust(29), f"{p}")
	print(f"Value tb{q}(Lo) =".rjust(29), f"{tbm}")
	q1 = tbm + ((hitn - maks)  / fi) * p
	print(f"\nQuartile {q} = {tbm} + {p} ( (({q}*{totalf1}) / 4) - {maks}) / {fi}")
	print(f"Quartile {q} =", f"{round(q1, 2)}")
 

line("-")
print(" Quartile 1 ".center(50, "="))
quartile(1)
line("-")

print(" Quartile 2 ".center(50, "="))
quartile(2)
line("-")

print(" Quartile 3 ".center(50, "="))
quartile(3)
line("-")

 #calculate sample data mode

print(" Calculating Modus ".center(50, "="))

for i in range(K) :
	b = max(f1)
	if b == f1[i] :
		tbmode = tbk[i]
		if i == (K - 1):
			b2 = 0
		else :
			b2 = b - f1[i+1]
		if i == (K- k) :
			b1 = 0
		else :
			b1 = b - f1[i- 1]
		break

print(f"Highest frequency data = {b}")
if b1 == 0 :
	mode = tbmode + p * (b1+b2)
else :
	mode = tbmode + p * (b1 / (b1+b2))
	
print("Modus = Lo + c (b1  / b1 +b2)")
print(f"Modus = {tbmode} + {p}({b1} / {b1}+{b2})")
print(f"Modus = {round(mode, 2)}")
line("-")

 #calculatingmedian
print(" Calculating Median ".center(50, "="))
datamedian = []
medn = (totalf1 / 2)
print(f"ΣF / 2 = {medn}")
for i in range(K) :
	ket1 = fk[i] >= medn
	if ket1 == True :
		fmedian = f1[i]
		fsi = fk[i- 1]
		tbmedian = tbk[i]
		break

print(f"Lo median = {tbmedian}")
print(f"Fk True interval = {fmedian}")
median = tbmedian + p * ((medn - fsi) / fmedian)
print("Median = Lo +c ((n / 4 - f) / f ) ")
print(f"Median = {tbmedian} + {p} (({medn} - {fsi}) /  {fmedian})")
print(f"Median = {round(median, 2)}")
line("-")
print()

#print("\nAveragedeviation")



ntable = K + 1
table = []
table2 = []

for i in range(ntable):
	if i < (ntable - 1) :
		table2 = [originalValue[i], f1[i], fk[i], dataxi[i], fixi[i], xi_xbar[i], xi_xbar2[i], fixbar[i], sr[i]]
	elif i == (ntable - 1) :
		table2 = ["Total", totalf1, totalf1, totalxi, totalfixi, totalxixbar, totalxixbar2, totalfixbar, totalsr]
	table.append(table2)

print(tabulate(table, headers= ["Value", "Fi", "Fk", "Xi", "Fi*Xi", "xi - xbar", "(xi - xbar)²", "fi( xi - xbar)²", "fi|xi - xbar|"], tablefmt="grid"))