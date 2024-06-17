# # Davaleba 12
# collection = {}

# def add_book(author, title, genre):
#     if author not in collection:
#         collection[author] = []
#     collection[author].append({'title': title, 'genre': genre})
#     print("წიგნი დაემატა კოლექციას.")

# def search_author(author_name):
#     return collection.get(author_name, [])

# def all_books():
#     return collection

# def main():
#     while True:
#         action = input("შეიყვანეთ რომელიმე: (add/title/author/end): ").strip().lower()
#         if action == "end":
#             break
#         elif action == "add":
#             title = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
#             author = input("შეიყვანეთ ავტორის სახელი: ").strip()
#             genre = input("შეიყვანეთ ჟანრი: ").strip()
#             add_book(author, title, genre)
#         elif action == "author":
#             author_name = ("შეიყვანეთ ავტორის სახელი: ").strip()
#             books = search_author(author_name)
#             if books:
#                 print(f"წიგნები {author_name} მიერ:")
#                 for book in books:
#                     print(f"სახელწოდება: {book['title']}, ჟანრი: {book['genre']}")
#             else:
#                 print(f"{author_name} ავტორის სახელით წიგნი არ მოიძებნა.")
#         elif action == "title":
#             title_name = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
#             found = False
#             for author, books in collection.items():
#                 for book in books:
#                     if book['title'].lower() == title_name.lower():
#                         print(f"მოიძებნა: \"{book['title']}\" {author}-ს მიერ, ჟანრი: {book['genre']}")
#                         found = True
#                 if not found:
#                     print(f"წიგნი დასახელებით {title_name} არ მოიძებნა.")
#         elif action == "all":
#             print(all_books())
#         else:
#             print("არასწორი ბრძანება. გთხოვთ შეიყვანოთ რომელიმე: (add/title/author/end): ")

# main()



# # Davaleba 13:
# lst = ["red", "Green", "white", "Black", "Pink", "yellow"]

# file_name = "output.txt"

# with open(file_name, "w") as file:
#     for item in lst:
#         file.write(item + "\n")

# print("List contents have been saved to", file_name)


# def count_uppercase(file_name):
#     uppercase_count = 0

#     with open(file_name, "r") as file:
#         for line in file:
#             line = line.strip()
#             for item in line:
#                 if item.isupper():
#                     uppercase_count += 1
#     return uppercase_count            
    
# file_name = "output.txt"
# uppercase_count = count_uppercase(file_name)
# print("მაღალ რეგისტრში დაწერილი სიტყვების რაოდენობა: ", uppercase_count)



# # Davaleba 14:
# import csv

# def calculate_average_scores(file_name):
#     scores = {}

#     with open(file_name, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             full_name = row["FullName"]
#             score = int(row["Score"])
#             if full_name not in scores:
#                 scores[full_name] = []
#             scores[full_name].append(score)

#     averages = {full_name: sum(scores)/len(scores) for full_name, scores in scores.items()}

#     return scores, averages

# file_name = 'student_scores.csv'
# scores, averages = calculate_average_scores(file_name)

# print(f"Student's scores: {scores}")
# print(f"Average scores: {averages}")



# # Davaleba 16:
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#         self.prices = {
#             "პური": 1.50,
#             "კარაქი": 2.00,
#             "წყალი": 0.75,
#             "ზეთი": 3.50
#         }
    
#     def add_item(self, item_name, quantity):
#         if item_name in self.items:
#             self.items[item_name] += quantity
#         else:
#             self.items[item_name] = quantity

#     def remove_item(self, item_name):
#         if item_name in self.items:
#             del self.items[item_name]

#     def current_items(self):
#         return self.items
    
#     def calculate_total(self):
#         total = 0
#         for item_name, quantity in self.items.items():
#             if item_name in self.prices:
#                 total += self.prices[item_name] * quantity
#         return total

# cart = ShoppingCart()
# cart.add_item("პური", 2)
# cart.add_item("კარაქი", 1)
# cart.add_item("წყალი", 6)
# cart.add_item("ზეთი", 2)

# print("ამჟამად კალათაშია:")
# print(cart.current_items())
# print(f"ჯამი: {cart.calculate_total()}")

