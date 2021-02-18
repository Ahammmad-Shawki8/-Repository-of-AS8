# image manipulation with pillow.

# in this series we will look at the pillow library for python.
# pillow allows us to work with and manipulate images using python.
# we will learn several things about images like
    # displaying them in the screen
    # resizing them
    # modifying their colors 
    # and also saving them to our local machine
# this is extreamly useful when we want to modify multiple images at once or
# we want to automatically run a script on images that we upload on certain directory.

# first we want to install pillow
"""pip install pillow"""

# import pillow
from PIL import Image
# note that we have to use PIL not pillow.
# thats a naming convention.

# display image in the screen.
# we will nedd to create an Image object and use the open() method.
img1=Image.open("F:\Python\\1. Python Basics\pic\\winter.jpg")
# here we have to pass the path.
# to show the object, we need to use show() method.
img1.show()
# now we can see that image in the screen.
# lets do a simple modification to it.
# what if we want to save that photo as a png file instead of jpg file.
# we can use the save method.
img1.save("F:\Python\\1. Python Basics\pic\\winter_new.png")
# now we can see that we have a new winter_new.png file in our directory.

# what if we want to convert all of the images into tiff file.
# first we need a way to loop over all of the images of our pic directoty.
# now to do that we need to import the os module.
import os

for f in os.listdir("F:\Python\\1. Python Basics\pic"):# executing dir method in certain directory.
    if f.endswith(".png") or f.endswith(".jpg"):
        print(f)
        i=Image.open("F:\Python\\1. Python Basics\pic\\"+str(f))
        fname,fext=os.path.splitext(f)
        print(fname)
        print(fext)
        # save them in tiffs folder.
        i.save("F:\Python\\1. Python Basics\pic\\tiffs\\"+str(fname)+".tiff")

# lets resize each file
# this would be extreamly useful on web server or something like that.
# we may need the resized photos for thumdnails and image galaries.
# we need to maintain the same aspect ratio.
# first lets decide, what maximum size we want our files to be.
size_300=(300,300)# here 300 is the pixels.
size_window=(1366,768)
# image size needs to be a tuple.

for f in os.listdir("F:\Python\\1. Python Basics\pic"):
    if f.endswith(".png") or f.endswith(".jpg"):
        i=Image.open("F:\Python\\1. Python Basics\pic\\"+str(f))
        fname,fext=os.path.splitext(f)
        # thumdnail() function is used for changing the size.
        i.thumbnail(size_300)
        i.save("F:\Python\\1. Python Basics\pic\\resized\\{}_300{}".format(fname,fext))
        i.thumbnail(size_window)
        i.save("F:\Python\\1. Python Basics\pic\\resized\\{}_window{}".format(fname,fext))
# now we can see that these are the small 300 pixels version of our old images.
# the great thing is that we can quickly change the pixels value in python.

# lets just see few more things what we can do with pillow library.
# we can rotate images.
# we can make the images black-white.
# we can blur images and we can do all kind of things.

# lets see them.
# rotate an image.
img2=img1.rotate(90)
img2.show()
# here we have to pass the degrees that we want to rotate.

# now lets say we want to make this image black&white.
# we can do that by convert() method.
img3=img1.convert(mode="L")
# here we have to pass an argument mode and set that equal to "L"
img3.show()
# sometimes we forget about these methods and mode.
# but we can always see them in the documentation.
# and when we start working with this libraries, it is really not physible to memorize all these things in our head.
# because, these are the libraies that we may need to work not very often.
# so, we really have to be comfortable with the documentation.
# the documentation url is-
"""https://pillow.readthedocs.io/en/stable/"""

# blur image
# we have to import ImageFilter
from PIL import ImageFilter
img4=img1.filter(ImageFilter.GaussianBlur())
# here we need to use the filter() method and within that we need to execute the ImageFilter.GaussianBlur() method.
img4.show()
# we can see that this doesn't change much and that is because we are using default values from GaussianBlur() method.
# with the default value its radius is set to 2.
# we can change the default radius by passing the new radius number in the GaussianBlur() method.
img5=img1.filter(ImageFilter.GaussianBlur(15))
img5.show()
# now we can see that this blur is much more than the previous one.