from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response({
            'title': 'Home Page',
            'description': 'This is the home page',
        })

class AboutView(APIView):
    def get(self, request):
        return Response({
            'title': 'About Page',
            'description': 'This is the about the website',
        })

class FAQView(APIView):
    def get(self, request):
        return Response({
            'title': 'Contact Page',
            'description': 'This is the contact page',
        })