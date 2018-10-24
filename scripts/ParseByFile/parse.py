#Documentaition:
#First download google doc of questions as a .txt file then run
#Will parse and output file in following format: *(Note that file will input empty string value "" into indexes where there is a null value)
#Competition	Subject	Subtopic	QuestionType(MC or SA)	QuestionText	w)	x)	y)	Z)	ShortAnswerAnswerTxt	MultipleChoiceAnswerChoice	Author	QuestionCode
delimiter = "\t" #Currently Set to TAB, can change to other chars as needed
sa = False
line = ""
mcSA = ""
tuOb = ""
q = "" 
a = raw_input("Author name: (First Last)")
qc = raw_input("Question code: (i.e. U8)")
c = raw_input("NSB or NOSB? (i.e. NSB)")
s = raw_input("Subject: (i.e. Chemistry)")
sub = raw_input("Subtopic: (i.e. Bonding: General Concepts)")
i = raw_input("File to be Read: (i.e. MyFile.txt)")
o = raw_input("File for output: (i.e. MyOutput.txt)")
f = open(i,'r')
t = open(o, 'w')

t.truncate()
t.write(c.rstrip() + delimiter)
t.write(s.rstrip() + delimiter)
t.write(sub.rstrip() + delimiter)
while line != None:
	line = f.readline()
	print line
	if "Toss-Up" in line:
		tuOb = "Toss-Up"
	elif "Bonus" in line:
		tuOb = "Bonus"
	if "Multiple Choice" in line:
		sa = False
		mcSA = "Multiple Choice"
		t.write(mcSA.rstrip() + delimiter)
		parts = []
		parts = line.split("Multiple Choice", 1)
		t.write(parts[1].rstrip() + delimiter)
	if "Short Answer" in line:
		sa = True
		mcSA = "Short Answer"
		t.write(mcSA.rstrip() + delimiter)
		parts = []
		parts = line.split("Short Answer", 1)
		q = parts[1].rstrip()
	if ")" in line and "Multiple Choice" not in line and "Short Answer" not in line and "Answer" not in line:
		if mcSA == "Short Answer":
			q += " " + line.rstrip()
		if mcSA == "Multiple Choice":
			parts = []
			parts = line.split(")", 1)
			t.write(parts[1].rstrip() + delimiter)
	if "Answer:" in line:
		if sa:
			t.write(q.rstrip() + delimiter)
			t.write("" + delimiter)
			t.write("" + delimiter)
			t.write("" + delimiter)
			t.write("" + delimiter)
			t.write("" + delimiter)
		parts = []
		parts = line.split("Answer:", 1)
		t.write(parts[1].rstrip() + delimiter)
		if not sa:
			t.write("" + delimiter)
		t.write(a.rstrip() + delimiter)
		t.write(qc.rstrip() + delimiter)
		t.write(tuOb.rstrip() + delimiter)
		t.write("\n")
		t.write(c.rstrip() + delimiter)
		t.write(s.rstrip() + delimiter)
		t.write(sub.rstrip() + delimiter)
	if not line:
		break