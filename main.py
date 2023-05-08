

from rembg import remove

# import pytube
#
# url = input("enter video url: ")
#
# path = ""
#
# pytube.YouTube(url).streams.get_highest_resolution().download(path)

input_path = "sincap.jpg"
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
       input_file = i.read()
       output_file = remove(input_file)
       o.write(output_file)
