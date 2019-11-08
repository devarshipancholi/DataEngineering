def calculate(ques, parameters):
    res = []
    i=0
    while (i<len(ques)):
        print("1: Very Inaccurate  2: Moderately Inaccurate  3: Neither Inaccurate Nor Accurate  4: Moderately Accurate  5: Very Accurate")
        ans = int(input(ques[i]+":\t"))
        if (ans < 1 or ans > 5):
            print("Invalid choice. Try again.\n\n")
        else:
            res.append(parameters[i][1]*(ans-1) + parameters[i][0])
            i = i + 1
        print("\n")
    return sum(res)/len(res)


if __name__ == '__main__':
    
    # 1. conscientiousness
    # 2. extraversion
    # 3. openness
    # 4. agreeableness
    # 5. neuroticism
    questions = [["I make a mess of things", "I like order", "I often forget to put things back in their proper place", 
				"I get chores done right away"], ["I am the life of the party",  "I talk to a lot of different people at parties", "I keep in the background", "I don't talk a lot"], ["I Have difficulty understanding abstract ideas", "I do not have a good imagination", "I have vivid imagination", "I am not interested in abstract ideas"], ["I feel other's emotions", "I am not interested in other peoples problems", "I am not really interested in others", "I symphathize with others feelings"], ["I seldom feel blue", "I have frequent mood swings", "I am relaxed most of the time", "I get upset easily"]]
    
    parameters = [[(80, -32), (12, -42), (85, -11), (31, 42)], [(26, 30.75), (21, 28.5), (87, -12.5), (82, -11)], [(89, -29.5), (83, -28), (18, 32.5), (89, -29.5)], [(85, -12.75), (95, -11), (95, -11), (0, 21.5)], [(85, -11.75), (31, 41), (99, -10.25), (21, 31.5)]]
    
    characteristics = ["Conscientiousness", "Extra Version", "Openness", "Agreeableness", "Neuroticism"]
    res = []
    
    for i in range(len(questions)):
        res.append(calculate(questions[i], parameters[i]))
    print("Results: ")
    for i in range(len(res)):
        print(characteristics[i] + " = " + str(res[i]) + "%")
    