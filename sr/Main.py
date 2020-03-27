import os
from multiprocessing import Pool



a = os.getcwd()
os.mkdir(a + "/Scripts/")
scriptPath = a + "/Scripts/"
path = os.listdir(a)
chunks = []

counter = 0
for file in path:
    if file.endswith('.wav'):
        chunks.append(file)
        counter += 1


for i in range(0, counter):
    with open(a + "/Scripts/" + str(i) + ".py", "w") as scriptFile:
        string = "import speech_recognition as sr\n\nr = sr.Recognizer()\nsound = sr.AudioFile(" + "'" +chunks[i] + "'" + ")\n\nwith sound as source:\n    audio = r.record(source)\n\nprint(r.recognize_google(audio))"

        scriptFile.write(string)
        scriptFile.close()

pathToScripts = os.listdir(scriptPath)
scriptList = []
for file in pathToScripts:
    a = str(file)
    scriptList.append(a)

processes = tuple(scriptList)



def run_process(process):
    os.system('python3 ' + scriptPath + '{}'.format(process))

pool = Pool(processes=counter)
pool.map(run_process, processes)



