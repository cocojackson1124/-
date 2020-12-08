class BMI:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def print_bmi1(self):
        getBMI=self.weight/(self.height*self.height)
        getstaus="正常"
        if getBMI<18:
            getstaus="偏瘦"
        elif getBMI<24:
            getstaus="正常"
        elif getBMI<30:
            getstaus="偏胖"
        else:
            getstaus="肥胖"
           
            
        print("{n}的BMI是{m}，他的体型{s}".format(n=self.name,m=getBMI,s=getstaus))
