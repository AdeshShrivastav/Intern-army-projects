import random
import time 
import random

questions_answers_GK = {
    "What is the capital of India?\n(a) Mumbai\n(b) New Delhi\n(c) Kolkata\n": "b",
    "Which river is known as the 'Ganga of the South'?\n(a) Godavari\n(b) Yamuna\n(c) Kaveri\n": "c",
    "Who is known as the 'Father of the Nation' in India?\n(a) Jawaharlal Nehru\n(b) Mahatma Gandhi\n(c) Subhash Chandra Bose\n": "b",
    "Which Indian city is famous for its IT industry and is known as the 'Silicon Valley of India'?\n(a) Bengaluru\n(b) Hyderabad\n(c) Chennai\n": "a",
    "Which is the national animal of India?\n(a) Tiger\n(b) Elephant\n(c) Lion\n": "a",
    "What is the national bird of India?\n(a) Peacock\n(b) Sparrow\n(c) Pigeon\n": "a",
    "Who composed the Indian national anthem, 'Jana Gana Mana'?\n(a) Rabindranath Tagore\n(b) Bankim Chandra Chattopadhyay\n(c) Sarojini Naidu\n": "a",
    "In which year did India gain independence from British rule?\n(a) 1945\n(b) 1947\n(c) 1950\n": "b",
    "Which festival is known as the 'Festival of Lights' in India?\n(a) Diwali\n(b) Holi\n(c) Navratri\n": "a",
    "What is the national flower of India?\n(a) Lotus\n(b) Rose\n(c) Jasmine\n": "a","Which Indian state is known as the 'Land of Seven Sisters'?\n(a) Manipur\n(b) Assam\n(c) Mizoram\n": "c",
    "Who was the first woman Prime Minister of India?\n(a) Indira Gandhi\n(b) Sonia Gandhi\n(c) Mayawati\n": "a",
    "Which Indian city is famous for its tea gardens?\n(a) Darjeeling\n(b) Jaipur\n(c) Varanasi\n": "a",
    "What is the national tree of India?\n(a) Banyan\n(b) Neem\n(c) Peepal\n": "c",
    "Who was the first Indian woman to become Miss World?\n(a) Aishwarya Rai\n(b) Sushmita Sen\n(c) Priyanka Chopra\n": "b",
    "Which Indian cricketer has scored the most international centuries?\n(a) Sachin Tendulkar\n(b) Virat Kohli\n(c) Rohit Sharma\n": "a",
    "Which Indian festival marks the victory of good over evil?\n(a) Holi\n(b) Dussehra\n(c) Raksha Bandhan\n": "b",
    "What is the currency of India?\n(a) Rupee\n(b) Dollar\n(c) Euro\n": "a",
    "Who founded the Maurya Empire in ancient India?\n(a) Ashoka\n(b) Chandragupta Maurya\n(c) Akbar\n": "b",
    "Which Indian state is known as the 'Land of Five Rivers'?\n(a) Punjab\n(b) Haryana\n(c) Uttarakhand\n": "a",
    "Who composed the Indian national song, 'Vande Mataram'?\n(a) Rabindranath Tagore\n(b) Bankim Chandra Chattopadhyay\n(c) Subramania Bharati\n": "b",
    "In which year was the Indian Space Research Organisation (ISRO) founded?\n(a) 1969\n(b) 1972\n(c) 1980\n": "a",
    "Which Indian city is famous for its 'Marine Drive'?\n(a) Kolkata\n(b) Mumbai\n(c) Chennai\n": "b",
    "What is the highest civilian award in India?\n(a) Padma Bhushan\n(b) Bharat Ratna\n(c) Padma Vibhushan\n": "b",
    "Who is known as the 'Missile Man of India'?\n(a) Dr. A.P.J. Abdul Kalam\n(b) Dr. Vikram Sarabhai\n(c) Dr. Homi Bhabha\n": "a",
    "Which Indian state is known as the 'Land of the Gods'?\n(a) Himachal Pradesh\n(b) Jammu and Kashmir\n(c) Sikkim\n": "a",
    "Who is known as the 'Nightingale of India'?\n(a) Lata Mangeshkar\n(b) Asha Bhosle\n(c) Sarojini Naidu\n": "c",
    "What is the longest river in India?\n(a) Ganga\n(b) Yamuna\n(c) Brahmaputra\n": "a",
    "Which Indian cricketer has taken the most wickets in Test cricket?\n(a) Anil Kumble\n(b) Kapil Dev\n(c) Ravichandran Ashwin\n": "a",
    "Which Indian state is known as the 'Land of Thunderbolts'?\n(a) Arunachal Pradesh\n(b) Meghalaya\n(c) Nagaland\n": "a",
    "Who is the current Prime Minister of India?\n(a) Narendra Modi\n(b) Rahul Gandhi\n(c) Arvind Kejriwal\n": "a",
    "Which Indian state is known as the 'Land of High Passes'?\n(a) Ladakh\n(b) Uttarakhand\n(c) Jammu and Kashmir\n": "a",
    "Who is known as the 'Iron Man of India'?\n(a) Sardar Vallabhbhai Patel\n(b) Subhas Chandra Bose\n(c) Jawaharlal Nehru\n": "a",
    "What is the national aquatic animal of India?\n(a) Dolphin\n(b) Shark\n(c) Sea Turtle\n": "a",
    "Which Indian state is known as the 'Land of Festivals'?\n(a) Rajasthan\n(b) Uttar Pradesh\n(c) Kerala\n": "c",
    "Who was the first Indian woman to win an individual Olympic medal?\n(a) Karnam Malleswari\n(b) Mary Kom\n(c) Saina Nehwal\n": "a",
    "Which Indian state is known as the 'Land of Diamonds'?\n(a) Maharashtra\n(b) Gujarat\n(c) Madhya Pradesh\n": "b",
    "Who was the first Indian to win the Nobel Prize in Physics?\n(a) C.V. Raman\n(b) Har Gobind Khorana\n(c) Venkatraman Ramakrishnan\n": "a",
    "Which Indian city is known as the 'Pink City'?\n(a) Jaipur\n(b) Jodhpur\n(c) Udaipur\n": "a",
    "Which Indian state is known as the 'Land of Rivers'?\n(a) West Bengal\n(b) Uttar Pradesh\n(c) Bihar\n": "c",
    "What is the national reptile of India?\n(a) Indian Cobra\n(b) Gharial\n(c) Indian Python\n": "b",
    "Who was the first Indian woman to climb Mount Everest?\n(a) Arunima Sinha\n(b) Bachendri Pal\n(c) Santosh Yadav\n": "b",
    "Which Indian state is known as the 'Land of Black Pagoda'?\n(a) Tamil Nadu\n(b) Odisha\n(c) Andhra Pradesh\n": "b",
    "What is the national game of India?\n(a) Cricket\n(b) Football\n(c) Hockey\n": "c",
    "Who founded the Indian National Congress in 1885?\n(a) Mahatma Gandhi\n(b) Dadabhai Naoroji\n(c) A.O. Hume\n": "c",
    "Which Indian state is known as the 'Spice Garden of India'?\n(a) Karnataka\n(b) Kerala\n(c) Andhra Pradesh\n": "b",
    "Who is known as the 'Grand Old Man of India'?\n(a) Motilal Nehru\n(b) Gopal Krishna Gokhale\n(c) Dadabhai Naoroji\n": "c",
    "What is the national dance of India?\n(a) Kathak\n(b) Bharatanatyam\n(c) Odissi\n": "b",
    "Which Indian state is known as the 'Land of White Gold'?\n(a) Punjab\n(b) Gujarat\n(c) Haryana\n": "c"
}

