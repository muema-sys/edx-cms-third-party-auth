import third_party_auth

from contentstore.views.course import course_handler
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from third_party_auth import pipeline


@login_required
def course(request):
    response_format = request.GET.get('format', 'html')
    if request.method == 'GET' and response_format == 'html' and 'application/json' not in request.META.get('HTTP_ACCEPT', 'application/json'):
        running_pipeline = pipeline.get(request)
        if running_pipeline is not None:
            current_provider = third_party_auth.provider.Registry.get_from_pipeline(running_pipeline)
            if current_provider is not None:
                redirect_to = pipeline.get_complete_url(current_provider.backend_name)
                return redirect(redirect_to)

    return course_handler(request)
