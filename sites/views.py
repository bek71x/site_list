from django.shortcuts import render

from sites.models import Site


def sites_list(request):
    sites = Site.objects.all()

    context = {'sites': sites}
    return render(request, 'home.html', context)

def sites_detail(request,site_id):
    site = Site.objects.get(id =site_id)

    context = {'site': site}

    return render(request,'detail.html', context)

