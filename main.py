from tkinter import *
import PyPDF2
from tkinter import filedialog

class PDF_Extractor_Text:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Text Extractor | Developed by Sikandar Singh")
        self.root.geometry("600x500+260+10")
        self.root.configure(bg = "white")
        self.root.resizable(0, 0)
        
        self.head_label = Label(self.root, text = "No file selected", font = ("Bookman Old Styles", 15, "bold"), bd = 0, bg = "white")
        self.head_label.pack(fill = X, padx = 5, pady = 5)
        
        self.main_frame = LabelFrame(self.root, bg = "white", bd = 0, relief = GROOVE)
        self.main_frame.pack(fill = BOTH, expand = 1, padx = 10, pady = 10)
        
        self.yscroll = Scrollbar(self.main_frame, orient = VERTICAL)

        self.text_fd = Text(self.main_frame, wrap = WORD, yscrollcommand = self.yscroll.set, font = ("Bookman Old Styles", 10))
        self.yscroll.pack(side = RIGHT, fill = Y)
        self.yscroll.config(command = self.text_fd.yview)
        self.text_fd.pack(fill = BOTH, expand = 1)
            
        Button(self.root, text = "Open PDF File", command = self.OpenPdfFile, cursor = "hand2", font = ("Bookman Old Styles", 15, "bold")).pack(fill = X, padx = 5, pady = 5)
        
    def OpenPdfFile(self):
        filename = filedialog.askopenfilename(title = "Open PDF File", initialdir = "D:\Sikandar Singh\Python Programming\PDF Text Extractor", filetypes = [("PDF Files", "*.pdf")])

        reader = PyPDF2.PdfReader(filename)

        self.head_label.configure(text = filename)
        self.text_fd.delete("1.0", END)
        for i in range(len(reader.pages)):
            self.current_text = reader.pages[i].extract_text()
            self.text_fd.insert(END, self.current_text)

if __name__ == "__main__":
    root = Tk()
    obj = PDF_Extractor_Text(root)
    root.mainloop()