import maskpass as mask
import instagrapi
from instagrapi import Client

def make_post(photo_path):
	global location
	cl.album_upload(
		photo_path,
		caption = main_caption + "\n\n Location: #" + location + "\n Camera: #SonyA6300\n\n @sonyalpha @magnumphotos\n\n" + tags + "Authentic Streets", ## this will use the custom made NN app to generate unique captions
		location = Location() ######## ADD
		)

cl = Client()
USERNAME = input("USERNAME: ")
PASSWORD = mask.askpass(prompt ="PASSWORD: ", mask = "*")
verification_code = input("2FA CODE: ")
print("Logging in...")
cl.login(USERNAME, PASSWORD, verification_code=verification_code)
print("Access Completed.")

main_caption = input("What is the main caption? ")
location = input("What is the location? ")

tags = """#streets_storytelling #portrait #portraitphotography #streetclassics #sonyalpha #alphapro
#adobecreativecrowd #BeAlpha #streetgrammers
#lightroompresets #streetsvision
#cinegrams #photocinematica
#cinesomnia #streetphotographers
#StreetDreamsMag
#3amchronicles #spicollective
#creativephotography #streetpeople
#filmic_streets\n"""

# with open('hashtags.txt', 'r') as file:
#     hashtags = file.readlines()

# # Clean up the hashtags (remove newline characters)
# hashtags = [tag.strip() for tag in hashtags]

multiple = input("Are you attaching multiple photos? [Y/N] : ")
path_list = []
if multiple == "Y":
	in_loop = True
	counter = 1
	while in_loop == True:
		print("Photo number - " + str(counter))
		path = input("Path to photo: ")
		path_list.append(str(path))
		if input("Attach more photos? [Y/N] :") == "Y":
			counter += 1
			in_loop = True
			print("Photo added.")
		else:
			in_loop = False
			print("No more photos.")
else:
	path = input("Path to photo: ")
	path_list.append(str(path))

print("Posting Photo...")

print(path_list)
make_post(path_list)

print("Photo Posted.")

print("Logging out...")
cl.login()
print("Ending Program.")