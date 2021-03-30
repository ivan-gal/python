grades = [[['pepe' 'bruce'], [10.0, 20.0, 40.0]],
          [['juan' 'bruce'], [10.30, 20.0, 25.0]],
          [['zapata' 'bruce'], [10.0, 84.0, 40.0]],
          [['coti' 'bruce'], [24.0, 20.0, 90.0]], [
    ['ivan' 'pepe'], [100.0, 30.0, 40.0]],
    [['deadpool'],  []]]


def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats


def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0


print(get_stats(grades))
