from app import db

# المؤلف
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# الناشر
class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100))

# الكتاب
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    publish_date = db.Column(db.String(50))
    topic = db.Column(db.Text)
    total_copies = db.Column(db.Integer)
    is_useful = db.Column(db.String(1))  # 'Y' or 'N'
    suitable_age = db.Column(db.String(20))

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

    author = db.relationship('Author', backref='books')
    publisher = db.relationship('Publisher', backref='books')

# معلومات الحظر
class BanInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text)
    danger_level = db.Column(db.String(10))  # مثلاً: Low / Medium / High
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    book = db.relationship('Book', backref='baninfo')

# اللغة
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

# لغات الكتاب (جدول وسيط)
class BookLanguage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))

    book = db.relationship('Book', backref='book_languages')
    language = db.relationship('Language', backref='book_languages')

# البلدان المحظور فيها الكتاب
class CountryBan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    book = db.relationship('Book', backref='banned_countries')
