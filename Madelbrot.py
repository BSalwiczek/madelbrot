from plot import plot

MAX_ITERATIONS = 80


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITERATIONS:
        z = z * z + c
        n += 1
    return n


zoom = 0.99994

RE_START = -1.4005 + (zoom/2)*1.6
RE_END = 0.1995 - (zoom/2)*1.6
IM_START = 0 + (zoom/2)*0.9
IM_END = 0.9 - (zoom/2)*0.9
plot(mandelbrot, 'madelbrot12.png', RE_START, RE_END, IM_START, IM_END, MAX_ITERATIONS)
