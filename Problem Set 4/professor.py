import random


def main():
  level = get_level()
  total_questions = 0
  score = 0
 
  for problems in range(10):
    x, y = generate_integer(level)
    total_wrong = 0
    real_answer = x + y
   
    for _ in range(3):
      try:
        answer = int(input(f"{x} + {y} = ").strip())
       
        if answer != real_answer:
          total_wrong += 1
         
          if total_wrong  == 3:
            print("EEE")
            break
           
          continue
         
        elif answer == real_answer:
          score += 1
          break
      except ValueError:
        print("EEE")
        break
       
    total_questions += 1
   
    if total_questions == 10:
      break

  print(f"Score: {score}")


def get_level():
  while True:
    try:
      level = int(input("Level: ").strip())
     
      if level not in (1, 2, 3):
        raise ValueError
       
      return level
       
    except ValueError:
      continue


def generate_integer(level):
  if level == 1:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
   
  elif level == 2:
    x = random.randint(10, 99)
    y = random.randint(10, 99)
   
  elif level == 3:
    x = random.randint(100, 999)
    y = random.randint(100, 999)

  return x, y

if __name__ == "__main__":
    main()
