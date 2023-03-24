question = [
  "Q1) which of the following is are the levels of implementation of data structure",
  "Q2) A binary search tree whose left subtree differ in height by at most 1 unit is called",
  "Q3) ____ level is where the model becomes compatible executable code",
  "Q4) Stack is also called as",
  "Q5) Which of the following is not the part of ADT description?",
  "Q6)_______ is a pile in which items are added at one end and removed from the other",
  "Q7)Which of the following is not the type of queue?",
  "Q8)the property of binary tree is "
]

options = ["A)Abstract level\n B)Application level \nC)implementationlevel\nD)all of the above\n ","A)avl tree \n B)red-black tree \n C)Lemma tree \n D)None of the above\n ",
  "A)Abstract level\n B)Application level \n C)Implementation level\n   D)All of the above\n ",
  "A)Last in first out\n B)First in last out \n C)Last in last out\n D)First in first out\n ",
  "A)Data\n B)Operations \n C)Both of the above\n D)None of the above\n ",
  "A)Stack\n B)Queue \n C)List\n D)None of the above\n ",
  "A)Ordinary Queue\n B)Single ended Queue \n C)Circular Queue\n D)Priority \n ",
  "A)The first subset is called left subtree\n B)The second subtree is called right subtree \n C)The root cannot     contain NULL\n D)The right subtree can be empty\n",
]
answer = ["D", "A", "C", "A", "D", 'B', "B", "D"]
prize = [
  '1000', '2000', '3000', '5000', '10000', '20000', '40000', '60000', '80000'
]
sum = 0
for i in range(len(question)):
  print(question[i], '\n', options[i], '\n')
  ans = input()
  if ans == answer[i]:
    sum += int(prize[i])
    print("you won ", sum)
  else:
    print("Sorry it's the wrong answer\n you won a total of ", sum)
    break
