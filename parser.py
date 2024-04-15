#!/usr/bin/python3

SEPARATOR="\t"
FILE_NAME="thw_2022_theory_questions.tsv"
ANKI_IMPORT_FILE="thw_import_plaintext.txt"

class Line:
    def __init__(self, iterator):
        self.line = next(iterator).strip().split(SEPARATOR)

    def get_id(self):
        return self.line[0]

    def get_question_text(self):
        return self.line[1]

    def get_answer(self):
        size = len(self.line)
        if size == 5:
            # id, question, answer, A, X (True)
            return self.line[3], self.line[2], True
        elif size == 4:
            # id, question, answer, A
            return self.line[3], self.line[2], False
        elif size == 3:
            # answer, B|C, X (True)
            return self.line[1], self.line[0], True
        elif size == 2:
            # answer, B|C:
            return self.line[1], self.line[0], False
        else:
            raise RuntimeException


class Question:
    id = ""
    text = ""
    answers = {}

    def to_anki_plaintext(self):
        output = f"{self.text}\t\t1\t" # 1 configures anki card to be "multiple-choice"
        correctness_code = []
        for letter, (answer, correctness) in self.answers.items():
            output+=f"{letter}: {answer}\t"
            correctness_code.append(correctness)
        output+="\t\t" # for unused answers in multiple choice card (answer 4 and 5)
        # results in e.g. "1 0 0" for question with only A correct
        output+= " ".join(["1" if correctness else "0" for correctness in correctness_code]) 
        return output


def parse_file(file_name):
    output = ""
    with open(file_name, "r") as theory_questions:
        iterator = iter(theory_questions)
        try:
            while(iterator):
                question = Question()

                first_line = Line(iterator)
                second_line = Line(iterator)
                third_line = Line(iterator)

                question.id = first_line.get_id()
                question.text = first_line.get_question_text()
                for (letter, answer, correctness) in [line.get_answer() for line in [first_line, second_line, third_line]]:
                    question.answers[letter] = answer,correctness

                output+=f"{question.to_anki_plaintext()}\n"
        except StopIteration:
            print("Finished parsing file")
    return output



def debug(file_name):
    with open(file_name, "r") as theory_questions:
        iterator = iter(theory_questions)
        for line in theory_questions:
            segments = line.strip().split(SEPARATOR) # remove newlines, split on separator
            print(segments)

def write_to_anki(lines, output_file):
    with open(output_file, "w") as anki_file:
        anki_file.write("#separator:tab\n")
        anki_file.write("#html:false\n")
        anki_file.write(lines)


write_to_anki(parse_file(FILE_NAME), ANKI_IMPORT_FILE)

