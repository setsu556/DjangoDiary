from datetime import datetime
from zoneinfo import ZoneInfo

from django.shortcuts import render, redirect
from django.views import View

from diary.forms import PageForm
from diary.models import Page


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


class PageListView(View):
    @staticmethod
    def get(request):
        # DBから全件を取得する
        page_all = Page.objects.all()
        return render(request, 'diary/page_list.html', {'page_list': page_all})


index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
