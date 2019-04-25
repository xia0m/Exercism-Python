def reverse(text):
    return text[::-1]
    # another way
    # ''.join(reversed(text))

# courses = {
#     'spring2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Peter C.'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian',
#                            'assistant': 'Andy'}},
#     'fall2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Sarah'},
#                  'cs212': {'name': 'The Design of Computer Programs',
#                            'teacher': 'Peter N.',
#                            'assistant': 'Andy',
#                            'prereq': 'cs101'},
#                  'cs253': {'name': 'Web Application Engineering - Building a Blog',
#                            'teacher': 'Steve',
#                            'prereq': 'cs101'},
#                  'cs262': {'name': 'Programming Languages - Building a Web Browser',
#                            'teacher': 'Wes',
#                            'assistant': 'Peter C.',
#                            'prereq': 'cs101'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian'},
#                  'cs387': {'name': 'Applied Cryptography',
#                            'teacher': 'Dave'}},
#     'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
#                            'teacher': 'Dorina'},
#                         'cs003': {'name': 'Programming a Robotic Robotics Teacher',
#                            'teacher': 'Jasper'},
#                      }
#     }
# # print(courses['spring2020']['cs101'])
# print('101' in courses['spring2020'])
# for key,value in courses.items():
#   if 'cs101' in value:
#     print(value['cs101'])

# print(courses[0].keys())

# my_list = [3,2,1,0,5]

# def list_sort(my_list):
#   my_list.sort()
#   return my_list
# print(my_list)

# print(list_sort(my_list))

# print(my_list)

# Definition of the generator to produce even numbers.
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2

# my_gen = all_even()

# # Generate the first 5 even numbers.
# for i in range(5):
#     print(next(my_gen))

# # Now go and do some other processing.
# do_something = 4
# do_something += 3
# print(do_something)

# # Now go back to generating more even numbers.
# for i in range(100):
#     print(next(my_gen))

# correct = [[1,2,3],
#            [2,3,1],
#            [3,1,2]]

# incorrect = [[1,2,3,4],
#              [2,3,1,3],
#              [3,1,2,3],
#              [4,4,4,4]]

# incorrect2 = [[1,2,3,4],
#              [2,3,1,4],
#              [4,1,2,3],
#              [3,4,1,2]]

# incorrect3 = [[1,2,3,4,5],
#               [2,3,1,5,6],
#               [4,5,2,1,3],
#               [3,4,5,2,1],
#               [5,6,4,3,2]]

# incorrect4 = [['a','b','c'],
#               ['b','c','a'],
#               ['c','a','b']]

# incorrect5 = [ [1, 1.5],
#                [1.5, 1]]
               
# Define a function check_sudoku() here:
# def check_sudoku(board):
#     ref_num = [1,2,3,4,5,6,7,8,9][0:len(board)]
#     result = True
#     for row in board:
#         print(set(row),set(ref_num))
#         if set(row)!= set(ref_num):
#             result = False
#     if result:
#   total = sum(range(1,len(board)+1))
#   for row in board:
#     if sum(row) != total:
#       print(sum(row),total)
#       return False
#   for i in range(0,len(board)):
#     temp = total
#     for j in range(0,len(board)):
#       temp -= board[j][i]
#     if temp!=0:
#       return False
#   return True



    
    
# print(check_sudoku(incorrect))
# >>> False

# print(check_sudoku(correct))
# >>> True

# print(check_sudoku(incorrect2))
# >>> False

# print(check_sudoku(incorrect3))
# >>> False

# print(check_sudoku(incorrect4))
# >>> False

# print(check_sudoku(incorrect5))
# >>> False

# class Person:
#   def __init__(self,name,age):
#     self.person_name = name
#     self.person_age = age
  
#   def birthday(self):
#     self.person_age +=1

#   def getName(self):
#     return self.person_name

# bob = Person('Bob',32)
# print(bob.person_name)


