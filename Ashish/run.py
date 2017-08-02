import requests
import shutil
from subprocess import call
call(["python2","interp1.py"])

#call(["./biocharnorahserver.sh", "5000"]) #this should be done manually before starting
params = {'action':'render'}
files = {'design': open("input.json", 'rb'), 'render': open("render.json", "rb")}
rinput = requests.post("http://localhost:7000/render", files=files, data=params, stream=True)
with open("input.png", "wb") as f:
	rinput.raw.decode_content = True
	shutil.copyfileobj(rinput.raw, f)

params['skipreset'] = 'on'

for i in range(0,6):
	designjson = "data"+str(i)+".json"
	outpng = "out"+str(i)+".png"
	outfbx = "out"+str(i)
	files = {'design': open(designjson, 'rb'), 'render': open("render.json", "rb")}
	response = requests.post("http://localhost:7000/render", files=files, data=params, stream=True)
	with open(outpng, "wb") as f:
		response.raw.decode_content = True
		shutil.copyfileobj(response.raw, f)

files = {'design': open("output.json", 'rb'), 'render': open("render.json", "rb")}
rinput = requests.post("http://localhost:7000/render", files=files, data=params, stream=True)
with open("output.png", "wb") as f:
	rinput.raw.decode_content = True
	shutil.copyfileobj(rinput.raw, f)

