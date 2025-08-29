from datetime import datetime
from zoneinfo import ZoneInfo

from django.shortcuts import render, redirect
from django.views import View

from diary.forms import PageForm


class IndexView(View):
    @staticmethod
    def get(request):
        datetime_now = datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y年%m月%d日 %H:%M:%S')
        return render(request, 'diary/index.html', {'datetime_now': datetime_now})


class PageCreateView(View):
    # 入力画面を表示するときの関数
    @staticmethod
    def get(request):
        form = PageForm()
        return render(request, 'diary/page_form.html', {'form': form})

    # 入力画面から送信されたデータを処理するときの関数
    @staticmethod
    def post(request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            # indexは urls.py に紐づいている
            return redirect('diary:index')
        else:
            return render(request, 'diary/page_form.html', {'form': form})


index = IndexView.as_view()
page_create = PageCreateView.as_view()
