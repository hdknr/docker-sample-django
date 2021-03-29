from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Memo
from django.utils import timezone
from django.urls import reverse
from .forms import MemoForm
import datetime


# メモ一覧
class MemoList(generic.ListView):
    template_name = 'memo/memo.html'
    model = Memo

    context_object_name = 'memos'
    # 1ページ9個まで表示
    paginate_by = 12

    # 検索機能
    def get_queryset(self):
        memos = Memo.objects.all()
        if 'q' in self.request.GET and self.request.GET['q'] is not None:
            q = self.request.GET['q']
            memos = memos.filter(question__icontains=q)
        username = self.request.user.username
        return memos.filter(user__username__iexact=username)


# メモ詳細
class MemoDetail(generic.DetailView):
    template_name = 'memo/memo_detail.html'
    model = Memo


# メモ新規作成
class MemoCreate(generic.CreateView):
    template_name = 'memo/memo_create.html'
    model = Memo
    # 新規作成フィールド
    form_class = MemoForm

    success_url = reverse_lazy('memo:memo')
    #
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


# メモ編集
class MemoUpdate(generic.UpdateView):
    template_name = 'memo/memo_update.html'
    model = Memo
    # 編集フォーム
    fields = ('question', 'text', 'tag', 'update_time')

    # 新規作成後の画面
    def get_success_url(self):
        return reverse('memo:detail', kwargs={'pk': self.object.pk})


# メモ削除
class MemoDelete(generic.DeleteView):
    template_name = 'memo/memo_delete.html'
    model = Memo

    # メモ削除後の画面
    success_url = reverse_lazy('memo:memo')


# メモ復習
class MemoReview(generic.ListView):
    template_name = 'memo/memo_review.html'
    model = Memo

    context_object_name = 'reviews'
    paginate_by = 12

    # 復習日が今日のものを表示
    def get_queryset(self):
        memos = Memo.objects.all()
        # memos = memos.filter(update_time__lte=date.today())
        if 'q' in self.request.GET and self.request.GET['q'] is not None:
            q = self.request.GET['q']
            memos = memos.filter(question__icontains=q)
        username = self.request.user.username
        return memos.filter(user__username__iexact=username)
        # return Memo.objects.filter(update_time__lt=date.today())


# 復習詳細
class ReviewDetail(generic.DetailView):
    template_name = 'memo/review_detail.html'
    model = Memo


# 復習日時とカウンターの変更
def change_time(request, memo_id):
    # エラー出力
    one_memo = get_object_or_404(Memo, id=memo_id)

    # カウンターが1~5までのものに制御
    if 1 <= one_memo.counter <= 5:
        # カウンターが1の時
        if one_memo.counter == 1:
            one_memo.update_time = timezone.datetime.today() + datetime.timedelta(days=3)
            one_memo.counter += 1

        elif one_memo.counter == 2:
            one_memo.update_time = timezone.datetime.today() + datetime.timedelta(days=7)
            one_memo.counter += 1

        elif one_memo.counter == 3:
            one_memo.update_time = timezone.datetime.today() + datetime.timedelta(days=16)
            one_memo.counter += 1

        elif one_memo.counter == 4:
            # one_memo.update_time = date.today() + timedelta(days=25)
            one_memo.counter += 1
        else:
            one_memo.counter += 10

    one_memo.save()
    return redirect('memo:review')
