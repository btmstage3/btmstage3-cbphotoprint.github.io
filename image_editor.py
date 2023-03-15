from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditor:

    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.image = None
        self.filename = None

    def open_image(self):
        self.filename = filedialog.askopenfilename(title="Select an Image File",
                                                   filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.filename:
            self.image = Image.open(self.filename)
            self.image.thumbnail((600, 600))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='red', width=2)

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        pass

    def crop_image(self):
        if self.rect:
            x1 = self.canvas.coords(self.rect)[0]
            y1 = self.canvas.coords(self.rect)[1]
            x2 = self.canvas.coords(self.rect)[2]
            y2 = self.canvas.coords(self.rect)[3]
            x1 = max(0, int(x1))
            y1 = max(0, int(y1))
            x2 = min(int(x2), self.image.size[0])
            y2 = min(int(y2), self.image.size[1])
            if x2 > x1 and y2 > y1:
                crop_width = int(input("Enter crop width (in pixels): "))
                crop_height = int(input("Enter crop height (in pixels): "))
                cropped_image = self.image.crop((x1, y1, x1 + crop_width, y1 + crop_height))
                save_filename = filedialog.asksaveasfilename(title="Save Cropped Image As",
                                                             defaultextension=".jpg",
                                                             filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")])
                if save_filename:
                    cropped_image.save(save_filename)

    def quit(self):
        self.root.quit()

if __name__ == '__main__':
    root = Tk()
    root.title("Image Editor")
    root.geometry("600x600")
    image_editor = ImageEditor(root)
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open", command=image_editor.open_image)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=image_editor.quit)
    editmenu = Menu(menu)
    menu.add_cascade(label="")
