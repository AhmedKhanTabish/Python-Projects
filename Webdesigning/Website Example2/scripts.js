document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    alert('Thank you for your message! We will get back to you soon.');

    // You can replace this with your own code to send the message to your email or a server.
    // For example, you can use the Fetch API to send the data to a server.
});