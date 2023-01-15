# Objetivo

Experimentar diversas [queries de Django](https://docs.djangoproject.com/en/4.1/topics/db/queries/)

Para ello requeriremos de cargar data a un modelo de nuestra aplicación de Django.

## Data

Utilizaremos una colección de 11127 libros:

-   [Link de archivo en formato csv](https://gist.github.com/silabuz/aeb1d4cc56bf68442011027dee3d7150).
-   [Link de archivo en formato json](https://gist.github.com/silabuz/17e9c5ff2a0c2d716c1065c2f179174a)
- [Link api](https://silabuzinc.github.io/books/books.json)

Realizar el modelo en base al modelado requerido para los libros. Posteriormente realizar la carga de datos con el comando **loaddata**

```shell
python manage.py loaddata books
```

Analizar y evaluar los campos para el correcto procedimiento de importación.

## Uso opcional de ipython
Para facilitar la experimentación de nuestros modelos en el shell puede instalar ipython:

[Link de instrucciones, instalación y alcance](https://github.com/silabuzinc/django-first-steps/blob/main/docs/django-shell.md#uso-opcional-de-ipython)

# Consultas a realizar

Por cada consulta de ser posible genere una vista, en su defecto agrupe las relacionadas.

1.  Filtre los libros publicados después del 2007.
2.  Contabilice el total de libros publicados después del 2007 por año.
3.  Filtre los tipos de libros cuyo ratings estén entre 3.5 y 4.2
4.  Muestre los libros cuyos títulos en longitud estén en el top 20.
5.  Del punto anterior, respecto al rating del libro indicar el valor menor, el mayor valor, el promedio así como la desviación estándar.
6.  Filtre libros con número dé páginas mayores a 400 y con rating mayor a 3.9. Presente el resultado ordenado alfabéticamente por el título.
7.  Ordernar los libros descendentemente por el número de páginas y el isbn.
8.  Listar los libros cuya editora (publisher) contenga la palabra "Books" o "'Audio".
9.  Filtrar los libros con rating menor a 3.5, excluyendo a los que pertenezcan a las siguientes editoras `Vintage`, `Cambridge University Press` y `Cambridge University Press`. Ordenar el resultado descendentemente por número de reseñas (text_reviews_count).
10.  Mostrar todos los libros publicados entre los meses de Mayo a Agosto, Ordenarlos descendentemente por el rating.

# Extra

Adicionar bootstrap a nuestro proyecto de Django

