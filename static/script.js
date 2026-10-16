document.addEventListener("DOMContentLoaded", function () {

    // Typing effect
    const text = "Python Full Stack Developer";
    let index = 0;
    const heading = document.querySelector(".hero h2");

    heading.textContent = "";

    function typeEffect() {
        if (index < text.length) {
            heading.textContent += text.charAt(index);
            index++;
            setTimeout(typeEffect, 100);
        }
    }

    typeEffect();

});