from .models import Words


def load_file(text):
    for word in text.split():
        if word.isalpha():
            if Words.objects.filter(word=word).exists():
                db_word = Words.objects.get(word=word)
                db_word.count += 1
                db_word.save()
            else:
                Words.objects.create(word=word)


def word_count(word):
    db_word = Words.objects.get(word=word)
    return db_word.count


def clear_memory():
    for word in Words.objects.all():
        word.delete()
