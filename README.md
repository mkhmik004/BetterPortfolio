# Web Portfolio with Email Server Backend

## Introduction

This project features a professional web portfolio with an email server backend for the contact page. The email server acts as a middleman between the website and my Gmail email account, allowing users to submit data through a web form on my contact page. The server sends an email with the submitted data to my email account and sends a CC to the author of the email, facilitating a conversation thread under one subject.

## Video Demo

- URL: `<URL HERE>`

The video demo showcases how the web portfolio and email server work together, including handling form submissions, sending automated replies, and keeping communication threads organized.

## Installation

### Dependencies

- Ensure you have Python 3.x installed.
- Install the required libraries using pip:

    ```bash
    pip install flask flask-mail flask-wtf python-dotenv flask-cors
    ```

### Setting up the project

1. Create a `.env` file in the root directory of your project and include the following variables:
    ```plaintext
    MAIL_USERNAME=your_email@gmail.com
    MAIL_PASSWORD=your_email_password
    SECRET_KEY=your_secret_key
    ```

2. Run the server using the following command:

    ```bash
    python app.py
    ```

## Configuration

- **Mail settings**: The server connects to the Gmail SMTP server to send emails. Ensure that `MAIL_SERVER`, `MAIL_PORT`, and other configurations match your Gmail account.

## Usage

### `/contact` Endpoint

- **Method**: POST
- **Purpose**: Handles form submissions from your website's contact page and sends emails.
  
- **Request Body**: Form data including:
    - `name`: The name of the person submitting the form.
    - `email`: The email address of the person submitting the form.
    - `subject`: The subject of the email.
    - `message`: The message to be sent.
    - `csrf_token`: The CSRF token obtained from the server.

- **Response**:
    - **Success**: Returns a flash with a message indicating the email was sent successfully.
    - **Error**: Returns a flash with an error message indicating why the form submission failed.

## Error Handling

The server handles errors and exceptions gracefully and returns appropriate error messages as JSON objects.

## Conclusion

This project combines a web portfolio with an email server backend for the contact page. The integration provides a convenient and secure way to facilitate communication between your website's visitors and yourself through email. By handling form submissions and sending emails, the server streamlines the process of connecting with you.
