from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm
from .forms import UserForm
from .models import SearchData
import re


#home page
def home_page(request):
    return render(request,'home.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form.save()
            User=form.save()
            login(request, User)
            return redirect('/search')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password  = form.cleaned_data['password']

            User = authenticate(request, email=email, password=password)
            print(User)
            
            if User is not None:
                login(request, User)
                return redirect('/search')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





def search_paragraphs(n1, n2):
    paragraphs = n1.split('\n\n')  

    found_paragraphs = []
    for idx, paragraph in enumerate(paragraphs,1): 
        if re.search(n2, paragraph, re.IGNORECASE):  
            found_paragraphs.append(idx)

    return found_paragraphs


def SearchWord(request):
    try:
        message=""
        if request.method == "POST":
            n1 = request.POST.get('num1', '').strip()  # Get input data and remove leading/trailing whitespace
            n2 = request.POST.get('num2', '').strip()
            
           
            if not n1 or not n2:  # Check if either input is empty
                message = "Please enter both paragraph and word to search."
            else:
                found_paragraphs = search_paragraphs(n1, n2)
                if found_paragraphs:
                    search_data = SearchData(paragraph=n1, word=n2)
                    search_data.save()
                    message = f" {n2}|{','.join(map(str,found_paragraphs))}"
                    # message = f" '{n2}'|{', '.join('  ' + str(p) for p in found_paragraphs)}"
                    # message = f"Search term '{n2}' found in paragraph(s):{', '.join(map(str, found_paragraphs))}"
                    
                else:
                    message = f"Search term '{n2}' not found."
          
    except Exception as e:
        message = f"An error occurred: {str(e)}"
    
    return render(request, "search.html", {'message': message})

def main_page(request):
    return render(request,'main.html')