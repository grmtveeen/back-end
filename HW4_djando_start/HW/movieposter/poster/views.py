from django.shortcuts import render
from django.http.response import JsonResponse, Http404, HttpResponse
import json

posters = [dict(id=1, name='Большой лебовский', description='Джефф Лебовски по прозвищу Чувак — самый ленивый человек в Лос-Анджелесе: закоренелый холостяк, которого ничего не интересует, кроме боулинга и алкоголя. Но однажды к Чуваку врываются два бандита и начинают пугать долгом в миллион долларов.', main_actor='Джефф Бриджес', year=2021,
              link="https://www.youtube.com/embed/M6_JJK5IIDU", date='18:46', img='static/img/header5.jpg'),
         dict(id=2, name='Гнев человеческий', description='В инкассаторскую компанию устраивается новый сотрудник Эйч (Джейсон Стэйтем). Он тих и немногословен, что, в принципе, приветствуется в такой сфере, где каждый день перевозят по Лос-Анджелесу миллионы долларов наличными. Но внутри этого загадочного британца бушуют страсти. Он жаждет отомстить банде грабителей, нападавших на инкассаторские машины. Это история мести, которая перемещается по временной шкале то в прошлое, то в настоящее, а также показанная с позиции разных персонажей.', main_actor='Джейсон Стэтхем', year=2021,
              date='15:35', link="https://www.youtube.com/embed/YLw55x-zOSo", img='static/img/header1.jpg'),
         dict(id=3, name='Интерстеллар', description='Братья Кристофер и Джонатан Нолан представляют космическую одиссею под названием «Интерстеллар».Фантастическая драма, в главных ролях которой снялись Мэттью МакКонахии, Энн Хэтэуэй и Джессика Честейн, была номинирована на множество премий и получила «Оскар» за лучшие визуальные эффекты. Действие переносит зрителя в недалекое будущее, когда космос уже почти освоен шагнувшим вперед человечеством, но ресурсы Земли истощены. Из-за растущей концентрации азота на нашей планете царит засуха и, как следствие, глобальный продовольственный кризис. Сотрудники секретной лаборатории НАСА обнаруживают в районе орбиты Сатурна червоточину, позволяющую преодолеть пространственно-временной барьер и в кратчайшие сроки переместиться в другую галактику. Возможно, это шанс на спасение для всего человечества. В рамках программы «Лазарь» совершается первая экспедиция, в результате которой по ту сторону так называемой кротовой норы обнаруживаются три наиболее подходящих для жизни планеты. Теперь настало время для второй экспедиции: профессору Бренду и его коллегам предстоит, рискуя собственными жизнями, провести исследования в условиях, когда один час равен нескольким годам на Земле, и найти способ переселения землян на другую планету. Смогут ли ученые спасти человечество, можно узнать, если смотреть онлайн «Интерстеллар».', main_actor='Мэттью Макконехи', year=2014, date='12:20',
              link="https://www.youtube.com/embed/qcPfI0y7wRU", img='static/img/header2.jpg'),
         dict(id=4, name='Игра в кальмара', description='Из-за нужды в деньгах сотни игроков принимают странное приглашение поучаствовать в детских соревнованиях. Их ждет заманчивый приз, но ставки смертельно высоки.', main_actor='Ли Джон Джэ', year=2021, date='12:20',
              link="https://www.youtube.com/embed/6sI7pZuQZPg", img='static/img/header3.jpg'),
         dict(id=5, name='Черная Вдова', description='Скарлетт Йоханссон в блокбастере Marvel, посвященном одной из «‎Мстителей»‎ Наташе Романофф. Наташа, она же ‎Черная Вдова‎ — бывшая сотрудница КГБ, прошлое которой хранит множество загадок. Сейчас ей предстоит столкнуться со всеми мрачными тайнами лицом к лицу. Пора узнать, как Наташа стала Черной Вдовой.', main_actor='Скарлетт Йоханссон', year=2021, date='12:20',
              link="https://www.youtube.com/embed/0k82-pGgryk", img='static/img/header4.jpg')]


def poster_description(request, post_id):
    if request.method == 'GET':
        print(post_id)
        print(posters[post_id-1])
        if post_id <= len(posters):
            # return JsonResponse(posters[post_id], safe=False)
            return render(request, 'poster/poster_description.html', context={'posters': posters[post_id-1]})
        else:
            raise Http404
    return JsonResponse({'ER': 'You can use only GET for that'}, status=405)


def posters_list(request):
    if request.method == 'GET':
        return render(request, 'poster/posters.html', context={'posters': posters})
    return JsonResponse({'ER': 'You can use only GET for that'}, status=405)


def create_poster(request):
    if request.method == 'POST':
        posters.append(json.loads(request.body.decode('utf-8')))
        return JsonResponse({'OK': 'poster created!'}, status=200)
    return JsonResponse({'ER': 'You have to use only POST for that'}, status=405)


def delete_poster(request):
    if request.method == 'GET':
        if len(posters) > 0:
            posters.pop()
            return JsonResponse({'OK': 'last deleted!'}, status=200)
        else:
            return JsonResponse({'ER': 'Poster is empty'}, status=412)
    return JsonResponse({'ER': 'You have to use only POST for that'}, status=405)
