from display import *

def draw_line(x0, y0, x1, y1, screen, color ):
  a,b,m = findABM(x0, y0, x1, y1)
  d = 2 * a + b
  x = x0
  y = y0
  while x <= x1:
    plot(screen, color, x, y)
    if d > 0:
      y += 1
      d += 2 * b
    x += 1
    d += 2 * a
    
def findABM(x0, y0, x1, y1):
  a = y1 - y0
  b = -1 * (x1 - x0)
  m = -1.0 * a / b
  return a,b,m
