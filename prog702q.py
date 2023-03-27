from Cl701g import *

def main():
  try:
    veh = []
    with open("data/prog701g.dat", 'r') as f:
      for line in f:
        num = int(f.readline())
        if num == 1:
          n = f.readline()
          t = int(f.readline())
          c = int(f.readline())
          c = Car(n, t, val)
          veh.append(c)
        elif num == 2:
          n = f.readline()
          t = int(f.readline())
          mile = float(f.readline())
          v = Truck(n, t, mile)
          veh.append(v)
        elif num == 3:
          n = f.readline()
          t = int(f.readline())
          home = f.readline()
          bus = Car(n, t, home)
          veh.append(b)
        num = int(f.readline())
      num = 0
      totC = 0
      totV = 0
      lrg = ""
      lst = ""
      mst = 4893023482074927502843040298409720359701830
      tireC = 0
      tireT = 0
      tireB = 0

      for v in veh:
        if isinstance(v, Car):
          totC += v.val
          totV += v.val
          tireC += v.tires
        if isinstance(v, Truck):
          totV += v.val
          tireT += v.tires
          if v.val < mst:
            lst = v.name
            mst = v.val

        if isinstance(v, Bus):
          totV += 50000
          tireB += v.tire
          if len(v.home) > len(lrg):
            lrg = v.home
        num += 1
          
      print("Total number of vehicles: ", num)
      print("Total value of cars: ")
      print("Truck with the lowest value: ")
      print("Longest home destination name: ")
      print("Longest home destination name: ")

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()