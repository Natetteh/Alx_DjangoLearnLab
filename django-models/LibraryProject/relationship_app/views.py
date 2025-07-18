from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def check_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def check_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
