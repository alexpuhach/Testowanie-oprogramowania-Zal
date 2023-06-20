# Dokumentacja Zaliczenie Testowanie oprogramowania
**Oleksandr Puhach, nr albomu: 91555**


## 1.   Część związana z kodowaniem (katalog – [code_part](/code_part))
##### Napisałem dość prosty program testowy o nazwie **Task Manager**.  
Pliki programu: 
- [app.py](app.py)
- [task_manager.py](task_manager.py)
- [taks_save.py](taks_save.py)

W tym katalogu znajdują się testy (unittest) dla programu. Ogólna dokumentacja znajduje się w plikach testowych. Poniżej znajduje się pełna dokumentacja dla tych plików:

### [task_manager_test.py](/code_part/tests/task_manager_test.py)

##### test_add_task()
Ten test weryfikuje, czy zadanie zostało poprawnie dodane do listy **TaskManager.tasks**. Sprawdza, czy długość listy zadań wzrasta po dodaniu jednego zadania. Oczekuje się, że długość listy będzie równa 1.

##### test_remove_task()
Ten test weryfikuje, czy zadanie zostało poprawnie usunięte z listy **TaskManager.tasks**. Najpierw dodaje zadanie do listy, a następnie usuwa je za pomocą metody **remove_task()**. Test sprawdza, czy długość listy zadań wynosi 0 po usunięciu zadania. Ponadto test sprawdza, czy przy próbie usunięcia zadania przy użyciu nieprawidłowego indeksu wyświetlany jest komunikat o nieprawidłowym indeksie.

##### test_complete_task()
Ten test sprawdza, czy zadanie zostało wykonane poprawnie. Najpierw dodaje kilka zadań do listy **TaskManager.tasks**, a następnie wywołuje metodę **complete_task()**, aby oznaczyć zadanie jako ukończone. Test sprawdza, czy wyświetlany jest prawidłowy komunikat o ukończeniu zadania dla prawidłowego indeksu i czy wyświetlany jest komunikat o nieprawidłowym indeksie podczas próby ukończenia zadania z nieprawidłowym indeksem.

##### test_view_tasks()
Ten test sprawdza, czy lista zadań jest wyświetlana poprawnie przy użyciu metody **view_tasks()**. Dodaje on kilka zadań do listy **TaskManager.tasks** i sprawdza, czy wyświetlane są prawidłowe linie opisu zadania.

##### test_task_list()
Ten test sprawdza, czy lista zadań jest poprawnie utworzona jako krotki. Dodaje on kilka zadań do listy **TaskManager.tasks**, a następnie sprawdza, czy lista **task_descriptions** odpowiada oczekiwanym zadaniom, które są reprezentowane jako krotki. Test sprawdza, czy krotki z opisami zadań, priorytetem i statusem są poprawnie utworzone.

### [task_save_test.py](/code_part/tests/task_save_test.py)

##### test_save_tasks()
Ten test sprawdza, czy zadania są poprawnie zapisywane do pliku. Najpierw wywołuje metodę **save_tasks()** z klasy **TaskFileManager**, aby zapisać zadania do określonego pliku. Test sprawdza, czy po pomyślnym zapisaniu zadań wyświetlany jest prawidłowy komunikat. Ponadto test sprawdza, czy plik istnieje po zapisaniu.

##### test_load_tasks()
Ten test sprawdza, czy zadania są poprawnie ładowane z pliku. Najpierw wywołuje metodę **save_tasks()** z klasy **TaskFileManager**, aby zapisać zadania w pliku testowym. Następnie wywołuje metodę **load_tasks()**, aby załadować zadania z pliku. Test weryfikuje, czy wczytane zadania mają prawidłowy numer i pasują do oryginalnych zadań pod względem opisu i priorytetu.


## 2.	Część związana z siecią (katalog – [bugbug.io](/bugbug.io))


##### Przetestowałem 5 stron internetowych przy użyciu usługi [bugbug.io](https://bugbug.io/). Przeprowadziłem dwa testy dla każdej witryny. Desktop - rozdzielczość ekranu komputera i Mobile - rozdzielczość ekranu telefonu komórkowego. Dodatkowo przeprowadził testy oparte na kilku elementach: Ogólne wrażenie, Funkcjonalność, Nawigacja, Wyświetlanie, Reakcja na błędy.

