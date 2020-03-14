# Create your views here.
from django.http import HttpResponse
from django.template import loader

import datetime
import math

def index(request):
    template = loader.get_template('index.html')
    context = {}
    if request.method == 'GET' and request.GET.get('sampleg'):
        sample_g = request.GET.get('sampleg')
        times_silica = request.GET.get('silica')
        rf = request.GET.get('rf')
        context['sample_g'] = sample_g
        context['times_silica'] = times_silica
        context['rf'] = rf
        
            
            
        def column_height(radius, column_volume):
            listy = []
            column_height=column_volume/(math.pi*radius**2)
            diameter=2*radius
            if 6<column_height<25:
                listy.append(f'FOR: column diameter = {diameter} cm</br>')
                listy.append(f'     column height = {round(column_height)} cm</br>')
                return listy
            else:
                return ''

        def column_size(sample_g, times_silica, rf):
            listy = []
            silica_density=1/2.5
            silica_mass=float(sample_g)*float(times_silica)
            column_volume=silica_mass/silica_density
            listy += [f'silica mass = {silica_mass} grams']
            listy += [f'"column volume" ~ {column_volume} mL of silica']
            radius = 0.5
            for i in range(14):
                listy += [column_height(radius, column_volume)]
                radius=radius+0.5

            rf = float(rf)
            if 1>rf>0:
                elute_column_volume=1/rf
                elute_volume=elute_column_volume*column_volume
                number_fractions=0.8*(13+int(75*rf**2)+int(7*rf))
                fraction_volume=elute_volume/number_fractions
                listy += [f'Suggested:</br>     fraction volume ~ {round(fraction_volume)} mL</br>']
                listy += [f'     fractions untill cmpd. starts eluting ~ {int(number_fractions)}']
                listy += [f'    (total volume untill cmpd. starts eluting ~ {round(elute_volume)} mL']
            
            return listy

        listy = column_size(sample_g, times_silica, rf)
        context['listy'] = listy





    
    
    
    return HttpResponse(template.render(context, request))