# used library
import random as rd

# main function
def genetic_trait_ratio(count = 100000):
    
    # variables
    male = ["A", "a"]
    female = ["A", "a"]
    trait = []
    dpl = 0 # dominant pure line
    crossbread = 0
    rpl = 0 # recessive pure line
    
    # for loop
    for i in range(0,count):
        trait = [rd.choice(male),rd.choice(female)]
        match trait:
            case ["A", "A"]:
                dpl += 1
            case ["A", "a"] | ["a", "A"]:
                crossbread += 1
            case ["a", "a"]:
                rpl += 1

        print(f"{i+1}: {trait}")

    # result
    print("顕性の形質: A, 潜性の形質: a")
    print(f"詳しい比率(["A", "A"] : ["A", "a"] | ["a", "A"] : ["a", "a"]): \n{dpl} : {crossbread} : {rpl}")
    print("簡易比率(基準は純系): \n1 : 2 : 1")
    print(f"形質比(同じような形質を表す物): \n詳しい比率: \n{dpl + crossbread} : {rpl}\n簡易比率: \n3 : 1")

print(genetic_trait_ratio())

