import speech_recognition as sr
import tkinter
import tkinter.filedialog
root = tkinter.Tk()
def openfile():
    global f
    f = tkinter.filedialog.askopenfilename(
        parent=root, 
        title='Choose file',
        filetypes=[('Audio Files', '*.wav'),
                   ("All Files", "*.*")]
        )
    


def speechtotext(AUDIO_FILE):
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
    try:
        t.insert(tkinter.END,text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;{0}".format(e))

l1=tkinter.Label(root,text='Input audio')
l1.grid(row=0,column=0)
b1 = tkinter.Button(root, text='Upload', command=openfile)
b1.grid(row=0,column=1)
b2 = tkinter.Button(root, text='output', command=lambda:speechtotext(f))
b2.grid(row=1,column=1)
l2=tkinter.Label(root,text='Output text')
l2.grid(row=1,column=0)
t=tkinter.Text(root)
t.grid(row=3,column=0,columnspan=2,pady=10)
root.mainloop()
