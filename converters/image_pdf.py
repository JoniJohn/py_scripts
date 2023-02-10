from PIL import Image

def Image_Pdf(filename, output):
	images = []
	for file in filename:
		im = Image.open(file)
		im = im.convert('RGB')
		images.append(im)

		images[0].save(output, save_all=True, append_images=images[1:])


Image_Pdf(['image_path_1.png', 'image_path_2.png'], "output.pdf")
