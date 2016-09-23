import os

def mkdir(path):
	path = path.strip()
	path = path.rstrip("\\")
	isExists=os.path.exists(path)
	if not isExists:
		print(path+'make dir successfully') 
		os.makedirs(path)
		return True
	else:
		print(path+'dir already exists') 
		return False

mkdir("d:\\LearnPython\\webapp\\backup")