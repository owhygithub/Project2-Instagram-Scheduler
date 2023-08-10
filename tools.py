import maskpass as mask
import instagrapi
from instagrapi import Client

cl = Client()
def make_post(photo_path):
	global location
	cl.album_upload(
		photo_path,
		caption = main_caption + "\n\n Location: #" + location + "\n Camera: #SonyA6300\n\n @sonyalpha @magnumphotos\n\n" + tags + "Authentic Streets", ## this will use the custom made NN app to generate unique captions
		location = Location() ######## ADD
		)