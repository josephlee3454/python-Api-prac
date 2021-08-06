#!/usr/bin/env python3
##notes
# it IS a dictionary.
# what you're seeing the in browser is a JSON object, which translates to being a python dictionary, so after you use .json() to translate it, you're good to go
import requests
import random

API = "https://opentdb.com/api.php?amount=10&category=9"
questionArr = []
answersArr = []
dicts = {}
scoreR = 0
total = 0
def randy():
  rando = random.randrange(0,len(questionArr))
  # print(rando)
  return rando
  

def ask_ques():
  # print("hello")
  new_rand = randy()
  # print(answersArr[new_rand])
  # print(new_rand)
  count = 0;
  while count < 3:
    
    count += 1
    ask = input(questionArr[new_rand])
    print(answersArr[new_rand])
    if ask == answersArr[new_rand]:
      print("you got the answer correct ")
      # print(scoreR + "out of" + total)
      # count = 3;
      scoreR + 1
      total + 1
      
      break
      
    else:
      print("you got the answer wronfg")
      ask_ques()
      print(scoreR)

def main():

  resp = requests.get(API) 

  data= resp.json()

  for questdict in data["results"]:

    questionArr.append(questdict["question"])
    answersArr.append(questdict["correct_answer"])
   
  
  # print(answersArr)

  count = 0
  while count < 3:
    count += 1
    ask_ques()  
    
  # list = [102, 232, 424]
  # count = 0
  # d = {} #Empty dictionary to add values into

  # for i in list:
  #     d[count] = i
  #     count+=1
    
# okie doke, one sec
if __name__ == "__main__":
  main()
