from PIL import Image, ImageDraw
import math

size = (71, 40)
output = Image.new('RGB', size, (240,240,255))
drawTo = ImageDraw.Draw(output)

def cut(num, cutNum):
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
	g = cut(7*r + 3*b, 1)
	return (r, g, b)
		
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

for y in range(size[1]):
	for x in range(size[0]):
		drawTo.point((x, y), fill = proc(x, y))



output.save("shader.png")