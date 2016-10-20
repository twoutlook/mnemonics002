
導出 xls 時
如果想要直接 import, 居然不行, 報錯。
使用複製貼上到另一個 Excel , 才發現資料有掉。


導出 ods 時,沒有發現異常。受限在 Django Import Format 少於  Import Format 的選項，只好
在 OpenOffice 另存為 xls，可以直接用來 import.

理論上5,8,13,19的起勢和收勢都是一樣的口訣
如何設計資料的完整性?





http://mp.weixin.qq.com/s?__biz=MjM5MDE4Njc0MQ==&mid=2650994138&idx=3&sn=bd172b36fbc24f9ca0aaf57228ece44d&chksm=bdbef8408ac97156509239591c3fd96f803c364d4241ce9d1e646dcd4d4c77f7bd799da732f2&scene=0#wechat_redirect


https://docs.djangoproject.com/en/1.10/topics/http/urls/

    urlpatterns = [
        url(r'^articles/2003/$', views.special_case_2003),
        url(r'^articles/([0-9]{4})/$', views.year_archive),
        url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
        url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    ]
https://www.w3.org/Provider/Style/URI

# My Note
Git 的指令學習需要階段性

以
 tag v0.1

local/remote show/add/delete

- local show: 
  `git tag`

- local add:  
  `tag -a v0.1 -m"blank mysite and app001 with superuser ubuntu"`
- local delte: `git tag --delete v0.1`


