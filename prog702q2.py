from Cl702q import *

def main():
  try:
    veh = []
    with open("data/prog702q.dat", 'r') as f:
      a = f.readlines()
      cnt = 0
      while cnt <= len(a):
        num = f.readline()
        n = f.readline()
        t = int(f.readline())
        if num == 1:
          #n = f.readline()
          #t = f.readline()
          val = f.readline()
          v = Car(n, t, val)
          veh.append(v)
        elif num == 2:
          #n = f.readline()
          #t = f.readline()
          miles = int(f.readline())
          v = Truck(n, t, miles)
          veh.append(v)
        elif num == 3:
          #n = f.readline().strip()
          #t = int(f.readline())
          home = f.readline().strip()
          v = Bus(n, t, home)
          veh.append(v)
        cnt += 1

      cnt = 0
      carV = 0
      totV = 0
      tireC = 0
      tireT = 0
      tireB = 0
      lrg = ""
      least = ""
      mst = 98204003824082038402
      for v in veh:
        if isinstance(v, Car):
          carV += v.val
          totV += v.val 
          tireC += v.tires
          cnt += 1
        if isinstance(v, Truck):
          val = v.val
          name = v.name
          totV += v.val
          tireT += v.tires
          if val < mst:
            least = name
            mst = val
          cnt += 1
        if isinstance(v, Bus):
          home = v.home
          totV += v.val
          tireB += v.tires
          if len(home) > len(lrg):
            lrg = home
          cnt += 1
        #print("Total number of vehicles: ", cnt)
        #print("Total value of cars: ", carV)
        #print("Truck with the lowest value: ", least)
        #print("Longest home destination name: ", lrg)
        print("hi")

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()