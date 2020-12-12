from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from advertiser.models import Advertiser
from advertiser_management.models import AdView


class BaseView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "base_template.html"
    process_ip = True

    def get(self, request):
        queryset = Advertiser.objects.all()
        AdView.increase_views(request.user_ip)
        return Response({'advertisers': queryset})
