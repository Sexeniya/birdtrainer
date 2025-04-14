from django.shortcuts import render, redirect
from .models import Bird
from .forms import BirdForm
from random import choice
import random

def home(request):
    return render(request, 'birds/home.html')

def bird_list(request):
    birds = Bird.objects.all()
    return render(request, 'birds/bird_list.html', {'birds': birds})

def add_bird(request):
    if request.method == 'POST':
        form = BirdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bird_list')
    else:
        form = BirdForm()
    return render(request, 'birds/add_bird.html', {'form': form})

def quiz(request):
    shown_birds = request.session.get('shown_birds', [])

    if request.method == 'POST' and request.POST.get('bird_id'):
        bird_id = int(request.POST.get('bird_id'))
        bird = Bird.objects.get(id=bird_id)
        answer = request.POST.get('answer', '').strip().lower()
        correct = (answer == bird.name.lower())

        # Добавляем текущую птицу в список показанных
        if bird.id not in shown_birds:
            shown_birds.append(bird.id)
        request.session['shown_birds'] = shown_birds

        return render(request, 'birds/quiz.html', {
            'bird': bird,
            'result': 'Правильно!' if correct else f'Неправильно. Это {bird.name}',
            'show_result': True,
        })

    # Показываем новую птицу
    remaining_birds = Bird.objects.exclude(id__in=shown_birds)
    if not remaining_birds.exists():
        request.session['shown_birds'] = []  # сброс
        return render(request, 'birds/quiz.html', {'result': 'Квиз завершён!', 'quiz_over': True})

    bird = random.choice(remaining_birds)
    return render(request, 'birds/quiz.html', {'bird': bird})


