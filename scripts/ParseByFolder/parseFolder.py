import os
import re
delimiter = "\t" #Currently Set to TAB, can change to other chars as needed
answerChoices = list()
row = list()
splitFileName = list()

def clear(clearAll):
    MCoSA = ""
    TUoB = ""
    questionText = ""
    subject = "" #(i.e. Chemistry)
    answerChoices[:] = []
    answer = ""
    row[:] = []
    if clearAll:
        splitFileName[:] = []
        subtopic = "" #(i.e. Bonding: General Concepts)
        author = "" #(i.e. Evan Zhong)
        questionCode = "" #(i.e. J8)

print "Thanks for using the science bowl parser!"
print "This parser will work as long as the .txt files approximate the following nomenclature: "
print "\t Evan Zhong J8_ Acid-Base Equilibria [35].txt\n"
print "Downloading question sets from drive should automatically be in the above format."
print "Please also ensure that written questions follow the question template on drive\n"

folderDirectory = raw_input("Relative file path to the folder with the .txt files (e.g. source/): ").strip()
competitionType = raw_input("Parsing NSB or NOSB questions? (i.e. NSB): ").strip()

o = open('o.txt', 'w+')

for filename in os.listdir(folderDirectory):
    clear(True)
    if ".txt" in filename:
        print "Parsing through: " + filename
        fileIn = open(folderDirectory + filename, 'r')
        splitFileName = filename.split("_ ")
        # print splitFileName
        subtopic = splitFileName[1][:splitFileName[1].index(" [")].strip()
        author = re.split("((E|F|U|J|S)[0-9]+)", splitFileName[0], 1)[0].strip()
        questionCode = re.split("((E|F|U|J|S)[0-9]+)", splitFileName[0], 1)[1].strip()

        for line in fileIn:
            # print line

            # Toss-Up or Bonus detection
            if "Toss-Up" in line:
                TUoB = "Toss-Up"
            elif "Bonus" in line:
                TUoB = "Bonus"
            
            # Assigning MC or SA
            if "Multiple Choice" in line:
                MCoSA = "Multiple Choice"
                subject = line.split("Multiple Choice", 1)[0].split(")")[1].strip()
                questionText = line.split("Multiple Choice", 1)[1].strip()
            elif "Short Answer" in line:
                MCoSA = "Short Answer"
                subject = line.split("Short Answer", 1)[0].split(")")[1].strip()
                questionText = line.split("Short Answer", 1)[1].strip()
            
            # SA 1, 2, 3, 4 detection
            if re.compile("[0-9][)]").search(line) and "Multiple Choice" not in line and "Answer" not in line:
                questionText += " " + line.strip()

            # MC w, x, y, z detection
            if re.compile("(W|X|Y|Z|w|x|y|z)[)]").search(line) and "Multiple Choice" not in line and "Answer" not in line:
                answerChoices.append(line.split(")", 1)[1].strip())
            
            # Answer line detection and writing to file
            if "Answer:" in line:
                if MCoSA == "Multiple Choice":
                    answer = line.split("Answer:", 1)[1].strip()
                    row = [competitionType, subject, subtopic, MCoSA, questionText] + (answerChoices) + [answer, "", author, questionCode, TUoB]
                elif MCoSA == "Short Answer":
                    answer = line.split("Answer:", 1)[1].strip()
                    row = [competitionType, subject, subtopic, MCoSA, questionText, "", "", "", "", "", answer, author, questionCode, TUoB]
                o.write(delimiter.join(row) + "\n")
                # print str(row) + "\n\n"
                clear(False)
