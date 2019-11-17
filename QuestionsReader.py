import itertools
import Bahr_template 
import doc
import doc2

true_questions =[]
choices_dict = {}
# with open("true.txt") as fp:
#     for i, line in enumerate(fp):

# # print(questions)

with open("true2.txt") as f:
    true_questions = [line.strip() for line in f if line.strip()]


try:
    with open("output.txt") as f:
        for line1 in f:
            line1 = line1.strip()
            line2 = next(f)
            line2 = line2.strip()
            key, values = line1, line2
            choices_dict[key] = values
            keys =  list(choices_dict.keys()) 


except StopIteration:
    pass

print(keys)
print(100*"=")
print([(key, choices_dict[key]) for key in keys])

# for i in range(1,2):

#     x = Bahr_template.BahrTemplateGenerator()

#     x = x.build_pdf(i,true_questions,keys,choices_dict)


for i in range(1,5):

    x = doc.docGenerator()

    x = x.build_pdf(i,true_questions,keys,choices_dict)

    y = doc2.docGenerator()

    y = y.build_pdf(i,true_questions,keys,choices_dict)

    
# x = Bahr_template.BahrTemplateGenerator()

# x = x.build_pdf("khaled2",true_questions)
# x = Bahr_template.BahrTemplateGenerator()

# x = x.build_pdf("khaled3",true_questions)

#Choose only one answer for each of the following question:                             