dbms_questions_answers = {
    "What does DBMS stand for?\n(a) Data Business Management System\n(b) Database Management System\n(c) Digital Base Management Software\n": "b",
    "What is the purpose of a primary key in a database table?\n(a) To uniquely identify each row in the table\n(b) To establish relationships between tables\n(c) To store encrypted data\n": "a",
    "What is normalization in DBMS?\n(a) The process of reducing data redundancy and dependency by organizing fields and table of a database\n(b) The process of creating multiple tables to store the same data\n(c) The process of optimizing database queries\n": "a",
    "What is the difference between a database and a DBMS?\n(a) A database is a collection of related data, while a DBMS is software that manages and interacts with databases\n(b) There is no difference, the terms are interchangeable\n(c) A DBMS is a collection of related data, while a database is software that manages and interacts with DBMS\n": "a",
    "What is a foreign key in DBMS?\n(a) A key that uniquely identifies each row in a table\n(b) A key that establishes a relationship between tables\n(c) A key used to encrypt sensitive data\n": "b",
    "What are the ACID properties in DBMS?\n(a) Atomicity, Consistency, Isolation, Durability\n(b) Accuracy, Consistency, Integrity, Durability\n(c) Availability, Consistency, Isolation, Durability\n": "a",
    "What is a view in DBMS?\n(a) A virtual table based on the result of a database query\n(b) A physical table that stores data\n(c) A temporary table used for sorting data\n": "a",
    "What is a trigger in DBMS?\n(a) A stored procedure that is automatically executed in response to certain events on a table\n(b) A mechanism for managing concurrency control\n(c) A constraint that ensures data integrity\n": "a",
    "What is the difference between DELETE and TRUNCATE in SQL?\n(a) DELETE removes all rows from a table, while TRUNCATE removes specific rows\n(b) DELETE removes specific rows from a table, while TRUNCATE removes all rows\n(c) There is no difference, the terms are interchangeable\n": "b",
    "Explain the concept of data integrity in DBMS.\n(a) Ensuring the accuracy, completeness, and consistency of data\n(b) Ensuring the security of data\n(c) Ensuring the availability of data\n": "a",
}

