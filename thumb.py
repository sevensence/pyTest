import Image
im = Image.open('91e0ea902a75dd4060807e810699e044.jpg')
print im.format,im.size,im.mode 

im.thumbnail((800,600))
im.save('thumb.jpg','JPEG')
