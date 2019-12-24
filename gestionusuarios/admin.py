from django.contrib import admin
from .models import Usuario
from .models import Tipo
from .models import Term
from .models import Statuspropuesta
from .models import Propuesta

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tipo)
admin.site.register(Term)
admin.site.register(Statuspropuesta)
admin.site.register(Propuesta)

