from Cl701g import *

def main():
  try:
    ppl = []
    with open("data/prog701g.dat", 'r') as f:
      num = int(f.readline())
      while num != 99:
        fn = f.readline()
        ln = f.readline()
        if num == 1:
          gpa = float(f.readline())
          p = Student(fn, ln, gpa)
          ppl.append(p)
        elif num == 2:
          numStu = int(f.readline())
          p = Teacher(fn, ln, numStu)
          ppl.append(p)
        elif num == 3:
          favW = f.readline().strip()
          p = Admin(fn, ln, favW)
          ppl.append(p)
        num = int(f.readline())
      tot = 0.0
      cnt = 0
      totStu = 0
      lrg = ""
      sm = "reoororokrkktkfdsfkgsdsfsfs"

      for person in ppl:
        if isinstance(person, Student):
          tot += person.gpa
          cnt += 1
        if isinstance(person, Teacher):
          totStu += person.numStu
          cnt += 1
        if isinstance(person, Admin):
          favW = person.favW
          if len(favW) > len(lrg):
            lrg = favW
          if len(favW) < len(sm):
            sm = favW
          cnt += 1

      print("Average student GPA is: ", round(tot / cnt, 2))
      print("Number of students taught is: ", totStu)
      print("Longest favorite word is: ", lrg)
      print("Smallest favorite word is: ", sm)

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()