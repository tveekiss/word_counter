from django.shortcuts import render
from django.http import HttpResponse
from .utils import load_file, word_count, clear_memory


def index(request):
    return render(request, 'index.html')


def load(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_contents = file.read().decode('utf-8')
        load_file(file_contents)
        return HttpResponse("Файл успешно загружен.")
    return HttpResponse("Метод не разрешен.")


def wordcount(request):
    if request.method == 'POST':
        word = request.POST['word']
        count = word_count(word)
        return HttpResponse(f"Слово '{word}' встречается {count} раз(а).")
    return HttpResponse("Метод не разрешен.")


def clear(request):
    clear_memory()
    return HttpResponse("Память успешно очищена.")
