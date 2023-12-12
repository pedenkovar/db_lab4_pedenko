import matplotlib.pyplot as plt
import psycopg2

username = 'Pedenko_Varvara'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_2a = """
        select author.name, count(author_book.isbn) as book_count
        from author
        left join author_book on author.id_author = author_book.id_author
        group by author.name
        order by book_count desc;
    """

query_2b = """
        select book.language, sum(review.text_reviews_count) as total_text_reviews
        from book
        left join review on book.isbn = review.isbn
        group by book.language;
    """

query_2c = """
        select language, count(*) as book_count
	    from book
	    left join review on book.isbn = review.isbn
	    group by language;
    """
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn, conn.cursor() as cursor:
    cursor.execute(query_2a)
    data_2a = cursor.fetchall()

authors = [row[0] for row in data_2a]
book_counts = [row[1] for row in data_2a]

plt.figure(figsize=(10, 6))
plt.bar(authors, book_counts)
plt.xlabel('Автор')
plt.ylabel('Кількість книг')
plt.title('Кількість книг, написаних кожним автором')
plt.xticks(rotation=45, ha='right')
plt.show()


with conn, conn.cursor() as cursor:
    cursor.execute(query_2b)
    data_2b = cursor.fetchall()

languages = [row[0] for row in data_2b]
total_text_reviews = [row[1] for row in data_2b]

plt.figure(figsize=(8, 8))
plt.pie(total_text_reviews, labels=languages, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Загальна кількість текстових рецензій в залежності від мови')
plt.show()


with conn, conn.cursor() as cursor:
    cursor.execute(query_2c)
    data_2c = cursor.fetchall()

languages_2c = [row[0] for row in data_2c]
book_count_2c = [row[1] for row in data_2c]

plt.figure(figsize=(10, 6))
plt.plot(languages_2c, book_count_2c, marker='o', linestyle='-', color='green')
plt.xlabel('Мова')
plt.ylabel('Кількість книг')
plt.title('Кількість книг кожною мовою')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()