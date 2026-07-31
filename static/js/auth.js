// ===============================
// Show / Hide Password
// ===============================

document.querySelectorAll(".toggle-password").forEach(toggle => {

    toggle.addEventListener("click", function () {

        const input = this.previousElementSibling;
        const icon = this.querySelector("i");

        if (input.type === "password") {

            input.type = "text";

            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");

        } else {

            input.type = "password";

            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");

        }

    });

});


// ===============================
// Password Strength Meter
// ===============================

const password = document.getElementById("password");

const strengthBar = document.querySelector(".strength-bar");

const strengthText = document.querySelector(".strength small");

if (password && strengthBar && strengthText) {

    password.addEventListener("input", function () {

        const value = this.value;

        let score = 0;

        if (value.length >= 8) score++;
        if (/[A-Z]/.test(value)) score++;
        if (/[0-9]/.test(value)) score++;
        if (/[^A-Za-z0-9]/.test(value)) score++;

        if (score === 1) {

            strengthBar.style.width = "25%";
            strengthBar.style.background = "#ef4444";
            strengthText.innerHTML = "Weak Password";

        }

        else if (score === 2) {

            strengthBar.style.width = "50%";
            strengthBar.style.background = "#f59e0b";
            strengthText.innerHTML = "Medium Password";

        }

        else if (score === 3) {

            strengthBar.style.width = "75%";
            strengthBar.style.background = "#3b82f6";
            strengthText.innerHTML = "Good Password";

        }

        else if (score === 4) {

            strengthBar.style.width = "100%";
            strengthBar.style.background = "#22c55e";
            strengthText.innerHTML = "Strong Password";

        }

        else {

            strengthBar.style.width = "0%";
            strengthText.innerHTML = "Password Strength";

        }

    });

}


// ===============================
// Button Loading Effect
// ===============================

document.querySelectorAll("form").forEach(form => {

    form.addEventListener("submit", function () {

        const btn = this.querySelector(".auth-btn");

        if (btn) {

            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Please Wait...';

            btn.disabled = true;

        }

    });

});