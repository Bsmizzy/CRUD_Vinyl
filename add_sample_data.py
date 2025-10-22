from app import app, db, Vinyl

sample_records = [
    {
        'title': 'I Let It In and It Took Everything',
        'artist': 'Loathe',
        'year': 2020,
        'genre': 'Rock',
        'condition': 'Mint'
    },
    {
        'title': 'The Cold Sun',
        'artist': 'Loathe',
        'year': 2017,
        'genre': 'Rock',
        'condition': 'Near Mint'
    },
    {
        'title': 'Take Me Back to Eden',
        'artist': 'Sleep Token',
        'year': 2023,
        'genre': 'Rock',
        'condition': 'Mint'
    },
    {
        'title': 'This Place Will Become Your Tomb',
        'artist': 'Sleep Token',
        'year': 2021,
        'genre': 'Rock',
        'condition': 'Mint'
    },
    {
        'title': 'Sundowning',
        'artist': 'Sleep Token',
        'year': 2019,
        'genre': 'Rock',
        'condition': 'Very Good'
    },
    {
        'title': 'Nothing Left to Love',
        'artist': 'Counterparts',
        'year': 2019,
        'genre': 'Rock',
        'condition': 'Near Mint'
    },
    {
        'title': 'You\'re Not You Anymore',
        'artist': 'Counterparts',
        'year': 2017,
        'genre': 'Rock',
        'condition': 'Very Good'
    },
    {
        'title': 'Tragedy Will Find Us',
        'artist': 'Counterparts',
        'year': 2015,
        'genre': 'Rock',
        'condition': 'Good'
    },
    {
        'title': 'The Difference Between Hell and Home',
        'artist': 'Counterparts',
        'year': 2013,
        'genre': 'Rock',
        'condition': 'Good'
    },
    {
        'title': 'The Current Will Carry Us',
        'artist': 'Counterparts',
        'year': 2011,
        'genre': 'Rock',
        'condition': 'Fair'
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