# cart.remove_item("ზეთი")

# print("ამჟამად კალათაშია:")
# print(cart.current_items())
# print(f"ჯამი: {cart.calculate_total()}")



# # Davaleba 17:
# class User:
#     def __init__(self, username):
#         self.username = username
#         self.posts = []
#         self.friends = set()

#     def create_post(self, content):
#         post = Post(content, self)
#         self.posts.append(post)
#         return post

#     def like_post(self, post):
#         post.add_like()

# class Post:
#     def __init__(self, content, author):
#         self.content = content
#         self.author = author
#         self.comments = []
#         self.likes = 0

#     def add_comment(self, comment):
#         self.comments.append(comment)

#     def add_like(self):
#         self.likes += 1

# class Comment:
#     def __init__(self, content, author):
#         self.content = content
#         self.author = author

# user1 = User("User1")
# user2 = User("User2")
# user1.friends.add(user2)

# user1.create_post("Today is a great day for studying.")
# post2 = user1.create_post("Went for a nice walk with my dog.")
# post2.add_comment(Comment("I am happy for you", post2))
# user1.like_post(post2)
# user2.like_post(post2)



# # Davaleba 18:
# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
    
#     def __str__(self):
#         return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"
    
# class House:
#     def __init__(self, ID, price, owner=None, status="გასაყიდი"):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = status

#     def sell(self, buyer, loan_amount=0):
#         if loan_amount > 0:
#             buyer.deposit += loan_amount
#             self.owner = buyer
#             self.status = "გაყიდული სესხით"
#             self.owner.loan += loan_amount
#             print(f"The house with ID {self.ID} has been sold with a loan of {loan_amount}.")
#         else:
#             self.owner.deposit += self.price
#             buyer.deposit -= self.price
#             self.owner = buyer
#             self.status = "გაყიდული"
#             print(f"The house with ID {self.ID} has been sold.")

# person1 = Person("Davit Apakidze")
# person2 = Person("Lasha Papava")
# house = House(123, 200000, owner=person1)

# house.price = 220000
# house.sell(person2, loan_amount = 50000)
# print(person1)
# print(person2)



# # Davaleba 19:
# class Roman:
#     def __init__(self):
#         self.roman_numerals = {
#             'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
#             'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
#         }
    
#     def convert_to_decimal(self, roman):
#         decimal = 0
#         previous_value = 0
#         for i in roman[::-1]:
#             value = self.roman_numerals[i]
#             if value < previous_value:
#                 decimal -= value
#             else:
#                 decimal += value

#             previous_value = value
#         return decimal

# result = Roman().convert_to_decimal("MMDVCML")
# print(result)



# # Davaleba 20:
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def printLeafNodes(root):
#     if root is None:
#         return
#     if root.left is None and root.right is None:
#         print(root.value)
#     else:
#         printLeafNodes(root.left)
#         printLeafNodes(root.right)

# def main():
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.left = TreeNode(6)
#     root.right.right = TreeNode(7)

#     print("Leaf nodes of the binary tree:")
#     printLeafNodes(root)

# if __name__ == "__main__":
#     main()



# # Davaleba 21:
# import json

# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     @classmethod
#     def read_json(cls, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             students_data = data["students"]
#             students = []
#             for i in students_data:
#                 student = cls(i["name"], i["age"], i["grades"])
#                 students.append(student)
#             return students

#     @staticmethod    
#     def calculate_average_grade(student):
#         return sum(student.grades) / len(student.grades)
    
#     @staticmethod
#     def write_json(students, filename):
#         average_grades = {student.name: Student.calculate_average_grade(student) for student in students}
#         with open(filename, "w") as file:
#             json.dump(average_grades, file, indent=4)

# def main():
#     students = Student.read_json("C:\\Users\\akoti\\OneDrive - Girteka Competence Center, UAB\\Desktop\\AK.PRG\\Homework\\Homework\\students.json")
#     for student in students:
#         average_grade = Student.calculate_average_grade(student)
#         print(f"{student.name}: {average_grade}")

#     Student.write_json(students, "average_grades.json")

# if __name__ == "__main__":
#     main()