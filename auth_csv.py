fe=open('auth_writ.csv','w')
writer_no=0
with open('writers.txt','r') as f:
	for line in f:
		line=line.strip()
		fe.write(line+","+str(writer_no)+"\n")
		writer_no=writer_no+1
fe.close()
