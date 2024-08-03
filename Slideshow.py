from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image-SlideShow-App")

# file path of Images
Iamge_paths = [
    r"D:\Projects\Image-Slideshow-App\pic\astronaut-explorer-wanderer-planets-cosmos-surreal-3840x4800-6771.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\autumn-forest-5120x3800-15540.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\biker-helmet-neon-5120x2880-15476.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\demon-slayer-3840x5270-10716.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\denji-artwork-5120x3657-13802.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\denji-chainsaw-man-manga-series-3840x2743-8869.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\dreamlike-whale-3840x2160-14385.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\dva-cute-art-school-3840x2160-11864.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\exploring-saturn-planet-surreal-time-travel-space-3000x2400-1052.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\giyu-tomioka-demon-3840x2160-16085.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\goku-amoled-super-10000x5736-12116.png",
    r"D:\Projects\Image-Slideshow-App\pic\goku-black-super-5120x2880-13399.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\goku-dragon-ball-amoled-retro-artwork-neon-black-background-5120x2880-5059.png",
    r"D:\Projects\Image-Slideshow-App\pic\goku-super-saiyan-4-fusion-ssj4-fusion-amoled-black-5120x2880-5048.png",
    r"D:\Projects\Image-Slideshow-App\pic\goku-super-saiyan-4096x4096-14709.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\goku-vegeta-dragon-5120x2880-15843.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\ichigo-kurosaki-bleach-3840x3840-10512.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\jujutsu-kaisen-5120x3657-15334.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\jujutsu-kaisen-yuji-7680x5486-9287.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\kento-nanami-5k-5120x2880-13897.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\kyojuro-rengoku-5k-5120x2880-13969.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\kyojuro-rengoku-5120x7168-12130.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\maserati-mc20-cielo-10000x7117-16110.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\monkey-d-luffy-3840x2160-13282.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\monkey-d-luffy-3997x2829-10535.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\moon-falling-couple-silhouette-surreal-3840x2560-1080.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\mystic-surreal-dream-tree-planets-digital-art-man-alone-3600x4500-8367.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\nezuko-kamado-5120x2880-14025.png",
    r"D:\Projects\Image-Slideshow-App\pic\nezuko-kamado-5400x4050-9321.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\nezuko-kamado-demon-7629x5603-9331.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\one-punch-man-fubuki-garou-garou-king-saitama-sonic-3840x2304-7580.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-ahmed-adly-1270184.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-baskin-creative-studios-1766838.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-eberhard-grossgasteiger-443446.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-eberhard-grossgasteiger-1421903.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-eberhard-grossgasteiger-1612351.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-irina-iriser-1366957.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-irina-iriser-1379636.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-james-wheeler-1519088.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-phil-kallahar-983200.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-phil-kallahar-983200.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-pixabay-36717.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-pixabay-326055.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-rafael-guajardo-604684.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-sebastiaan-stam-1097456.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-stein-egil-liland-1933239.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-todd-trapani-1535162.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-toni-cuenca-585752.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\pexels-vlad-alexandru-popa-1402787.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\roronoa-zoro-katana-4096x2884-10544.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\roronoa-zoro-one-piece-4000x3624-10525.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\saitama-8k-one-7680x4320-10093.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\saitama-one-punch-man-5k-5680x3104-11350.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\shinobu-kocho-demon-slayer-kimetsu-no-yaiba-5k-anime-girl-6400x4320-7914.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\shinobu-kocho-demon-slayer-kimetsu-no-yaiba-3840x2160-7909.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\skull-island-seascape-tropical-caribbean-surreal-blue-5k-6000x4000-5456.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\tanjiro-kamado-4416x3533-9322.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\tanjiro-kamado-4052x3243-9324.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\tanjiro-kamado-cute-anime-3840x2160-12045.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\wlop-beautiful-5120x5120-15981.jpg",
    r"D:\Projects\Image-Slideshow-App\pic\wooden-house-3840x2160-14956.jpg"
]

#Resize the image for no space in background
Image_size=(1080,1080)

#accessig Images through loop and resize according to image_size provideds
images = [Image.open(path). resize(Image_size) for path in Iamge_paths]

photo_Images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

#function to display images in label and update imge according to time method
def update_Image():
    for photo_image in photo_Images:
        label.config(image=photo_image)
        label.update()
        time.sleep(5)

slideshow = cycle(photo_Images)

#function to iterate Image in slideshow till all images are covered
def start_slideshow():
    for _ in range(len(Iamge_paths)):
        update_Image()

Play_button = tk.Button(root, text="Start SlideShow", command=start_slideshow)
Play_button.pack()

root.mainloop()