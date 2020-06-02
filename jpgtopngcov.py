from PIL import Image
# open the image that u want to convert and type in its adress like where it is saved
image1 = Image.open('./images/mouse.jpg')
# for 2nd image that u want to convert
image2 = Image.open('./images/pokemon.jpg')
# save the image(where u want to save->images) and specify its name -> mouse.png
image1.save('./images/mouse.png')
image2.save('./images/pokemon.png ')
