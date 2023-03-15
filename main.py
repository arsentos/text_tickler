from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import ImageFont


def text_tickle(text,
                background_color=(255, 255, 255),
                text_color="white",
                width=100, height=100,
                filename="text.mp4",
                duration=3.0):
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 30)
    size = font.getlength(text)
    print(size)

    def position(t):
        return (width / 2 + (-(size / duration) * t), "center")

    add_text = TextClip(text, fontsize=30, color=text_color, font="Arial").set_position(position).set_duration(3.0)

    final = CompositeVideoClip([add_text], size=(width, height), bg_color=background_color)
    final.duration = duration
    final.fps = 60
    final.write_videofile(filename)


for i in TextClip.list('color'):
    print(i)
text_tickle("Size of the picture in pixels. Can be auto-set if method=’label’, but mandatory if method=’caption’. the height can be None, it will then be auto-determined.",
            filename="new.mp4",
            text_color="VioletRed3",
            background_color=(175, 25, 75),
            )
