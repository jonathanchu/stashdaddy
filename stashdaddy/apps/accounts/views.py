from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def account(request):
    """
    Profile view
    """
    try:
        profile_obj = request.user.get_profile()
    except ObjectDoesNotExist:
        return 0
    return render_to_response("accounts/profile.html", {
        "profile_obj": profile_obj,
    }, context_instance=RequestContext(request))
