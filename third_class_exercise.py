from PIL import Image, ImageDraw

# 1

#   a = 1 / 0;

# 2
import os

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Error division by zero!")

# 3  Yes

try:
    x = 1
finally:
    print("finally")

# 4  Any exception


# 5

# It's too general and will catch any exception you can't
# give specific treatment or know which exception was thrown

# 6
'''

IOError and ZeroDivisionError 

the following handlers can handle IO File errors
e.g: when file not exist , of file location is wrong

and also Handle match operation error when you try to make division by zero


'''

# 7

if not os.path.exists("word.txt"):
    f = open("word.txt", 'w')
    f.close()

# 8
with open("word.txt", mode="w") as file:
    file.write("ron bar yosef")

# 9
with open("word.txt", mode="r") as file:
    for line in file:
        print(line)

# 10

hebrew_message = "פייתון אחלה שפה שבעולם"
with open("word.txt", 'w', encoding='utf-8') as file:
    file.write(hebrew_message)

with open("word.txt", 'r', encoding='utf-8') as file:
    file_content = file.read()
    print("File Content:")
    print(file_content)


# 11
def create_image():
    width, height = 300, 200

    image = Image.new("RGB", (width, height), "white")

    draw = ImageDraw.Draw(image)

    rectangle_color = (0, 0, 255)  # RGB color for blue
    rectangle_coordinates = (50, 50, 250, 150)  # (left, top, right, bottom)
    draw.rectangle(rectangle_coordinates, fill=rectangle_color)

    # Draw a red circle
    circle_color = (255, 0, 0)  # RGB color for red
    circle_center = (width // 2, height // 2)  # Center of the image
    circle_radius = 40
    draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                  circle_center[0] + circle_radius, circle_center[1] + circle_radius],
                 fill=circle_color)

    # Save the image as a PNG file
    image.save("my_image.png")

    print("my_image.png was created")


create_image()
