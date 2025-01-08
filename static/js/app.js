// app.js

document.addEventListener('DOMContentLoaded', function () {
    // Example: Toggle password visibility
    const passwordField = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');

    if (togglePassword) {
        togglePassword.addEventListener('click', function () {
            const type = passwordField.type === 'password' ? 'text' : 'password';
            passwordField.type = type;
            this.classList.toggle('fa-eye-slash');
        });
    }

    // Example: Form validation
    const form = document.getElementById('registrationForm');
    if (form) {
        form.addEventListener('submit', function (event) {
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (!username || !email || !password) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }
});
