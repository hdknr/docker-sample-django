from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    # メモ詳細
    path('detail/<int:pk>/', views.MemoDetail.as_view(), name='detail'),
    # 新規作成
    path('create/', views.MemoCreate.as_view(), name='create'),
    # メモ編集
    path('update/<int:pk>/', views.MemoUpdate.as_view(), name='update'),
    # メモ削除
    path('delete/<int:pk>/', views.MemoDelete.as_view(), name='delete'),
    # 復習一覧
    path('review/', views.MemoReview.as_view(), name='review'),
    # 復習詳細
    path('review_detail/<int:pk>', views.ReviewDetail.as_view(),
         name='review_detail'),
    # 復習時間の変更
    path('change_time/<int:memo_id>', views.change_time, name='change_time'),
    # メモ一覧
    path('', views.MemoList.as_view(), name='memo'),
]