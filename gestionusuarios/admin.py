from django.contrib import admin
from .models import Persona
from .models import Tipo
from .models import Term
from .models import Statuspropuesta
from .models import Propuesta
from .models import Statustrabajogrado
from .models import Trabajogrado

# Register your models here.

admin.site.register(Persona)
admin.site.register(Tipo)
admin.site.register(Term)
admin.site.register(Statuspropuesta)
admin.site.register(Propuesta)
admin.site.register(Statustrabajogrado)
admin.site.register(Trabajogrado)

