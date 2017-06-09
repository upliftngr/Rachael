class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzzzz"
    def count_legs(self):
        print "doug have %s legs. " % self.number_of_legs
class dog(pet):
   def bark(self):
       print "woof"

doug = dog()
doug = pet()

doug.sleep()
doug.number_of_legs = 4
doug.count_legs()

    

fish = pet()
fish.number_of_legs = 0
fish.count_legs()


