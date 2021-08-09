from django.shortcuts import render
import pafy


def ytd_down(request):
    return render(request, 'ytindex.html')


def yt_down(request):
    if request.method == "POST":
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embed_link = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embed_link

        }
        return render(request, 'yt_download.html', context)
    return render(request, 'yt_download.html')

