import csv
from hello.models import Question

def parse(text):
    rows = text.split("\n")
    types = rows[0].split(",");

    for row in rows:
        obj = row.split(",")
        question = Question()
        if len(obj) > 2:
            question.question_text = obj[3];
            question.w = obj[4];
            question.x = obj[5];
            question.y = obj[6];
            question.z = obj[7];
            question.correct = obj[8];
            question.save()
        else:
            print("failed to write question (length is not right)")
            print(obj)