python_questions_answers = {
    "What is Python?\n(a) A high-level programming language\n(b) A snake species\n(c) A type of coffee\n": "a",
    "What is the syntax for declaring a variable in Python?\n(a) var x = 5\n(b) int x = 5\n(c) x = 5\n": "c",
    "What is the purpose of the 'if' statement in Python?\n(a) To declare a loop\n(b) To make decisions based on conditions\n(c) To define a function\n": "b",
    "What is the result of 2 + 3 * 4 in Python?\n(a) 20\n(b) 14\n(c) 18\n": "c",
    "How do you comment out multiple lines in Python?\n(a) // This is a comment //\n(b) /* This is a comment */\n(c) ''' This is a comment '''\n": "c",
    "What is the output of print('Hello, world!') in Python?\n(a) Hello, world!\n(b) 'Hello, world!'\n(c) None\n": "a",
    "What is a list in Python?\n(a) A collection of items in a specific order\n(b) A type of loop\n(c) A conditional statement\n": "a",
    "How do you create an empty list in Python?\n(a) list()\n(b) []\n(c) EmptyList()\n": "b",
    "What is the correct way to access the third element in a list named 'my_list'?\n(a) my_list[3]\n(b) my_list(3)\n(c) my_list[2]\n": "c",
    "What is the difference between '==' and 'is' in Python?\n(a) '==' checks for value equality, 'is' checks for identity\n(b) '==' checks for identity, 'is' checks for value equality\n(c) There is no difference\n": "a",
    "What is the purpose of a for loop in Python?\n(a) To repeat a block of code a specific number of times\n(b) To make decisions based on conditions\n(c) To define a function\n": "a",
    "What is the output of range(5) in Python?\n(a) [0, 1, 2, 3, 4]\n(b) [1, 2, 3, 4, 5]\n(c) [1, 2, 3, 4]\n": "a",
    "What is the result of 'hello' + 'world' in Python?\n(a) hello world\n(b) helloworld\n(c) hello + world\n": "b",
    "What is the purpose of the 'elif' statement in Python?\n(a) To catch any exception that occurs\n(b) To specify multiple conditions\n(c) To end a loop\n": "b",
    "What does the 'in' operator do in Python?\n(a) Checks if a value is present in a sequence\n(b) Assigns a value to a variable\n(c) Performs bitwise AND operation\n": "a",
    "What is the purpose of the 'break' statement in Python?\n(a) To exit a loop prematurely\n(b) To skip the current iteration of a loop\n(c) To resume the next iteration of a loop\n": "a",
    "What is the purpose of the 'continue' statement in Python?\n(a) To exit a loop prematurely\n(b) To skip the current iteration of a loop\n(c) To resume the next iteration of a loop\n": "b",
    "What is the output of len('hello') in Python?\n(a) 4\n(b) 5\n(c) 6\n": "b",
    "What is the purpose of the 'def' keyword in Python?\n(a) To define a function\n(b) To declare a variable\n(c) To import a module\n": "a",
    "What is a dictionary in Python?\n(a) A collection of key-value pairs\n(b) A type of loop\n(c) A conditional statement\n": "a",
    "How do you create an empty dictionary in Python?\n(a) dict()\n(b) {}\n(c) EmptyDict()\n": "b",
    "What is the correct way to access the value associated with the key 'name' in a dictionary named 'my_dict'?\n(a) my_dict['name']\n(b) my_dict(name)\n(c) my_dict[name]\n": "a",
    "What is the output of 'hello'.upper() in Python?\n(a) 'hello'\n(b) 'HELLO'\n(c) 'Hello'\n": "b",
    "What is the purpose of the 'return' statement in Python?\n(a) To exit a function and return a value\n(b) To print a message to the console\n(c) To raise an exception\n": "a",
    "What is the output of 'hello'.split() in Python?\n(a) ['h', 'e', 'l', 'l', 'o']\n(b) ['hello']\n(c) ['hello']\n": "c",
    "What is the purpose of the 'import' statement in Python?\n(a) To export a module\n(b) To import a module\n(c) To define a function\n": "b",
    "What is the output of 5 // 2 in Python?\n(a) 2.5\n(b) 2\n(c) 3\n": "b",
    "What is the purpose of the 'with' statement in Python?\n(a) To open and close files safely\n(b) To define a block of code\n(c) To catch any exception that occurs\n": "a",
    "What is the result of 'hello' * 3 in Python?\n(a) 'hellohellohello'\n(b) 'hello hello hello'\n(c) 'hello3'\n": "a",
    "What is the output of 'hello'.replace('l', 'w') in Python?\n(a) 'hewwo'\n(b) 'hewwo'\n(c) 'hewlo'\n": "a",
    "What is the purpose of the 'global' keyword in Python?\n(a) To declare a global variable\n(b) To define a global function\n(c) To import a module globally\n": "a",
    "What is the output of 'hello'.find('l') in Python?\n(a) 2\n(b) 3\n(c) 4\n": "a",
    "What is the purpose of the 'pass' statement in Python?\n(a) To exit a loop prematurely\n(b) To skip the current iteration of a loop\n(c) To do nothing\n": "c",
    "What is the output of 'hello'.capitalize() in Python?\n(a) 'Hello'\n(b) 'hello'\n(c) 'HELLO'\n": "a",
} 
z = input("Which quiz you want to take \n (a) GK \n (b) python \n (c) DBMS \n ")
if z== "a":
    for i in range(10):
        c = 0
        w= 0
        x,y = random.choice(list(questions_answers_GK.items()))
        print(x)
        z = input("enter answer: ")
        if y == z:
            print("correct")
            c+=1
        else:
            print("wrong")
            w+=1
    if c ==0 :
        print("your marks are 0%")
    else:
        print(f"your marks are {(c+w)/c}% and ")
if z== "b":
    for i in range(10):
        c= 0
        w=0
        x,y = random.choice(list(python_questions_answers.items()))
        print(x)
        n = input("enter answer: ")
        if y == n:
            print("correct")
            c+=1
        else:
            print("wrong")
            w+=1
    if c ==0 :
        print("your marks are 0%")
    else:
        print(f"your marks are {(c+w)/c}%")
if z== "c":
    for i in range(10):
        c= 0
        w=0
        x,y = random.choice(list(dbms_questions_answers.items()))
        print(x)
        n = input("enter answer: ")
        if y == n:
            print("correct")
            c+=1
        else:
            print("wrong")
            w+=1
    if c ==0 :
        print("your marks are 0%")
    else:
        print(f"your marks are {(c+w)/c}%")