Lista stron internetowych:
-	[amazon.com](https://www.amazon.com/)
-	[moodle2.e-wsb.pl](https://moodle2.e-wsb.pl/)
-	[booking.com](https://www.booking.com/)
-	[wikipedia.org](https://www.wikipedia.org/)
-	[tutorialspoint.com](https://www.tutorialspoint.com/)

### Amazon
**Desktop**: 20 kroków testu, 01m 43.31s - czas wykonania testu, wynik - Zaliczony.	<a href="/bugbug.io/Amazon_Desktop.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 5
- Nawigacja - 4
- Wyświetlanie - 4
- Reakcja na błędy - 5

**Mobile** : 23 kroków testu, 01m 09.80s- czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Amazon_Mobile.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 3
- Funkcjonalność - 4
- Nawigacja - 3
- Wyświetlanie - 3
- Reakcja na błędy – 5

### Moodle WSB
**Desktop**: 33 kroków testu, 01m 06.31s - czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Moodle_Desktop.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 5
- Nawigacja - 3
- Wyświetlanie - 4
- Reakcja na błędy - 3

**Mobile** : 18 kroków testu, 01m 02.97s- czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Moodle_Mobile.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 3
- Funkcjonalność - 3
- Nawigacja - 2
- Wyświetlanie - 3
- Reakcja na błędy – 3

### Booking
**Desktop**: 32 kroków testu, 01m 42.24s - czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Booking_Desktop.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 5
- Nawigacja - 4
- Wyświetlanie - 4
- Reakcja na błędy - 3

**Mobile** : 29 kroków testu, 01m 30.88s- czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Booking_Mobile.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 4
- Nawigacja - 4
- Wyświetlanie - 3
- Reakcja na błędy – 3

### Wikipedia
**Desktop**: 17 kroków testu, 00m 40.76s - czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Wikipedia_Desktop.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 5
- Funkcjonalność - 5
- Nawigacja - 4
- Wyświetlanie - 5
- Reakcja na błędy - 5

**Mobile** : 21 kroków testu, 01m 06.77s - czas wykonania testu, wynik - Zaliczony. <a href="/bugbug.io/Wikipedia_Mobile.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 5
- Nawigacja - 4
- Wyświetlanie - 5
- Reakcja na błędy – 5

### Tutorialspoint
**Desktop**: 28 kroków testu, 02m 24.83s - czas wykonania testu, wynik - Zaliczony.  <a href="/bugbug.io/Tutorialspoint_Desktop.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 5
- Nawigacja - 4
- Wyświetlanie - 5
- Reakcja na błędy - 4

**Mobile** : 21 kroków testu, 01m 27.16s - czas wykonania testu, wynik - Nie zaliczony. <a href="/bugbug.io/Tutorialspoint_Mobile.png"><img alt="github" width="3%" style="padding:5px" src="https://img.icons8.com/?size=512&id=114320&format=png"/></a> 
- Ogólne wrażenie - 4
- Funkcjonalność - 4
- Nawigacja - 3
- Wyświetlanie - 4
- Reakcja na błędy – 4

### **Wnioski**

**Jeśli chodzi o same strony i ich funkcjonalność, przeszły one pomyślnie prawie wszystkie testy, nie było żadnych znaczących błędów i mogę śmiało powiedzieć, że zdały test, z wyjątkiem ostatniej (Tutorialspoint), która nie przeszła testu mobilnego. Nie udało mi się znaleźć przyczyny.**

**Jeśli chodzi o usługę bugbug.io, mogę powiedzieć, że nie byłem z niej zadowolony. Szybkość jest słaba, funkcjonalność być może, a dane wynikowe są przeciętne. Testowanie tych stron zajęło mi sporo czasu i nie mogę powiedzieć, że było warto. Było kilka błędów, które mi się nie podobały.**


## 3.   Testy penetracyjne (katalog – [Penetration_Testing](/Penetration_Testing/))

Chciałbym wyrazić moje najszczersze przeprosiny za to, że nie udało mi się ukończyć zadania instalacji wirtualnego środowiska Kali Linux i przeprowadzenia testów penetracyjnych. Ciężko pracowałem, aby zrozumieć i skonfigurować to środowisko w ciągu ostatnich kilku dni, ale niestety nie udało mi się.

Byłem naprawdę zainteresowany tym zadaniem i zamierzałem wrócić do niego później, gdy będę miał więcej czasu i możliwości. Wierzyłem w swoje umiejętności i odwiedziłem różne zasoby, ale problemy z instalacją na moich systemach operacyjnych uniemożliwiły mi osiągnięcie celu.

Chciałbym poprosić ciebie, jako instruktora, o uważne przejrzenie mojej pracy nad poprzednimi zadaniami i docenienie moich wysiłków podczas całego kursu. Starałem się zrozumieć materiał i wykonałem zadania z całą odpowiedzialnością i starannością.

Przepraszam za awarię na tym etapie i liczę na zrozumienie.
