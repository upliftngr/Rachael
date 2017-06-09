class pet:
    number_of_legs = 0

    def run(self):
        print "flash"
    def count_legs(self):
        print "doug have %s legs. " % self.number_of_legs
class dog(pet):
   def bark(self):
       print "big dogs don't bark"

doug = dog()
doug = pet()

doug.run()
doug.number_of_legs = 4
doug.count_legs()

    

fish = pet()
fish.number_of_legs = 0
fish.count_legs()


