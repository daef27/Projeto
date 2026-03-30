from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio, Noticia, HistoricoPagamento, Historia, Esporte, Cliente, Doacao
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from .models import Parceiro  # Certifique-se que o modelo Parceiro existe

def parceiros_view(request):
    parceiros = Parceiro.objects.all()
    return render(request, 'parceiros.html', {'parceiros': parceiros})

def esportes_view(request):
    esportes = Esporte.objects.filter(ativo=True)
    clientes = Cliente.objects.all()
    doacoes = Doacao.objects.all()

    context = {
        'esportes': esportes,
        'clientes': clientes,
        'doacoes': doacoes,
    }

    return render(request, 'esportes.html', context)


def home(request):
    noticias = Noticia.objects.all().order_by('-data')
    return render(request, 'home.html', {'noticias': noticias})


def cadastro(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        numero = request.POST.get('numero')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        senha = request.POST.get('senha')

        if Socio.objects.filter(cpf=cpf).exists():
            return render(request,'cadastro.html',{
                'erro':'CPF já cadastrado'
            })

        Socio.objects.create(
            nome=nome,
            numero_socio=numero,
            cpf=cpf,
            rg=rg,
            senha=make_password(senha)
        )

        return redirect('login')

    return render(request,'cadastro.html')


def login_view(request):

    erro = None

    if request.method == 'POST':

        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:

            socio = Socio.objects.get(cpf=cpf)

            if check_password(senha, socio.senha):

                request.session['socio_id'] = socio.id

                return redirect('dashboard')

            else:
                erro = 'CPF ou senha inválidos'

        except Socio.DoesNotExist:

            erro = 'CPF ou senha inválidos'


    return render(request,'login.html',{
        'erro':erro
    })


def dashboard(request):

    socio_id = request.session.get('socio_id')

    if not socio_id:
        return redirect('login')

    socio = get_object_or_404(Socio, id=socio_id)

    ano_atual = datetime.now().year
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

    historico, created = HistoricoPagamento.objects.get_or_create(
        socio=socio,
        ano=ano_atual
    )

    historicos = HistoricoPagamento.objects.filter(
        socio=socio
    ).order_by('-ano')


    pagamentos = {

        'Jan': historico.jan,
        'Fev': historico.fev,
        'Mar': historico.mar,
        'Abr': historico.abr,
        'Mai': historico.mai,
        'Jun': historico.jun,
        'Jul': historico.jul,
        'Ago': historico.ago,
        'Set': historico.set,
        'Out': historico.out,
        'Nov': historico.nov,
        'Dez': historico.dez,

    }

    pagos = sum(1 for v in pagamentos.values() if v)
    total = len(pagamentos)


    context = {

        'socio': socio,
        'historico': historico,
        'historicos': historicos,
        'data_atual': data_atual,
        'ano_atual': ano_atual,
        'pagamentos': pagamentos,
        'pagos_percent': (pagos/total)*100,
        'pendentes_percent': ((total-pagos)/total)*100,

    }

    return render(request,'dashboard.html',context)


def logout_view(request):

    request.session.flush()

    return redirect('login')