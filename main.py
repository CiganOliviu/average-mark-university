def calculate_class_mark(number_of_credits, mark):
    return mark * number_of_credits


def calculate_average_mark(credits_list, marks_list):

    marks_sum = 0
    length = len(credits_list)

    for item in range(length):
        marks_sum += credits_list[item] * marks_list[item]

    return marks_sum / sum(list_of_credits)


list_of_credits = [5, 5, 5, 5, 3, 3, 2, 2]
list_of_marks = [7, 7, 8, 10, 8, 9, 9, 10]

if __name__ == '__main__':
    print(calculate_average_mark(list_of_credits, list_of_marks))
