##5
def study1():
    ##1
    name1 = "ねずこ"
    name2 = "ぜんいつ"
    print("{}と{}は仲間です".format("ねずこ","ぜんいつ"))
    ##2
    name1 = "ねずこ"
    name2 = "むざん"
    if name2 == "むざん":
        print("仲間ではありません")
    else:
        print("{}と{}は仲間です".format("ねずこ","ぜんいつ"))
    ##3
    name=["たんじろう","ぎゆう","ねずこ","むざん"]
    name.append("ぜんいつ")
    print(name)
    ##4
    for names in name:
        print(names)

study1()

##6
def test(hikisuu):
    hikisuu2 = ["たんじろう","ぎゆう","ねずこ","むざん"]
    for name in hikisuu:
        if name in hikisuu2:
            print("{}が存在します".format(name))
        else:
            print("{}が存在しません".format(name))  

hikisuu = ["たんじろう","ぎゆう","ねずこ","むざん","ぜんいつ"]              
test(hikisuu)