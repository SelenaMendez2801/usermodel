import questionnaires
from scenario import Scenario

def create_scenarios():
    scenario1 = Scenario("drinking choice", "drinking water", "drinking sugary drink", ["health","enjoyment", "social acceptance"], "at a party", 3)
    scenario2 = Scenario("bedtime", "sleeping early", "sleeping late", ["health","wealth", "career"],"working deadline", 3)
    scenario3 = Scenario("eating", "eating healthy", "eating unhealthy", ["health","enjoyment", "social acceptance", "wealth"], "dinner party with friends", 4)
    scenario4 = Scenario("exercising", "exercising outside", "watching movie", ["health","enjoyment", "safety", "comfort"], "raining outside", 4)

    return [scenario1, scenario2, scenario3, scenario4]


def create_models():
    rates = questionnaires.questionnaire()

    scenarios[0].rates_base = rates[0][0]
    scenarios[0].rates_context = rates[1][0]

    scenarios[1].rates_base = rates[0][1]
    scenarios[1].rates_context = rates[1][1]

    scenarios[2].rates_base = rates[0][2]
    scenarios[2].rates_context = rates[1][2]

    scenarios[3].rates_base = rates[0][3]
    scenarios[3].rates_context = rates[1][3]


if __name__ == '__main__':
    scenarios = create_scenarios()

    create_models()
    for i, sc in enumerate(scenarios):
        sc.create_summary_file("Scenario " + str(i+1), participant="Name")

