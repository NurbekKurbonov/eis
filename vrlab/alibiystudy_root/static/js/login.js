const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#passwordField');

const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField");
const stirField = document.querySelector("#stirField");

const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const stirFeedBackArea = document.querySelector(".stirFeedBackArea");
const passwordFeedBackArea = document.querySelector(".passwordFeedBackArea");
const passwordField = document.querySelector("#passwordField");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");

const submitBtn = document.querySelector(".submit-btn");

togglePassword.addEventListener('click', function (e) {
  // toggle the type attribute
  const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
  password.setAttribute('type', type);
  // toggle the eye slash icon
  this.classList.toggle('fa-eye-slash');
});

passwordField.addEventListener("keyup", (e) => {
  const passwordVal = e.target.value;

  passwordField.classList.remove("is-invalid");
  passwordFeedBackArea.style.display = "none";

  if (passwordVal.length > 0) {
    fetch("/validate-password", {
      body: JSON.stringify({ password: passwordVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.password_error) {
          submitBtn.disabled = true;
          passwordField.classList.add("is-invalid");
          passwordFeedBackArea.style.display = "block";
          passwordFeedBackArea.innerHTML = `<p>${data.password_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

stirField.addEventListener("keyup", (e) => {
  const stirVal = e.target.value;

  stirField.classList.remove("is-invalid");
  stirFeedBackArea.style.display = "none";

  if (stirVal.length > 0) {
    fetch("/validate-stir", {
      body: JSON.stringify({ stir: stirVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.stir_error) {
          submitBtn.disabled = true;
          stirField.classList.add("is-invalid");
          stirFeedBackArea.style.display = "block";
          stirFeedBackArea.innerHTML = `<p>${data.stir_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;

  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.email_error) {
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;

  usernameSuccessOutput.style.display = "block";

  usernameSuccessOutput.textContent = `Tekshirilyapti...  ${usernameVal}`;

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        usernameSuccessOutput.style.display = "none";
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});