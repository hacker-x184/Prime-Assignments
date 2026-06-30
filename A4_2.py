class Book:
    def __init__(self,title,author,li_reviews):
        self.author = author
        self.title = title
        self.li_reviews = li_reviews
    def add_review(self,new_review):
        self.li_reviews.append(new_review)
        print("Review Added sussesful")
    def count(self):
        print("Here is the total no of reviews",len(self.li_reviews))

    def display(self):
        no = 1
        for i in self.li_reviews:
            print(no,". ",i)
            no+=1
        print("Total no of reviews are ", no-1)
    

book1 = Book("Harry Potter","J.K. Rowling",["Amazing book!","Very interesting.","Loved it."])
book1.add_review("I like that")
book1.count()
book1.display()