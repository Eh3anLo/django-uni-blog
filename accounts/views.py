from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic , View
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.contrib.auth import login , logout
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import CustomUser, OTP
from .forms import EmailForm, OTPForm , CustomUserCreationForm
# Create your views here.
class SignOutView(View):
    def post(self, request):
        logout(request.user)

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class SendOTPView(UserPassesTestMixin , View):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def get(self, request):
        form = EmailForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp_code = get_random_string(length=6, allowed_chars='0123456789')
            OTP.objects.create(email=email, code=otp_code)
            send_mail(
                'کد عبور برای نشریه',
                f'''کد یک بار مصرف شما جهت ورود در سامانه  
                {otp_code}
    ''',
                'ehsunlotfy@gmail.com',
                [email],
                fail_silently=False,
            )
            request.session['email'] = email
            return redirect('validate_otp')
        return render(request, 'registration/login.html', {'form': form})

class ValidateOTPView(UserPassesTestMixin , View):
    def test_func(self):
        return not self.request.user.is_authenticated

    def get(self, request):
        email = request.session.get('email')
        if not email:
            redirect('send_otp')
        form = OTPForm()
        return render(request, 'registration/login_validate.html', {'form': form})

    def post(self, request):
        email = request.session.get('email')
        if not email:
            return redirect('send_otp')

        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp']
            try:
                otp = OTP.objects.get(email=email, code=otp_code)
            except OTP.DoesNotExist:
                form.add_error('otp', 'کد وارده نامعتبر است.')
            else:
                if otp.expires_at < timezone.now():
                    form.add_error('otp', 'کد منقضی شده است.')
                else:
                    user, created = CustomUser.objects.get_or_create(email=email)
                    if created:
                        user.username = email.split('@')[0]
                        user.set_unusable_password()  # No password needed
                        user.save()
                        login(request, user)
                        return redirect('user_profile' , username = user.username)
                    # del request.session['email']
                    login(request, user)
                    return redirect('article_list')
        return render(request, 'registration/login_validate.html', {'form': form})
