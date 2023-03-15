from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import ImageFont


def text_tickle(text, background_color="black", text_color="white", width=100, height=100, velocity=100):
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 30)
    size = font.getlength(text)
    print(size)

    def position(t):
        a = (width) + (-100 * t)
        return (a, "center")

    add_text = TextClip(text, fontsize=30, color=text_color, font="Arial").set_position(position).set_duration(3.0)

    final = CompositeVideoClip([add_text])
    final.duration = 3.0
    final.fps = 60
    final.write_videofile("text.mp4")


text_tickle("абобус")
