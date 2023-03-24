from django.shortcuts import render
from core.models import Consumer
import requests


def calculardesconto(consumo,tax_type):

    coverage = 0
    applied_discount = 0

    if consumo < 10000:
        coverage = 0.9

        if tax_type == "Residencial":
            applied_discount = 0.18
        elif tax_type == "Comercial":
            applied_discount = 0.16
        elif tax_type == "Industrial":
            applied_discount = 0.12

    elif 10000 <= consumo <= 20000:
        coverage = 0.95

        if tax_type == "Residencial":
            applied_discount = 0.22
        elif tax_type == "Comercial":
            applied_discount = 0.18
        elif tax_type == "Industrial":
            applied_discount = 0.15

    elif consumo > 20000:
        coverage = 0.99

        if tax_type == "Residencial":
            applied_discount = 0.25
        elif tax_type == "Comercial":
            applied_discount = 0.22
        elif tax_type == "Industrial":
            applied_discount = 0.18

    return (

        applied_discount,
        coverage,
    )


def view1(request):
    if request.method == 'POST':

        nome = request.POST['nome']
        documento = request.POST['documento']
        cep = request.POST['cep']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        consumo = request.POST['consumo']
        tarifa = request.POST['tarifa']
        tipo = request.POST['tipo']

        # desconto, coverage = calculardesconto(consumo,tipo)

        consumer = Consumer.objects.create(
            name=nome,
            document=documento,
            zip_code=cep,
            city=cidade,
            state=estado,
            consumption=consumo,
            distributor_tax=tarifa
        )

        consumer.save()

        consumers = Consumer.objects.all()

        return render(request, 'listagem.html', {
            'consumers': consumers
        })

        return render(request, 'listagem.html')

    return render(request, 'cadastro.html')


def view2(request):
    consumers = Consumer.objects.all()

    return render(request, 'listagem.html', {
        'consumers': consumers
    })


def consulta_cep(request, input_value):

    if input_value:
        response = requests.get(f'https://viacep.com.br/ws/{input_value}/json/')

        if response.status_code == 200:
            dados = response.json()

            return render(request, 'cadastro.html', {
                'dados': dados
            })
    return render(request, 'cadastro.html')


# def buscar(request):
#     if 'buscar' in request.GET:
#             tipo-consumidor = request.GET['tipo-consumidor']
#
#             if buscar:
#
#                 consumers = Consumer.objects.filter(consumption=tipo-consumidor)
#
#                 return render(request, 'listagem.html', {
#                     'consumers': consumers
#                 })
#
#     return render(request, 'listagem.html')