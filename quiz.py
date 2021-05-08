qa_read = open("qa.txt", "r")
qa_data = qa_read.read()
qa_read.close()
qa_data = qa_data.split("\n")
question = []
answer = []
score = 0
user_answer = []
for n, data in enumerate(qa_data, start=0):
    data = data.split("=")
    question.append(data[0])
    answer.append(data[1])
    user_answer.append(input(f"answer the question number {n+1}. {question[n]} = "))

for m, answers in enumerate(user_answer, start=0):
    if answers == answer[m]:
        score = score + 1
n = len(question)
result_write = open("result.txt", "w")
result_write.write(f"user score is {score} / {n} ")
result_write.close()
