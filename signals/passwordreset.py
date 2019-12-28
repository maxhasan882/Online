from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    subject = 'Password reset token'
    context = {
        'current_user': reset_password_token.user,
        'reset_password_url': "http://127.0.0.1:8000/userApi/reset/?token={token}".format(token=reset_password_token.key)
    }
    html_content = render_to_string('password.html', {'content': context})
    email_from = settings.EMAIL_HOST_USER
    mail = str(reset_password_token.user.email)
    recipient_list = [mail, 'rhmithu50@gmail.com']
    msg = EmailMessage(subject=subject, body=html_content, from_email=email_from, bcc=recipient_list)
    msg.content_subtype = "html"
    msg.send()


send_email = Signal(providing_args=["email", "content"])


@receiver(send_email)
def user_created_signal_method(sender, **kwargs):
    # print("I am here")
    email = str(kwargs.get("email"))
    content = str(kwargs.get("content"))
    print('Content is......... : ', content)
    subject = 'Thank you for registering to our site'
    content = {"name": "BAl", 'code': "bal", 'mail': email}
    html_content = render_to_string('mail.html', {'content': content})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, 'rhmithu50@gmail.com']
    print('Content is : ', content)
    msg = EmailMessage(subject=subject, body=html_content, from_email=email_from, bcc=recipient_list)
    msg.content_subtype = "html"
    return msg.send()

