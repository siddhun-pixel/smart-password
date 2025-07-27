const passwordInput = document.getElementById("password");
const strengthFill = document.getElementById("strength-fill");
const resultText = document.getElementById("result-text");

passwordInput.addEventListener("input", () => {
  const password = passwordInput.value;
  const strength = calculateStrength(password);

  // Update strength bar based on score
  strengthFill.className = "strength-fill"; // Reset
  if (strength === 0) {
    strengthFill.style.width = "0%";
    resultText.textContent = "";
  } else if (strength <= 2) {
    strengthFill.classList.add("weak");
    resultText.textContent = "Weak Password";
  } else if (strength === 3) {
    strengthFill.classList.add("medium");
    resultText.textContent = "Medium Strength";
  } else {
    strengthFill.classList.add("strong");
    resultText.textContent = "Strong Password";
  }
});

// Function to calculate strength
function calculateStrength(password) {
  let score = 0;
  if (password.length >= 8) score++;
  if (/[a-z]/.test(password)) score++;
  if (/[A-Z]/.test(password)) score++;
  if (/\d/.test(password)) score++;
  if (/[\W_]/.test(password)) score++;

  if (password.length === 0) return 0;
  if (score <= 2) return 1;
  if (score === 3) return 3;
  return 4;
}
