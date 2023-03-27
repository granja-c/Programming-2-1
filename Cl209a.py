class Counting:
  def __init__(self, m, l, cnt):
    self.more = m
    self.less = l
    self.cnt = cnt
  def __str__(self):
    return f"The number of numbers less than 500 is {self.less}\nThe number of numbers greater than or equal to 500 is {self.more}\nThe total number of numbers is {self.cnt}"