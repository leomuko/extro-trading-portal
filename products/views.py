from django.shortcuts import render, redirect
from django.core import serializers

from .models import Product, ProductCategory, Trade, Year, Country
from .utils import country_names
# Create your views here.

def search_view(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    countries = Country.objects.all()
    # countries = serializers.serialize('json', countries)

    if request.method == 'POST' or request.method == 'GET':
        print(request.POST)
        product_name = request.POST.get('product name')
        print(product_name)
        trade_type = request.POST.get('trade type')
        print(trade_type)
        country = request.POST.get('country')
        print(country)

        try: 
            if any(char.isdigit() for char in product_name):
                selected_product = Product.objects.get(custom_code=product_name)
            else:
                selected_product = Product.objects.get(description=product_name)

            if trade_type == "Export":
                trade_choice = "Export To"
            else:
                trade_choice = "Import From"

            selected_country = Country.objects.get(name=country)
            selected_trades = Trade.objects.filter(trade_choice=trade_choice,
                                                    product__id=selected_product.id)

            print(selected_country)
            print(selected_trades)

            for trade in selected_trades:
                if selected_country.trade.id == trade.id:
                    print("Successful trade")
                    return render(request, 'search_results.html', {'trade': trade, 
                                                                    'country': selected_country, 
                                                                    'selected_product': selected_product, 
                                                                    'selected_country': selected_country,
                                                                    'products': products, 
                                                                    'countries': countries, 
                                                                    'categories': categories
                                                                })

                else:
                    print("None exsitent trade")
                    errors = {
                        "description": "None Existent Trade!",
                        "message": """
                                The trade you are searching for does not exist in our 
                                system. Please contact our support team for more information.
                        """
                    }
                    return render(request, 'search_results.html', {'errors': errors, 
                                                                    'form_product': product_name, 
                                                                    'form_country': country,
                                                                    'form_trade': trade_type,
                                                                    'products': products, 
                                                                    'countries': countries, 
                                                                    'categories': categories
                                                                })

    
        except (Product.DoesNotExist, Country.DoesNotExist, Trade.DoesNotExist) as e:
            errors = {
                "description": e, 
            }
            return render(request, "search_results.html", {
                "errors": errors,
                "form_product": product_name,
                "form_trade": trade_type,
                "form_country": country,
                'products': products, 
                'countries': countries, 
                'categories': categories
            }) 

    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    countries = Country.objects.all()
    # Serialize countries to JSON object
    # countries = serializers.serialize('json', countries)
    return redirect('/', kwargs={'categories': categories, 'products': products, 'countries': countries})


def home_view(request):
    if request.method == 'GET':
        categories = ProductCategory.objects.all()
        products = Product.objects.all()
        countries = Country.objects.all()

        # Serialize countries to JSON object
        # countries = serializers.serialize('json', countries)

        # countries = []
        # for country in country_names:
        #     countries.append(country[0])
    return render(request, 'home.html', {'categories': categories,
             'products': products,
              'countries': countries})