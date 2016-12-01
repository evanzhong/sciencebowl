import csv
from hello.models import Question

def parse(text):
    rows = text.split("\n")
    types = rows[0].split("\t");

    for row in rows:
        obj = row.split("\t")
        question = Question()
        if len(obj) = 13:
            question.comp = obj[0];
            question.subject = obj[1];
            question.subtopic = obj[2];
            question.question_type = obj[3];
            question.question_text = obj[4];
            question.w = obj[5];
            question.x = obj[6];
            question.y = obj[7];
            question.z = obj[8];
            question.correct = obj[9];
            question.short_answer_answer_text = obj[10];
            question.name = obj[11];
            question.set_number = obj[12];
            question.save()
        else:
            print("failed to write question (length is not right)")
            print(obj)
