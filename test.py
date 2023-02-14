import base64

with open("test.jpg", "rb") as image_file:
    image_data = image_file.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")

print(image_base64)
