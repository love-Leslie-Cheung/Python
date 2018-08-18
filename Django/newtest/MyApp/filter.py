from django.shortcuts import render

def test(request):
	a = {'letters':'abc','number':1}
	news_titles = [('12/5', '作者成为全国首富。'), ('12/4', '作者成为全省首富。'),('12/3', '作者成为全市首富。'), ('12/2', '作者成为镇里首富。'), ('12/1', '作者成为村里首富。')]
	a = {'news_titles':news_titles}
	return render(request,'filter.html',a)