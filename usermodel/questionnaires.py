

def questionnaire_scenario1(options, options2):
    base1 = []
    context1 = []

    print("Scenario 1: Drink choice")
    print("It is healthy to drink water")
    print(options)
    base1.append(calculate_rate(input()))
    print("It is enjoyable to drink water")
    print(options)
    base1.append(calculate_rate(input()))
    print("It is socially acceptable to drink water")
    print(options)
    base1.append(calculate_rate(input()))
    print("It is healthy to drink sugary drinks")
    print(options)
    base1.append(calculate_rate(input()))
    print("It is enjoyable to drink sugary drinks")
    print(options)
    base1.append(calculate_rate(input()))
    print("It is socially acceptable to drink sugary drinks")
    print(options)
    base1.append(calculate_rate(input()))
    print("Context: At a party")
    print("Does the healthiness of drinking water change when you are at a party?")
    print(options2)
    context1.append(calculate_rate(input()))
    print("Does the enjoyment of drinking water change when you are at a party?")
    print(options2)
    context1.append(calculate_rate(input()))
    print("Does the social acceptance of drinking water change when you are at a party?")
    print(options2)
    context1.append(calculate_rate(input()))
    print("Does the healthiness of drinking sugary drinks change when you are at a party?")
    print(options2)
    context1.append(calculate_rate(input()))
    print("Does the enjoyment of drinking sugary drinks change when you are at a party?")
    print(options2)
    context1.append(calculate_rate(input()))
    print("Does the social acceptance of drinking sugary drinks change when you are at a party?")
    print(options2)
    context1.append(calculate_rate(input()))

    return base1, context1


def questionnaire_scenario2(options, options2):
    base2 = []
    context2 = []

    print("Scenario 2: Bedtime")
    print("It is healthy to go to bed early")
    print(options)
    base2.append(calculate_rate(input()))
    print("Going to bed early increases your wealth")
    print(options)
    base2.append(calculate_rate(input()))
    print("Going to bed early positively influences your career")
    print(options)
    base2.append(calculate_rate(input()))
    print("It is healthy to stay up late")
    print(options)
    base2.append(calculate_rate(input()))
    print("Staying up late increases your wealth")
    print(options)
    base2.append(calculate_rate(input()))
    print("Staying up late positively influences your career")
    print(options)
    base2.append(calculate_rate(input()))
    print("Context: Working deadline")
    print("Does the healthiness of going to bed early change when you have a working deadline?")
    print(options2)
    context2.append(calculate_rate(input()))
    print("Does going to bed early increase your wealth when you have a working deadline?")
    print(options2)
    context2.append(calculate_rate(input()))
    print("Does going to bed early positively influence your career when you have a working deadline?")
    print(options2)
    context2.append(calculate_rate(input()))
    print("Does the healthiness of staying up late change when you have a working deadline?")
    print(options2)
    context2.append(calculate_rate(input()))
    print("Does staying up late increase your wealth when you have a working deadline?")
    print(options2)
    context2.append(calculate_rate(input()))
    print("Does staying up late positively influence your career when you have a working deadline?")
    print(options2)
    context2.append(calculate_rate(input()))

    return base2, context2

def questionnaire_scenario3(options, options2):
    base3 = []
    context3 = []

    print("Scenario 3: Eating healthy")
    print("It is healthy to eat the healthy food option")
    print(options)
    base3.append(calculate_rate(input()))
    print("It is enjoyable to eat the healthy food option")
    print(options)
    base3.append(calculate_rate(input()))
    print("It is socially acceptable to eat the healthy food option")
    print(options)
    base3.append(calculate_rate(input()))
    print("Eating the healthy food option positively influences your wealth")
    print(options)
    base3.append(calculate_rate(input()))
    print("It is healthy to eat the unhealthy food option")
    print(options)
    base3.append(calculate_rate(input()))
    print("It is enjoyable to eat the unhealthy food option")
    print(options)
    base3.append(calculate_rate(input()))
    print("It is socially acceptable to eat the unhealthy food option")
    print(options)
    base3.append(calculate_rate(input()))
    print("Eating the unhealthy food option positively influences your wealth")
    print(options)
    base3.append(calculate_rate(input()))
    print("Context: Dinner with friends")
    print("Does the healthiness of eating the healthy food option change when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does the enjoyment of eating the healthy food option change when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does the social acceptance of eating the healthy food option change when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does eating the healthy food option positively influence your wealth when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does the healthiness of eating the unhealthy food option change when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does the enjoyment of eating the unhealthy food option change when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does the social acceptance of eating the unhealthy food option change when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))
    print("Does eating the unhealthy food option positively influence your wealth when you are at dinner with friends?")
    print(options2)
    context3.append(calculate_rate(input()))

    return base3, context3


def questionnaire_scenario4(options, options2):
    base4 = []
    context4 = []

    print("Scenario 4: Working out")
    print("It is healthy to work out")
    print(options)
    base4.append(calculate_rate(input()))
    print("It is enjoyable to work out")
    print(options)
    base4.append(calculate_rate(input()))
    print("Exercising positively influences your safety")
    print(options)
    base4.append(calculate_rate(input()))
    print("Exercising positively influences your comfort")
    print(options)
    base4.append(calculate_rate(input()))
    print("Staying home and watching a movie is healthy")
    print(options)
    base4.append(calculate_rate(input()))
    print("Staying home and watching a movie is enjoyable")
    print(options)
    base4.append(calculate_rate(input()))
    print("Staying home and watching a movie positively influences your safety")
    print(options)
    base4.append(calculate_rate(input()))
    print("Staying home and watching a movie positively influences your comfort")
    print(options)
    base4.append(calculate_rate(input()))
    print("Context: Raining outside")
    print("Does the healthiness of working out change when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does the enjoyment of working out change when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does exercising positively influence your safety when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does exercising positively influence your comfort when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does the healthiness of staying home and watching a movie change when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does the enjoyment of staying home and watching a movie change when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does staying home and watching a movie positively influence your safety when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))
    print("Does staying home and watching a movie positively influence your comfort when it is raining outside?")
    print(options2)
    context4.append(calculate_rate(input()))

    return base4, context4


def calculate_rate(num):
    if num == str(1):
        return -10
    elif num == str(2):
        return -5
    elif num == str(3):
        return 0
    elif num == str(4):
        return 5
    elif num == str(5):
        return 10



def questionnaire():
    options = "1: Strongly disagree" + "\n" + "2: Slightly disagree" + "\n" + "3: Neutral" + "\n" + "4: Slightly agree" + "\n" + "5: Strongly agree"
    options2 = "1: Highly negative" + "\n" + "2: Mildly negative" + "\n" + "3: Neutral" + "\n" + "4: Mildly positive" + "\n" + "5: Highly positive"

    b1,c1 = questionnaire_scenario1(options, options2)
    b2,c2 = questionnaire_scenario2(options, options2)
    b3, c3 = questionnaire_scenario3(options, options2)
    b4, c4 = questionnaire_scenario4(options, options2)

    print("")
    print(b1,c1,b2,c2,b3,c3,b4,c4)
    print("end")

    return [[b1, b2, b3, b4], [c1, c2, c3, c4]]
