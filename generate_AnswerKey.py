
def write_answers(title,test_number,question_count,points_per_question,total_points,answers):
    output = ','.join([title,test_number,question_count,points_per_question,total_points])
    # Add in a comma to separate the answers from the previous field
    output += ','
    output += ','.join(answers)
    return output
    
question_count = '50'
points_per_question = '25'
total_points = '1000'
answers = ('B','D','A','E','C','D','A','B','D','C','C','D','A','E','B','A','B','C','D','E','A','E','B','A','D','E','C','A','C','D','A','E','B','C','E','B','D','E','C','E','B','B','B','A','C','B','A','D','B','E')

test_list = {'11':'Science'}

for test in test_list:
    print write_answers(test + ' - ' + test_list[test], test, question_count, points_per_question, total_points, answers) 
