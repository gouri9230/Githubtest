class Student():
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

students_questions = [
    "What is the capital city of India?\na)Delhi\nb)Bangalore\nc)Harayana\n", 
    "Where is Taj Mahal?\na)Gurgaon\nb)Agra\nc)Kanpur\n", 
    "Who is the current president of India?\na)Narendra Modi\nb)Pranab Mukharjee\nc)Ramnath Kovind\n"
] 

questions = [Student(students_questions[0], "a"), Student(students_questions[1], "b"), Student(students_questions[2], "c")]

def test_score(questions):
    score = 0
    for que in questions:
        user_answer = input(que.prompt)
        if (user_answer == que.answer):
            score += 1
    print("You answered " + str(score) + "/" + str(len(students_questions)) + " questions correctly")

test_score(questions)