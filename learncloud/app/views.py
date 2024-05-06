from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from app.forms import PostsForm
from app.models import Posts

from . import service


@require_http_methods(["GET", "POST"])
def top(request):
    if request.method == "GET":
        # フォームを生成
        form = PostsForm()
        # 投稿一覧を取得
        posts = Posts.objects.all()
        # ワードクラウドを生成
        wordcloud_image = service.generate_wordcloud_image(posts)
        print(wordcloud_image)
        context = {
            "form": form,
            "posts": posts,
            "wordcloud_image": wordcloud_image,
        }
        return render(request, "app/top.html", context)
    elif request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(top)
