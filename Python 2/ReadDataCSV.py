import csv 

data = []
train = []
test = []
with open('data.csv', 'rb') as csvfile:
	rows = csv.reader(csvfile,delimiter=',')
	for row in rows:
		if len(row) > 1 :
			data.append(row)
for i in range(0,len(data)):
	if (i+1)%10 == 0:
		test.append(data[i])
	else:
		train.append(data[i])
print train
print "----------"
print test

with open('train.csv','wb') as csvfile:
	writer = csv.writer(csvfile)
	for i in xrange(0,len(train)):
		writer.writerow(train[i])
with open('test.csv','wb') as csvfile:
	writer = csv.writer(csvfile)
	for i in xrange(0,len(test)):
		writer.writerow(test[i])