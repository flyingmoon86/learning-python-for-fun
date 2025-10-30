from PIL import Image, ImageFilter
before = Image.open("test.jpg")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.jpg")
after.show()