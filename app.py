from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vinyl_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Vinyl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100))
    condition = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Vinyl {self.title} by {self.artist}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        artist = request.form.get('artist', '').strip()
        year = request.form.get('year', '').strip()
        genre = request.form.get('genre', '').strip()
        condition = request.form.get('condition', '').strip()
        
        if not title or not artist or not year:
            flash('Title, Artist, and Year are required.', 'error')
        else:
            try:
                year_int = int(year)
                if year_int < 1900 or year_int > 2025:
                    flash('Year must be between 1900 and 2025.', 'error')
                else:
                    new_vinyl = Vinyl(
                        title=title,
                        artist=artist,
                        year=year_int,
                        genre=genre if genre else None,
                        condition=condition if condition else None
                    )
                    db.session.add(new_vinyl)
                    db.session.commit()
                    flash('Vinyl record added.', 'success')
                    return redirect(url_for('index'))
            except ValueError:
                flash('Year must be a valid number.', 'error')
    
    vinyls = Vinyl.query.order_by(Vinyl.date_added.desc()).all()
    return render_template('index.html', vinyls=vinyls)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_vinyl(id):
    vinyl = Vinyl.query.get_or_404(id)
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        artist = request.form.get('artist', '').strip()
        year = request.form.get('year', '').strip()
        genre = request.form.get('genre', '').strip()
        condition = request.form.get('condition', '').strip()
        
        if not title or not artist or not year:
            flash('Title, Artist, and Year are required.', 'error')
        else:
            try:
                year_int = int(year)
                if year_int < 1900 or year_int > 2025:
                    flash('Year must be between 1900 and 2025.', 'error')
                else:
                    vinyl.title = title
                    vinyl.artist = artist
                    vinyl.year = year_int
                    vinyl.genre = genre if genre else None
                    vinyl.condition = condition if condition else None
                    
                    db.session.commit()
                    flash('Vinyl record updated.', 'success')
                    return redirect(url_for('index'))
            except ValueError:
                flash('Year must be a valid number.', 'error')
    
    return render_template('update.html', vinyl=vinyl)


@app.route('/delete/<int:id>')
def delete_vinyl(id):
    vinyl = Vinyl.query.get_or_404(id)
    db.session.delete(vinyl)
    db.session.commit()
    flash('Vinyl record deleted.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
