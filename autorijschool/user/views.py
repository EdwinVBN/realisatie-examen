from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditUserForm, LesEditForm, UserRegister, EigenaarEditUserForm, AutoCreateForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Les, Lespakket, Gebruiker_Lespakket, Gebruiker, Auto
from django.contrib.auth import authenticate

class User:
    @staticmethod
    def login(request):
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('profile')
        else:
            form = CustomAuthenticationForm()

        return render(request, "login.html", {'form': form})
    
    @staticmethod
    def logout(request):
        auth_logout(request)
        return redirect('login')

    @staticmethod
    def home(request):
        return render(request, 'home.html')
    
    @staticmethod
    @login_required
    def profiel(request):
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = EditUserForm(instance=request.user)

        return render(request, 'profiel.html', {
            'form': form,
            })
    
class Klant:
    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = UserRegister(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        else:
            form = UserRegister()

        return render(request, "register.html", {'form': form})
    
    @staticmethod
    @login_required
    def planning(request):
        if request.user.rol == 'eigenaar':
            return redirect('home')
        
        lessen = Les.objects.filter(gebruiker=request.user)

        return render(request, 'planning.html', {'lessen': lessen})
    
    @staticmethod
    @login_required
    def lesinfo(request, id):
        if request.user.rol == 'eigenaar':
            return redirect('home')

        les = get_object_or_404(Les, id=id, gebruiker=request.user)

        if request.method == 'POST':
            form = LesEditForm(request.POST, instance=les)
            if form.is_valid():
                form.save()
                return redirect('lesinfo', id=les.id)
        else:
            form = LesEditForm(instance=les)

        return render(request, 'lesinfo.html', {'les': les, 'form': form})

    @staticmethod
    @login_required
    def lespakket(request):
        if request.user.rol == 'eigenaar':
            return redirect('home')
        
        lespakketten = Lespakket.objects.all()
        gebruiker_lespakket = Gebruiker_Lespakket.objects.filter(gebruiker=request.user).first()
        
        if 'lespakket_id' in request.POST:
            lespakket = get_object_or_404(Lespakket, id=request.POST['lespakket_id'])
            if gebruiker_lespakket:
                # Update bestaand lespakket
                gebruiker_lespakket.lespakket = lespakket
                gebruiker_lespakket.save()
            else:
                # Maak nieuw als geen
                Gebruiker_Lespakket.objects.create(
                    gebruiker=request.user,
                    lespakket=lespakket
                )
            return redirect('lespakket')
        
        return render(request, 'lespakket.html', {
            'lespakketten': lespakketten,
            'gebruiker_lespakket': gebruiker_lespakket

        })

class Eigenaar:
    @staticmethod
    @login_required
    def beheer(request):
        klanten = Gebruiker.objects.filter(rol='klant')
        instructeurs = Gebruiker.objects.filter(rol='instructeur')

        if request.user.rol != 'eigenaar':
            return redirect('home')

        return render(request, 'beheer.html', {
            'klanten': klanten,
            'instructeurs': instructeurs,
        })

    @staticmethod
    @login_required
    def profile_details(request, id):
        gebruiker = get_object_or_404(Gebruiker, id=id)
        return render(request, 'profile_details.html', {'gebruiker': gebruiker})

    @staticmethod
    @login_required
    def profile_details_edit(request, id):
        if request.user.rol != 'eigenaar':
            return redirect('home')
            
        gebruiker = get_object_or_404(Gebruiker, id=id)
        
        if request.method == 'POST':
            form = EigenaarEditUserForm(request.POST, instance=gebruiker)
            if form.is_valid():
                form.save()
                return redirect('profile_details', id=gebruiker.id)
        else:
            form = EigenaarEditUserForm(instance=gebruiker)

        return render(request, 'profile_details.html', {
            'gebruiker': gebruiker,
            'form': form
        })
    
    @staticmethod
    @login_required
    def autos(request):
        if request.user.rol != 'eigenaar':
            return redirect('home')

        autos = Auto.objects.all()
        return render(request, 'autos.html', {'autos': autos})

    @staticmethod
    @login_required
    def auto_details(request, id):
        if request.user.rol != 'eigenaar':
            return redirect('home')

        auto = get_object_or_404(Auto, id=id)
        return render(request, 'auto.html', {'auto': auto})

    @staticmethod
    @login_required
    def auto_create(request):
        if request.user.rol != 'eigenaar':
            return redirect('home')

        if request.method == 'POST':
            form = AutoCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('autos')
        else:
            form = AutoCreateForm()

        return render(request, 'auto_create.html', {'form': form})

    @staticmethod
    @login_required
    def auto_edit(request, id):
        if request.user.rol != 'eigenaar':
            return redirect('home')
            
        auto = get_object_or_404(Auto, id=id)
        
        if request.method == 'POST':
            form = AutoCreateForm(request.POST, instance=auto)
            if form.is_valid():
                form.save()
                return redirect('auto_details', id=auto.id)
        else:
            form = AutoCreateForm(instance=auto, initial={'type': auto.soort.type})

        return render(request, 'auto.html', {
            'auto': auto,
            'form': form
        })

    @staticmethod
    @login_required
    def auto_delete(request, id):
        if request.user.rol != 'eigenaar':
            return redirect('home')
            
        auto = get_object_or_404(Auto, id=id)
        auto.delete()
        return redirect('autos')

    @staticmethod
    @login_required
    def deactivateren(request, id):
        if request.user.rol != 'eigenaar':
            return redirect('home')
            
        gebruiker = get_object_or_404(Gebruiker, id=id)
        gebruiker.is_active = False
        gebruiker.save()
        
        return redirect('beheer')
    
    @staticmethod
    @login_required
    def activateren(request, id):
        if request.user.rol != 'eigenaar':
            return redirect('home')

        gebruiker = get_object_or_404(Gebruiker, id=id)
        gebruiker.is_active = True
        gebruiker.save()
        return redirect('beheer')

