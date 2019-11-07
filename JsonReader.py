import itertools


questions =[]
# with open("true.txt") as fp:
#     for i, line in enumerate(fp):

# # print(questions)

with open("true.txt") as f:
    questions = [line.strip() for line in f if line.strip()]
print(len(questions))
print(questions)
