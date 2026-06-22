from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project
from .forms import ContactForm


def home(request):

    projects = Project.objects.all()

    form = ContactForm()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            full_message = f"""
Name: {name}

Email: {email}

Message:
{message}
"""

            send_mail(
                subject,
                full_message,
                email,
                ["ajaykrishnamsetty4@gmail.com"],
                fail_silently=False,
            )
            send_mail(
    "Thank You for Contacting Me",
    f"""
Hello {name},

Thank you for reaching out.

I have received your message and will get back to you as soon as possible.

Regards,
Ajay Krishnamsetty
Backend Developer
""",
    "ajaykrishnamsetty4@gmail.com",
    [email],
    fail_silently=False,
)

            return render(
                request,
                "core/home.html",
                {
                    "projects": projects,
                    "form": ContactForm(),
                    "success": True
                }
            )

    return render(
        request,
        "core/home.html",
        {
            "projects": projects,
            "form": form
        }
    )