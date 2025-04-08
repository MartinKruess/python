def calc_rest(income, expenses):
    
    result = income - expenses

    if result > 250: result - 150
    if result > 180: result - 100
    if result > 100: result - 50

    return result