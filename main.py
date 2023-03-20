from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import ImageFont


def text_tickle(text,
                background_color=(255, 255, 255),
                text_color="white",
                width=100, height=100,
                filename="text.mp4",
                duration=3.0):
    """
    text - текст строки
    text_color - цвет текста доступные варианты смотрите в TextClip.list('color')
    width - ширина
    height - высота
    filename - имя файла
    duration - продолжительность видео
    """
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 30)
    size = font.getlength(text)
    print(size)

    def position(t):
        """
        Вспомогательная функция
        :param t:
        принимает время в формате double
        :return:
        Возвращает позицию текста - tuple с позициями по X и Y в зависимости от времени

        """
        return width / 2 + (-(size / duration) * t), "center"
    #создаём объект с текстом, указывает в позиции вспомогательную функцию которая расчитывает позицию по секундам
    add_text = TextClip(text, fontsize=30, color=text_color, font="Arial") \
        .set_position(position) \
        .set_duration(duration)

    # создаём сгруппированное видео из текста
    final = CompositeVideoClip([add_text], size=(width, height), bg_color=background_color)
    final.duration = duration
    final.fps = 60
    final.write_videofile(filename)

#доступные цвета текста
print("available text colors:")
for i in TextClip.list('color'):
    print(i)

# вызов функции
text_tickle(
    "очень длинный текст",
    filename="new.mp4",
    text_color="SteelBlue1"
    )
