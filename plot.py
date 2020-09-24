from PIL import Image, ImageDraw
def plot(fun, filename, real_start, real_end, im_start, im_end, max_iter):
    WIDTH = 1280
    HEIGHT = 720
    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(real_start + (x / WIDTH) * (real_end - real_start),
                        im_start + (y / HEIGHT) * (im_end - im_start))
            # Compute the number of iterations
            m = fun(c)
            # The color depends on the number of iterations
            color_R = 255 - int(m * 255 / max_iter)
            color_G = 255 - int(m * 255 / max_iter)
            color_B = 255 - int(m * 255 / max_iter)
            # Plot the point
            if m == max_iter:
                draw.point([x, y], (0,0,0))
            else:
                draw.point([x, y], (color_R, color_G, color_B))

    im.save(filename, 'PNG')