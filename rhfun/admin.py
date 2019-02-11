# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Pessoa, Vaga, Curriculo

admin.site.register(Pessoa)
admin.site.register(Vaga)
admin.site.register(Curriculo)


# Register your models here.
