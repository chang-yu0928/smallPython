from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import PSDraw
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open('google-logo.jpg', 'r')


# xsize, ysize = im.size
# delta = xsize/3
# im2 = Image.new('RGB', (xsize, ysize))
#
# part1 = im.crop((0, 0, delta, ysize))
# part2 = im.crop((delta, 0, xsize, ysize))
#
# im2.paste(part1, (xsize-delta, 0, xsize, ysize))
# im2.paste(part2, (0, 0, xsize-delta, ysize))
#
# im2.show()

# r, g, b = im.split()
# im = Image.merge("RGB", (b, g, r))
#
# im.show()

# im.rotate(45).show()
# im.resize((125, 125)).show()

# im.transpose(Image.FLIP_LEFT_RIGHT).show()
# im.transpose(Image.FLIP_TOP_BOTTOM).show()
# im.transpose(Image.ROTATE_90).show()

# im.filter(ImageFilter.DETAIL).show()

# im.point(lambda i: i * 1.2).show()

# source = im.split()
#
# R, G, B = 0, 1, 2
# mask = source[R].point(lambda i: i < 100 and 255)
# out = source[G].point(lambda i: i * 0.7)
# source[G].paste(out, None, mask)
# Image.merge(im.mode, source).show()

# enh = ImageEnhance.Contrast(im)
# enh.enhance(1.3).show("30% more contrast")

# title = "4"
# box = (1*72, 2*72, 7*72, 10*72)
#
# ps = PSDraw.PSDraw()
# ps.begin_document(title)
#
# ps.image(box, im, 75)
# ps.rectangle(box)
#
# ps.setfont("HelveticaNarrow-Bold", 36)
# ps.text((3*72, 4*72), title)
#
# ps.end_document()

xSize, ySize = im.size
num = Image.new('RGBA', (100, 200), (255, 255, 255, 0))
draw = ImageDraw.Draw(num)

fontsize = 1
font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize("4")[0] < num.size[0]:
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)

fontsize -= 1
font = ImageFont.truetype("arial.ttf", fontsize)

draw.text((0, 0), '4', font=font, fill=(0, 0, 0))
im.paste(num, (((xSize/4) * 3), 0), num)
im.show()




