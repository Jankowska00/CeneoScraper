# CeneoScraper11S

## Etap 1 - pobranie pojedynczej opinii 
- opinia : div.js-product-review
- identyfikator : li.review-box["data-entry-id"]
- autor : div.reviewer-name-line
- rekomendacja : div.product-review-summary > em
- liczba gwiazdek : span.review-score-count
- czy potwierdzona zakupem : div.product-review-pz
- data wystawienia : span.review-time > time ["datetime"] - pierwsze wystąpienie
- data zakupu : span.review-time > time ["datetime"] - drugie wystąpienie
- przydatna : button.votes-yes["data-total-vote"]
- nieprzydatna : button.votes-no["data-total-vote"]
- treść : p.product-review-body
- wady : div.cons-cell > ul
- zalety : div.pros-cell > ul

## Etap 2 - pobranie wszystkich opinii z pojedynczej strony
- zapis składowych opinii do złożonej struktury danych

## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- sposób przechodzenia po kolejnych stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json)

## Etap 4 - refaktoryzacja kodu 
- eliminacja powtarzających się fragmentów kodu
- transformacja danych (typ danych, czyszczenie danych)

## Etap 5 - analiza pobranych danych
- zapis pobranych danych do obiektu dataframe (ramka danych)
- wykonanie prostych obliczeń na danych
- wykonanie prostych wykresów

## Etap 6 - interfejs webowy aplikacji (framework Flask)
- zainstalowanie i uruchamianie Flask'a
- routing (nawigowanie po stronach serwisu)
- struktura aplikacji
    /CeneoScraper
        /run.py
        /config.py
        /app
            /\_\_init\_\_.py
            /routes.py
            /models.py
            /forms.py
            /scraper.py
            /analyzer.py
            /static/
                /main.csss
                /figures/
                    /fig.png
            /templates/
                /base.html
            /opinions
            /requirements.txt
            /.venv
            /README.md
- routing (nawigowanie po stronach serwisu)
- widoki (Jinja)
