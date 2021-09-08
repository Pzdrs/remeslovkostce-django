from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView

from .models import ProductCategory, Product


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'index': True}

    # TODO: To same plati i pro ContactView. Pokud nepridavate nic potrebneho do contextu, pak je definice
    #  get_context_data nadbytecna vnasite si jen do kodu potencialni misto kde udelat chybu. Taky jsem toho hodne
    #  definoval znovu ale casem jak poznavam Django lenivim a snazim se maximum prace na existujici infrastrukture :)
    #  Aby bylo jasno neni to chyba jen je potreba dat pozor jestli nahodou nemazete nejakou jiz existuici funkcionaliu.
    #  A to Vy tady delate. Pokud je to zamer je to samozrejme v poradku, pokud ne vzdy osetrete existujici parent
    #  objekty. V tomto pripade TemplateView vychazi z ContextMixin a ten ma take definovanou get_context_data.
    #  Ta dela uzitecnou vec a to ze vlozi do contextu dictionary context definici z parametru ContextMixin.extra_context.
    #  To je super na staticke parametry vkladane do kontextu tedy napr. presne na to co delate Vy. Takze za predpokladu
    #  ze potrebujete parametr co vkladate do contextu (pominu fakt ze ho nikde nepouzivate ale rekneme je potreba)
    #  lze to udelat definici viz vyse...pokud to nestaci nezapomente vzdy volat super().get_context_data ve sve
    #  implementaci jinak o to co nekdo udelal pred vami v tomto pripade ContextMixin prijdete. To je pri sdileni kodu a
    #  vytvareni modulu s podpurnymi class base dviews nezadouci, protoze nekdo kdo pouzije Vas View objekt,
    #  pokud mu to nereknete v doc stringu objektu ocekava ze vse funguje jak je zvykly...
    #def get_context_data(self, **kwargs):
    #    return {'index': True}


class ContactView(TemplateView):
    template_name = 'contact.html'

    #def get_context_data(self, **kwargs):
    #    return {'contact': True}


class CatalogListView(ListView):
    template_name = 'catalog.html'
    model = ProductCategory
    context_object_name = 'categories'

    #def get_context_data(self, *, object_list=None, **kwargs):
    #    context = super().get_context_data(object_list=object_list, **kwargs)
    #    context['catalog'] = True
    #    return context


class CategoryProductsView(ListView):
    template_name = 'category.html'
    context_object_name = 'products'

    error_message = None
    category = None

    # TODO: kdyz kouknete do te dokumentace ke class based view, tak velmi casto __init__ nemaji vubec.
    #  Uvidite ze pokud je to sdilena promena objektu dava se jako 'staticka' tedy definuje se podobne jako
    #  treba template_view... Takze urcite to neni zadna chyba, ale pokud to dava smysl a neni to neco specifickeho
    #  vyhybam se psat constructor __init__ ale nekdy se tomu nevyhnu, treba pokud ten parametr je naplnen dynamicky
    #  pomoci nejakych treba objektovych funkci a potrebuji ho od sameho pocatku existence objektu tak se tomu nevyhnete.
    #  Ale tak jak je pouzivate zde v oprikladu bych constructor nedelal a definoal bych ty promenne staticky...
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.error_message = None
    #    self.category = None

    # TODO: zde mam dve spolu nesouvisejici poznamky ke kodu. 1. try - except a 2. error.html
    #  1. pokud je to co chcete, tedy pokud neexistuje dane id kategorie (slag) tak vyhod chybu a nic jineho neni
    #  prijatelne pak ok. Pokud vsak treba pokud je zadana chybna kategorie je to ignorovano a jako by nic zadaneho
    #  nebylo (coz treba ja osobne preferuji) tak se da pouzit:
    #  self.category = ProductCategory.objects.filter(slug=self.kwargs['category_slug']).first()
    #  efekt pokud je vse ok je stejny pokud neexistuje kkategotrie kod muze bez tvrde chyby pokracovat dal,
    #  pokud je to zadouci a treba zobrazit vsechny kategorie...
    #  2. snazte se at class view dela jen jednu vec a dobre a nic jineho. Vy zobrazujete detail kategorie a najednou
    #  dojde-li k chybe natvrdo prehodite sablonu a zobrazite chybu. Urcite to funguje, jen to je pro mne matouci.
    #  Takze ja delam to ze bud odchytavam chybu a v ramci existujici sablony treba nejakou podminkou bud zobrazim
    #  obsah co se ma, nebo nejakou chybovou hlasku v ramci existujici sablony (vlozim nejaky kousek hotoveho kodu
    #  ktery opakovane pouzivam - rikam jim snippets), nebo druha varianta napisu samostatne view nebo i nekolik
    #  error view na zobrazeni chybove hlasky a pouziji k tomu volani HttpResponseRedirect na vhodnem miste tedy kde se
    #  vraci django response objekt
    #  Podle toho jak mate napsanou get_context_data mi to ukazuje na volbu prvni varianty tedy modifikaci sablony
    #  category.html o zobrazeni chybove hlasky, protoze chybovou zpravu posilate do contextu. Zde je krasne videt
    #  jak je to pro mne matouci, protoze cast context parametru je urcena jedne sablone a cast druhe

    def get_queryset(self):
        try:
            self.category = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
            return Product.objects.filter(category_id=self.category.id)
        except ObjectDoesNotExist:
            self.error_message = 'Tento produkt neexistuje'
            self.template_name = 'error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalog'] = True
        context['category'] = self.category
        context['message'] = self.error_message
        return context
