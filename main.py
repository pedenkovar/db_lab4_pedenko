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

with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()

    print('\n2a.')
    cur.execute(query_2a)
    for row in cur:
        print(f'\t{row}')

    print('\n2b.')
    cur.execute(query_2b)
    for row in cur:
        print(f'\t{row}')

    print('\n2c.')
    cur.execute(query_2c)
    for row in cur:
        print(f'\t{row}')
