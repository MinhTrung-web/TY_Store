from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


# Create your views here.

# Đăng ký người dùng mới
class Register(SuccessMessageMixin, generic.CreateView):
    form_class = UserCreationForm
    success_message = "Registration Successful! You can now login."
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

# Trang chỉnh sửa hồ sơ 
@login_required
def profile(req):
    UserEditForm = modelform_factory(get_user_model(), fields=('first_name', 'last_name', 'username'))
    form = UserEditForm(instance=req.user)
    if req.method == "POST":
        form = UserEditForm(instance=req.user, data=req.POST)
        if form.is_valid():
            form.save()
    return render(req, 'registration/profile.html', {'form': form})

# Đăng xuất người dùng
def logout_view(request):
    if request.method == 'POST':  # Đảm bảo phương thức POST khi đăng xuất
        logout(request)  # Gọi hàm logout để đăng xuất người dùng
        return redirect('logged_out')  # Chuyển hướng đến trang thông báo đã đăng xuất
    else:
        return redirect('/')  # Trường hợp nếu yêu cầu không phải POST, chuyển hướng về trang chủ
# View cho trang thông báo đăng xuất
def logged_out(request):
    return render(request, 'registration/logged_out.html')  # Bạn cần tạo template này