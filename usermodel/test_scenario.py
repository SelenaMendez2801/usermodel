from usermodel.method import get_rates_str_context


def test_get_rates_str_context():
    a = -10
    b = -5
    return "slightly increased" ==  get_rates_str_context(a, b)

def test_get_rates_str_context2():
    a = -10
    b = 0
    return "mediumly increased" == get_rates_str_context(a, b)

def test_get_rates_str_context3():
    a = -10
    b = 5
    return "drastically increased" == get_rates_str_context(a, b)

def test_get_rates_str_context4():
    a = -10
    b = 10
    return "extremely increased" == get_rates_str_context(a, b)

def test_get_rates_str_context5():
    a = -5
    b = -10
    return "slightly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context6():
    a = -5
    b = 0
    return "slightly increased" == get_rates_str_context(a, b)

def test_get_rates_str_context7():
    a = -5
    b = 5
    return "mediumly increased" == get_rates_str_context(a, b)

def test_get_rates_str_context8():
    a = -5
    b = 10
    return "drastically increased" == get_rates_str_context(a, b)

def test_get_rates_str_context9():
    a = 0
    b = -10
    return "mediumly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context10():
    a = 0
    b = -5
    return "slightly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context11():
    a = 0
    b = 5
    return "slightly increased" == get_rates_str_context(a, b)

def test_get_rates_str_context12():
    a = 0
    b = 10
    return "mediumly increased" == get_rates_str_context(a, b)

def test_get_rates_str_context13():
    a = 5
    b = -10
    return "drastically decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context14():
    a = 5
    b = -5
    return "mediumly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context15():
    a = 5
    b = 0
    return "slightly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context16():
    a = 5
    b = 10
    return "slightly increased" == get_rates_str_context(a, b)

def test_get_rates_str_context17():
    a = 10
    b = -10
    return "extremely decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context18():
    a = 10
    b = -5
    return "drastically decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context19():
    a = 10
    b = 0
    return "mediumly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context20():
    a = 10
    b = 5
    return "slightly decreased" == get_rates_str_context(a, b)

def test_get_rates_str_context21():
    a = 10
    b = 10
    return "did not change" == get_rates_str_context(a, b)







