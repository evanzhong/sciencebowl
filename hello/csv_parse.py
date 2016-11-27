import csv
from hello.models import Question

def parse(text):
    csv_stuff = csv.DictReader(text, delimiter=',', quotechar='"')
    my_keys =["comp",
              "subject",
              "subtopic",
              "category",
              "name",
              "set_number",
              "date_written",
              "date_last_mod",
              "question_type",
              "question_text",
              "short_answer_answer_text",
              "w",
              "x",
              "y",
              "z",
              "correct",
              "difficulty"]
    for r in csv_stuff:
        result_dict = {}
        for key in my_keys:
            if key in r:
                result_dict[key] = r[key]
            else:
                result_dict[key] = ""
        question = Question(**result_dict)
        question.save()
