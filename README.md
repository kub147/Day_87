# Breakout Game

Gra Breakout napisana w Pythonie przy użyciu biblioteki Turtle. Celem gry jest odbijanie piłki za pomocą platformy i niszczenie cegieł.

## Jak uruchomić grę?
1. Upewnij się, że masz zainstalowanego Pythona (wersja 3.6 lub nowsza).
2. Pobierz pliki projektu.
3. Zainstaluj wymagane zależności:
   ```bash
   pip install pygame
   ```
4. Uruchom plik `breakout.py`:
   ```bash
   python breakout.py
   ```

## Sterowanie
- **Strzałka w lewo (`←`)** – przesuwa platformę w lewo
- **Strzałka w prawo (`→`)** – przesuwa platformę w prawo
- **R** – restartuje grę

## Zasady gry
- Gracz odbija piłkę platformą, aby niszczyć cegły.
- Każda cegła ma swój kolor i odpowiadający jej dźwięk.
- Gdy piłka uderza w platformę, jej prędkość stopniowo wzrasta.
- Jeżeli piłka spadnie poniżej ekranu, zwiększa się licznik upadków.
- Gdy wszystkie cegły zostaną zniszczone, wyświetli się komunikat o wygranej i otworzy się link do YouTube.

## Funkcjonalności
- **Losowy układ cegieł** – cegły są rozmieszczone w pięciu rzędach o różnych kolorach.
- **Efekty dźwiękowe** – każdy kolor cegły ma przypisany inny dźwięk.
- **Zmienna prędkość piłki** – po każdym odbiciu od platformy piłka przyspiesza.
- **Licznik upadków** – śledzi, ile razy piłka spadła poniżej platformy.
- **Wyświetlanie prędkości piłki i liczby upadków**.


## Licencja
Projekt jest udostępniony na licencji MIT. Możesz go dowolnie modyfikować i wykorzystywać.
