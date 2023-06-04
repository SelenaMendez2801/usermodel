def distance(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result

def get_rates_str_context(a, b):

    if a > b and distance(a, b) == 20:
        return "extremely decreased"
    elif a > b and distance(a, b) == 15:
        return "drastically decreased"
    elif a > b and distance(a, b) == 10:
        return "mediumly decreased"
    elif a > b and distance(a, b) == 5:
        return "slightly decreased"
    elif a == b:
        return "did not change"
    elif a < b and distance(a, b) == 5:
        return "slightly increased"
    elif a < b and distance(a, b) == 10:
        return "mediumly increased"
    elif a < b and distance(a, b) == 15:
        return "drastically increased"
    elif a < b and distance(a, b) == 20:
        return "extremely increased"