from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from datetime import datetime

@receiver(user_logged_in)
def capture_login_time(sender, request, user, **kwargs):
    # Зберігаємо час входу в сесію у форматі ISO
    request.session['login_time'] = datetime.now().isoformat()
