# import googletrans
# from tkinter import *
# from tkinter import  ttk
#
# # print(kys.values())
# root = Tk()
# root.title("Languages")
# lang= ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque',
#                       'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa',
#                       'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish',
#                       'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian',
#                       'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian',
#                       'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish',
#                       'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)',
#                       'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy',
#                       'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali',
#                       'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian',
#                       'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak',
#                       'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu',
#                       'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa',
#                       'yiddish', 'yoruba', 'zulu']
# root.geometry("300x300")
# options = StringVar(root)
# options.set("Choose")
# dropdown = OptionMenu(root, options,*lang ).pack(pady=50)
# def show():
#     result=options.get()
#     return result
#
# buttons= Button(root,command=show,text='show').pack(pady=100)
# root.mainloop()
# res= show()

# class Phone:
#     def make_call(self):
#         print("I am playing a call")
#
#     def set_color(self,color):
#         self.color=color
#
#
#     def show_color(self):
#         return self.color
#
#
#
# p1= Phone()
# p1.make_call()
# p1.set_color("blue")
# p1.show_color()

def set_color(self,color):
    self.color=color


def show_color(self):
        return self.color

show_color(set_color("","blue")