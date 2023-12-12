--Кількість книг, написаних кожним автором
select author.name, count(author_book.isbn) as book_count
    from author
    left join author_book on author.id_author = author_book.id_author
    group by author.name
    order by book_count desc;
	
--Загальна кількість текстових рецензій в залежності від мови	
select book.language, sum(review.text_reviews_count) as total_text_reviews
from book
left join review on book.isbn = review.isbn
group by book.language;

--Кількість книг кожною мовою
select language, count(*) as book_count
	from book
	left join review on book.isbn = review.isbn
	group by language;
	



