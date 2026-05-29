#May 30 02:13 
#Static method

class Temparature:
    @staticmethod
    def celsius_to_farenheit(c):
        return (c*(9/5))+32
print(Temparature.celsius_to_farenheit(25))