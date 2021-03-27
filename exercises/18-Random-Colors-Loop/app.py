import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black',
                  5:'white',
                  6:'purple',
                  7:'orange',
                  8:'gray',
                  9:'magenta',

              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = []
    #your loop here
    for i in range (0,10,1):
        students_array.append(get_color(i))
    return students_array




print(get_allStudentColors())