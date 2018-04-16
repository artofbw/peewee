from datetime import date

import peewee


db = peewee.SqliteDatabase('database.db')


class Author(peewee.Model):
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    age = peewee.IntegerField(null=True)

    class Meta:
        database = db

    def __str__(self):
        return '{} {} ({})'.format(
            self.first_name,
            self.last_name,
            self.age,
        )


class Book(peewee.Model):
    title = peewee.CharField()
    published_at = peewee.DateField()
    author = peewee.ForeignKeyField(Author, backref='books')

    class Meta:
        database = db

    def __str__(self):
        return '{}'.format(self.title)


db.drop_tables([Author, Book])
db.create_tables([Author, Book])

Author.create(first_name='Jan', last_name='Kowalski', age=20)
Author.create(first_name='Mariusz', last_name='Test', age=30)
Author.create(first_name='Mikołaj', last_name='Santa', age=120)

authors = Author.select()

Book.create(
    title="W pustyni i w puszczy",
    published_at=date(2016, 1, 1),
    author_id=authors[1]
)
Book.create(
    title="Janko Muzykant",
    published_at=date(2016, 1, 1),
    author_id=authors[1]
)


# for author in authors:
#     print(author)
#
#     for book in author.books:
#         print('--->', book)
#
    # for book in Book.select().where(Book.author == author):
    #     print('--->', book)


print('Authors count: {}'.format(Author.select().count()))

# authors[0].delete_instance()
# Author.delete_by_id(1)

print('Authors count: {}'.format(Author.select().count()))

author = Author.select().where(Author.id==3)[0]
print(author)
author.first_name = 'Bob'
author.last_name = 'Marley'
print(author)

author.save()
