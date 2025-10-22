from app import app, db, Vinyl

sample_records = [
    {
        'title': 'Abbey Road',
        'artist': 'The Beatles',
        'year': 1969,
        'genre': 'Rock',
        'condition': 'Near Mint'
    },
    {
        'title': 'Thriller',
        'artist': 'Michael Jackson',
        'year': 1982,
        'genre': 'Pop',
        'condition': 'Very Good'
    },
    {
        'title': 'Dark Side of the Moon',
        'artist': 'Pink Floyd',
        'year': 1973,
        'genre': 'Rock',
        'condition': 'Mint'
    },
    {
        'title': 'Kind of Blue',
        'artist': 'Miles Davis',
        'year': 1959,
        'genre': 'Jazz',
        'condition': 'Good'
    },
    {
        'title': 'Rumours',
        'artist': 'Fleetwood Mac',
        'year': 1977,
        'genre': 'Rock',
        'condition': 'Very Good'
    },
    {
        'title': 'Back in Black',
        'artist': 'AC/DC',
        'year': 1980,
        'genre': 'Rock',
        'condition': 'Near Mint'
    },
    {
        'title': 'The Miseducation of Lauryn Hill',
        'artist': 'Lauryn Hill',
        'year': 1998,
        'genre': 'Hip-Hop',
        'condition': 'Mint'
    },
    {
        'title': 'Blue Train',
        'artist': 'John Coltrane',
        'year': 1957,
        'genre': 'Jazz',
        'condition': 'Fair'
    },
    {
        'title': 'Random Access Memories',
        'artist': 'Daft Punk',
        'year': 2013,
        'genre': 'Electronic',
        'condition': 'Mint'
    },
    {
        'title': 'Blonde on Blonde',
        'artist': 'Bob Dylan',
        'year': 1966,
        'genre': 'Rock',
        'condition': 'Good'
    }
]

def add_sample_records():
    with app.app_context():
        existing = Vinyl.query.count()
        if existing > 0:
            print(f"Database has {existing} records.")
            if input("Add samples anyway? (y/n): ").lower() != 'y':
                return
        
        for record in sample_records:
            db.session.add(Vinyl(**record))
        
        db.session.commit()
        print(f"Added {len(sample_records)} records.")

if __name__ == '__main__':
    add_sample_records()
