from classes.Users import User

class Patient(User):

      viral_level = 0.0

      def getWeight(self):
           return self.weight

      def setWeight(self, value):
            self.weight = value

      def getDetails(self):
            return list(self.firstname,self.lastname,self.height,self.weight)

      def getViralLevel(self,white_blood,red_blood):
            self.viral_level  = red_blood - white_blood

      def getRecords(self, num):
            # use to query Patients records
            pass
      
      
            
            
