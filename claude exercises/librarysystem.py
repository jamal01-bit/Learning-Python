class book:
 def __init__(self, title, author, genre, bookID):
  self.title = title
  self.author = author
  self.genre = genre
  self.bookID = bookID
  self.available = True
  self.borrower = None
 def checkout(self, borrower_name):
  if self.available == False:
   print('Book unavailable')
  else:
   self.borrower = borrower_name
   print(f'{self.borrower} checked out  {self.title} successfully.')
   self.available = False
 def returnbook(self):
  if self.available == True:
   print(f'{self.title} has not been checked out')
  else:
   self.available = True
   self.borrower = None
   print(f'{self.title} has been returned')
 def displayinfo(self):
  print(f'Title:      {self.title}')
  print(f'Author:     {self.author}')
  print(f'Genre:      {self.genre}')
  print(f'ID:         {self.bookID}')
  print(f'Available:  {self.available}')
  print(f'Borrower:   {self.borrower}')
hp1 = book('Harry Potter 1', 'JK Rowling', 'Fantasy', 1)
hp2 = book('Harry Potter 2', 'JK Rowling', 'Fantasy', 2)
hp1.checkout('alice')
hp1.returnbook()
hp2.returnbook()
hp1.checkout('john')
hp1.checkout('hank')
hp1.displayinfo()
