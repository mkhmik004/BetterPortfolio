# Flask imports
from flask import render_template, request, redirect, url_for, flash

# WTForms imports
from .forms import ContactForm  # Import the ContactForm from the forms module

# Flask-Mail imports
from flask_mail import Message,Mail

# Define routes using the imported Flask application instance
def register_routes(app):
    mail = Mail(app)
    @app.route("/", methods=['GET'])
    def home():
        return render_template("index.html",current_page='home')

    @app.route("/projects", methods=['GET'])
    def projects():
        return render_template("portfolio.html",current_page='projects')

    @app.route("/education", methods=['GET'])
    def education():
        return render_template("resume.html",current_page='education')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message = form.message.data

            msg = Message(subject=subject, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[app.config['MAIL_DEFAULT_SENDER'], email])
            msg.body = f"Hi Mr/Ms {name},\n\nThank you for contacting me.\n\nSubject: {subject}\nMessage: {message}\n\nRegards,\nMMM Mkhabele."

            try:
                mail.send(msg)
                flash('Your Email has been sent successfully to Mr MMM Mkhabele!', 'success')
                return redirect(url_for('contact'))
            except Exception as e:
                 flash(f'Error sending Email to Mr MMM Mkhabele!: {str(e)}', 'warning')
                 return redirect(url_for('contact'))

        return render_template('contact.html', form=form,current_page='contact')










