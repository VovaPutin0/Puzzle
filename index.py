from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from moviepy.editor import *
from pydub import AudioSegment

app = Tk()
app.title('Puzzle')
app.resizable(width=False, height=False)
app.geometry('500x650')

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="Редактор видео")
notebook.add(frame2, text="Редактор аудио")


def audioClipping():
    filepath = filedialog.askopenfilename()
    examination = Path(filepath).suffix
    if examination == '.mp4':
        video = (VideoFileClip(filepath))
        audio = video.audio
        audio.write_audiofile('Ready.mp3')
        true = Label(app, text='Операция успешно завершена! Файл сохранен : Ready.mp3', pady=40)
        true.pack()
    elif filepath == '':
        false = Label(app, text='Операция прервана. Не выбран фаил', pady=40)
        false.pack()
    else:
        error = Label(app, text='Выберите формат файла .mp4', pady=40)
        error.pack()


def videoEditor():
    filepath = filedialog.askopenfilename()
    examination = Path(filepath).suffix
    if examination == '.mp4':
        video = (VideoFileClip(filepath))
        final = video.fx(vfx.speedx, 2)
        final.write_videofile('speed_x2.mp4')
        true = Label(app, text='Операция успешно завершена! Файл сохранен : speed_x2.mp4', pady=40)
        true.pack()
    elif filepath == '':
        false = Label(app, text='Операция прервана. Не выбран фаил', pady=40)
        false.pack()
    else:
        error = Label(app, text='Выберите формат файла .mp4', pady=40)
        error.pack()

def makeGif():
    filepath = filedialog.askopenfilename()
    examination = Path(filepath).suffix
    if examination == '.mp4':
        video = (VideoFileClip(filepath))
        video.write_gif('gif.gif')
        true = Label(app, text='Операция успешно завершена! Файл сохранен : gif.gif', pady=40)
        true.pack()
    elif filepath == '':
        false = Label(app, text='Операция прервана. Не выбран фаил', pady=40)
        false.pack()
    else:
        error = Label(app, text='Выберите формат файла .mp4', pady=40)
        error.pack()

button = Button(frame1, text='вырезать аудио', font='Tahoma 25', command=audioClipping)
button.pack(side=BOTTOM, pady=40)
button = Button(frame1, text='Ускорить видео в 2Х', font='Tahoma 25', command=videoEditor)
button.pack(side=BOTTOM, pady=40)
button = Button(frame1, text='Сделать Гифку из видео', font='Tahoma 25', command=makeGif)
button.pack(side=BOTTOM, pady=40)


########################################################################################################################

def songTwo():
    filepath = filedialog.askopenfilename()
    examination = Path(filepath).suffix
    if examination == '.mp3':
        audio = AudioSegment.from_file(filepath, format="mp3")
        audio.export("wav.wav", format="wav")
        true = Label(app, text='Операция успешно завершена! Файл сохранен : wav.wav', pady=40)
        true.pack()
    elif filepath == '':
        false = Label(app, text='Операция прервана. Не выбран фаил', pady=40)
        false.pack()
    else:
        error = Label(app, text='Выберите формат файла .mp3', pady=40)
        error.pack()

def upSound():
    filepath = filedialog.askopenfilename()
    examination = Path(filepath).suffix
    if examination == '.mp3':
        audio = AudioSegment.from_file(filepath)
        audioUp = audio + 10
        audioUp.export("upSound.mp3", format="mp3")
        true = Label(app, text='Операция успешно завершена! Файл сохранен : UpSound.mp3', pady=40)
        true.pack()
    elif filepath == '':
        false = Label(app, text='Операция прервана. Не выбран фаил', pady=40)
        false.pack()
    else:
        error = Label(app, text='Выберите формат файла .mp3', pady=40)
        error.pack()

def downSound():
    filepath = filedialog.askopenfilename()
    examination = Path(filepath).suffix
    if examination == '.mp3':
        audio = AudioSegment.from_file(filepath)
        audioDown = audio - 10
        audioDown.export("downSound.mp3", format="mp3")
        true = Label(app, text='Операция успешно завершена! Файл сохранен : downSound.mp3', pady=40)
        true.pack()
    elif filepath == '':
        false = Label(app, text='Операция прервана. Не выбран фаил', pady=40)
        false.pack()
    else:
        error = Label(app, text='Выберите формат файла .mp3', pady=40)
        error.pack()


button = Button(frame2, text='Уменьшение громкости', font='Tahoma 28', command=downSound)
button.pack(side=BOTTOM, pady=40)
button = Button(frame2, text='Увелечение громкости', font='Tahoma 28', command=upSound)
button.pack(side=BOTTOM, pady=40)
button = Button(frame2, text='Переформатировать файл из MP3 в WAV', font='Tahoma 19', command=songTwo)
button.pack(side=BOTTOM, pady=40)

app.mainloop()
