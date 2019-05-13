import connect

class Info():
 
    def __init__(self, username):
    
            self.username = username.lower()
            # self.information = Storage(self).read()

    def bio(self):
        self.firstname = input('Please enter your Firstname : ')
        self.lastname = input('Please enter your Lastname : ')
        self.parental_background  = input('Wheere you raised by single parents  [yes/no] : ')
        self.employment_record = input('Please enter your Employment Record  [yes/no] : ')
        self.criminal_record = input('Please enter your Criminal Record  [yes/no] : ')

        

    def academic(self):
        self.education_level = input('Are you a graduate [yes/no] : ')
        self.result = input('what class of result do you have [1st class/ 2nd class/ 3rd class] : ')
        self.post_school = input('years after graduation [1-5] : ')
        self.educational_awards = input('Are you a graduate [yes/no] : ')
        
        

    def skills(self):
        self.writing_skill = input('Writing skills [Excellent/Average/poor]: ')
        self.reading_skill = input('Reading skills [Excellent/Average/poor]: ')
        self.communication_skill = input('Communication skills [Excellent/Average/poor]: ')
        self.computer_skill = input('Computer skills [Excellent/Average/poor]: ')
        self.leadership_skill = input('Leadership skills [Excellent/Average/poor]: ')

       
