from PIL import Image, ImageDraw
import math

size = (71*10, 40*10)

output = Image.new('RGB', size, (240,240,255))
drawTo = ImageDraw.Draw(output)

"""
first normalize, then multiply out

(0, 0)     (71, 0)
     +-----+
		 |		 |
		 |		 |
		 +-----+
(0, 40)     (71, 40)
"""

def cut(num, cutNum):
	return (num / 10**cutNum)
	return round(num / 10**cutNum)

def proc(X, Y):
	# section A
	u = X - 36
	v = 18 - Y
	h = u**2 + v**2
	if h < 200:
		r, b = sectionB(X, Y, u, v, h)
	elif v < 0:
		r, b = sectionC(X, Y, u, v, h)
	else:
		r, b = sectionD(X, Y)
	# section E
	r = min(r, 255)
	b = min(b, 255)
	return (round(r), 0, round(b))
	g = cut(7*r + 3*b, 1)
	return (round(r), round(g), round(b))
		
def sectionB(X, Y, U, V, H):
	r = 420
	b = 520
	t = 5000 + 8*H
	p = cut(t*U, 2)
	q = cut(t*V, 2)
	s = 2*q
	w = cut(1000 + p - s, 2) + 8
	if w > 0:
		r += w**2
	o = s + 2200
	r = cut(r*o, 4)
	b = cut(b*o, 4)
	if p > -q:
		w = cut(p + q, 1)
		r += w
		b += w
	return(r, b)

def sectionC(X, Y, U, V, H):
	r = 150 + 2*V
	b = 50
	p = H + 8*V**2
	c = (240*-V) - p
	if c > 1200:
		o = cut(6*c, 1)
		o = c * (1500 - o)
		o = cut(o, 2) - 8360
		r = cut(r*o, 3)
		b = cut(b*o, 3)
	rt = c + U*V
	d = 3200 - H - 2*rt
	if d > 0:
		r += d
	return r, b

def sectionD(X, Y):
	c = X + 4*Y
	r = 132 + c
	b = 192 + c
	return r, b


expectedWidth = size[1] * 71/40
extraWidth = False

if size[0] > expectedWidth:
	normalSize = (expectedWidth, size[1])
	extraWidth = True
else:
	normalSize = (size[0], size[0] * 40/71)

"""         NOTE: "1" means "71" because lol

width = 3
expectedWidth = 1

ratio = width / expectedWidth

                          -1       0       1       2       3
                           |       |   |   |       |       |
answer                     -------------------------
  x                                ---------
x * ratio                          -------------------------


"""

for y in range(size[1]):
	for x in range(size[0]):
		xc = (x / size[0]) * 71
		yc = (y / size[1]) * 40
		drawTo.point((x, y), fill = proc(xc, yc))



output.save("better_shader.png")