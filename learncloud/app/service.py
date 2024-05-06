import base64
import os
from io import BytesIO

from wordcloud import WordCloud

from app.models import Posts


def generate_wordcloud_image(posts: list[Posts]):
    if len(posts) == 0:
        return
    skill_names = [post.skill_name.strip() for post in posts]
    text = " ".join(skill_names)
    # 日本語対応するためにフォントを指定する
    # os.path.join()を使用することで区切り文字の違いなどOSに依存せずパスを生成できる。
    font_path = os.path.join(
        "app", "static", "fonts", "ipaexg00401", "ipaexg.ttf"
    )
    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=400,
        background_color="white",
    ).generate(text)
    return _to_image(wordcloud)


def _to_image(wordcloud):
    # ワードクラウドを画像に変換
    image = wordcloud.to_image()
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    image_png = buffer.getvalue()
    buffer.close()

    # 画像データをBase64エンコードしてバイナリ型にする
    image_base64_binary = base64.b64encode(image_png)
    # UTF-8で文字列にデコードしてHTMLに埋め込める形式にする
    image_base64_string = image_base64_binary.decode("utf-8")
    return image_base64_string
