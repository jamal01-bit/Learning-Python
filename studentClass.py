class Student: 
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa

  def display_info(self):
   print(f'The student {self.name} \'s GPA is  {str(self.gpa)}!')

  
john = Student('john', 11, False, 4.0)
john.display_info()  

