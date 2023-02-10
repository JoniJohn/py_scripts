import gofile as go

def store_files(file):
	cur_server = go.getServer()
	print(cur_server)
	url = go.uploadFile(file)
	print("download link: ", url["downloadPage"])

store_files("test.file")
