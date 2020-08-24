from classes.Users import User

class Doctor(User):
      def __init__(self):
            self.logging_status = 'Falied'

      def login(self, username, password):
            # api will return the status of login
        self.logging_status = 'success'
        if(self.logging_status == 'success'):
            print('successfully logged in')
        else:
            print('Try again')



      def register(self, username, email, password):
        # register username and password
        print('You have successfully registered. Medical records would now be saved')
    
      def updatedetails(self, term, value):
        print('Do you wish to change your'+ term + 'to '+ value)



