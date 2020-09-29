from django.contrib import admin

# Register your models here.
from .models import Aluno, Motorista, Van

# Register your models here.
admin.site.register(Motorista)
admin.site.register(Van)
admin.site.register(Aluno)