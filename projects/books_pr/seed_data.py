from app import create_app, db
from app.model import Book, Author, Publisher, BanInfo, Language, BookLanguage, CountryBan

def seed_database():
    app = create_app()
    with app.app_context():
        # Create authors
        authors = [
            Author(name="Salman Rushdie"),
            Author(name="George Orwell"),
            Author(name="Mark Twain"),
            Author(name="J.K. Rowling"),
            Author(name="Harper Lee"),
            Author(name="Aldous Huxley"),
            Author(name="Margaret Atwood"),
            Author(name="Ray Bradbury"),
            Author(name="Kurt Vonnegut"),
            Author(name="James Joyce")
        ]
        db.session.add_all(authors)

        # Create publishers
        publishers = [
            Publisher(name="Penguin Books", country="UK"),
            Publisher(name="HarperCollins", country="USA"),
            Publisher(name="Random House", country="USA"),
            Publisher(name="Bloomsbury", country="UK"),
            Publisher(name="Vintage Books", country="USA")
        ]
        db.session.add_all(publishers)

        # Create languages
        languages = [
            Language(name="English"),
            Language(name="Arabic"),
            Language(name="French"),
            Language(name="Spanish"),
            Language(name="German")
        ]
        db.session.add_all(languages)

        # Create books with their ban information
        books = [
            Book(
                title="The Satanic Verses",
                publish_date="1988",
                topic="Religious controversy and magical realism",
                total_copies=1000,
                is_useful="Y",
                suitable_age="18+",
                author=authors[0],
                publisher=publishers[0]
            ),
            Book(
                title="1984",
                publish_date="1949",
                topic="Dystopian political fiction",
                total_copies=2000,
                is_useful="Y",
                suitable_age="16+",
                author=authors[1],
                publisher=publishers[1]
            ),
            Book(
                title="The Adventures of Huckleberry Finn",
                publish_date="1884",
                topic="Coming of age story",
                total_copies=1500,
                is_useful="Y",
                suitable_age="14+",
                author=authors[2],
                publisher=publishers[2]
            ),
            Book(
                title="Harry Potter and the Philosopher's Stone",
                publish_date="1997",
                topic="Fantasy fiction",
                total_copies=5000,
                is_useful="Y",
                suitable_age="10+",
                author=authors[3],
                publisher=publishers[3]
            ),
            Book(
                title="To Kill a Mockingbird",
                publish_date="1960",
                topic="Racial injustice",
                total_copies=3000,
                is_useful="Y",
                suitable_age="14+",
                author=authors[4],
                publisher=publishers[1]
            ),
            Book(
                title="Brave New World",
                publish_date="1932",
                topic="Dystopian science fiction",
                total_copies=1800,
                is_useful="Y",
                suitable_age="16+",
                author=authors[5],
                publisher=publishers[0]
            ),
            Book(
                title="The Handmaid's Tale",
                publish_date="1985",
                topic="Dystopian fiction",
                total_copies=2200,
                is_useful="Y",
                suitable_age="16+",
                author=authors[6],
                publisher=publishers[2]
            ),
            Book(
                title="Fahrenheit 451",
                publish_date="1953",
                topic="Dystopian science fiction",
                total_copies=2500,
                is_useful="Y",
                suitable_age="14+",
                author=authors[7],
                publisher=publishers[1]
            ),
            Book(
                title="Slaughterhouse-Five",
                publish_date="1969",
                topic="Anti-war science fiction",
                total_copies=1200,
                is_useful="Y",
                suitable_age="16+",
                author=authors[8],
                publisher=publishers[2]
            ),
            Book(
                title="Ulysses",
                publish_date="1922",
                topic="Modernist literature",
                total_copies=800,
                is_useful="Y",
                suitable_age="18+",
                author=authors[9],
                publisher=publishers[0]
            )
        ]
        db.session.add_all(books)

        # Create ban information
        ban_info = [
            BanInfo(
                reason="Religious controversy and blasphemy",
                danger_level="High",
                book=books[0]
            ),
            BanInfo(
                reason="Political content and surveillance themes",
                danger_level="Medium",
                book=books[1]
            ),
            BanInfo(
                reason="Racial language and stereotypes",
                danger_level="Medium",
                book=books[2]
            ),
            BanInfo(
                reason="Alleged promotion of witchcraft",
                danger_level="Low",
                book=books[3]
            ),
            BanInfo(
                reason="Racial themes and language",
                danger_level="Medium",
                book=books[4]
            ),
            BanInfo(
                reason="Sexual content and drug use",
                danger_level="Medium",
                book=books[5]
            ),
            BanInfo(
                reason="Sexual content and religious themes",
                danger_level="Medium",
                book=books[6]
            ),
            BanInfo(
                reason="Anti-censorship themes",
                danger_level="Low",
                book=books[7]
            ),
            BanInfo(
                reason="War themes and sexual content",
                danger_level="Medium",
                book=books[8]
            ),
            BanInfo(
                reason="Explicit sexual content",
                danger_level="High",
                book=books[9]
            )
        ]
        db.session.add_all(ban_info)

        # Create book languages
        for book in books:
            book_language = BookLanguage(book=book, language=languages[0])  # English
            db.session.add(book_language)

        # Create country bans
        banned_countries = [
            CountryBan(country_name="Iran", book=books[0]),
            CountryBan(country_name="Saudi Arabia", book=books[0]),
            CountryBan(country_name="China", book=books[1]),
            CountryBan(country_name="Russia", book=books[1]),
            CountryBan(country_name="USA", book=books[2]),
            CountryBan(country_name="UAE", book=books[3]),
            CountryBan(country_name="USA", book=books[4]),
            CountryBan(country_name="Ireland", book=books[5]),
            CountryBan(country_name="USA", book=books[6]),
            CountryBan(country_name="USA", book=books[7]),
            CountryBan(country_name="USA", book=books[8]),
            CountryBan(country_name="USA", book=books[9])
        ]
        db.session.add_all(banned_countries)

        # Commit all changes
        db.session.commit()

if __name__ == '__main__':
    seed_database() 