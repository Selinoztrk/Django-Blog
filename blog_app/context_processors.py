from .models import Category

def category_menu(request):
    return {
        'cat_menu': Category.objects.all()
    }
