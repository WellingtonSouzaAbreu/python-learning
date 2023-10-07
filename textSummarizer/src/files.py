def readFile(name):
    try:
        file = open(name, 'rt') 
        return file.read()
    except: 
        print('File not found...')

def writeFile(name, content):
    try:
        file = open(name, 'wt')
        file.write(content)
        file.close()
        return True
    except: 
        print('Error on write file...')
