
def create_test(number, name, answers):
    test = {'TotalQuestions':question_count, 'PointsPer':points_per_question, 'TotalPoints':total_points};
    test['EventNum'] = number
    test['EventName'] = name
    test['answers'] = answers
    return test

def write_answers(test):
    title = test['EventNum'] + ' - ' + test['EventName']
    output = ','.join([title,test['EventNum'],test['TotalQuestions'],test['PointsPer'],test['TotalPoints']])
    # Add in a comma to separate the answers from the previous field
    output += ','
    output += ','.join(test['answers'])
    return output
    
question_count = '50'
points_per_question = '25'
total_points = '1000'
lang_answers = ('A','D','B','D','C','C','E','E','E','A','B','D','C','E','A','D','B','C','D','A','D','B','C','E','E','A','B','B','C','D','B','C','A','C','A','C','E','B','D','A','E','B','C','D','A','D','E','C','D','E')
music_answers = ('D','B','B','D','C','C','A','B','B','A','B','B','B','C','E','D','A','C','A','E','E','E','B','E','E','D','A','E','E','D','D','A','C','E','A','C','B','A','E','B','C','A','E','D','B','C','D','C','D','D')
science_answers = ('B','D','A','E','C','D','A','B','D','C','C','D','A','E','B','A','B','C','D','E','A','E','B','A','D','E','C','A','C','D','A','E','B','C','E','B','D','E','C','E','B','B','B','A','C','B','A','D','B','E')

lang_test = create_test('1', 'Lang & Lit',lang_answers)
music_test = create_test('2', 'Music', music_answers)
science_test = create_test('11', 'Science', science_answers)

test_list = (lang_test,music_test,science_test)

for test in test_list:
    print write_answers(test)
