function hamburg() {
    const navbar = document.querySelector(".dropdown");
    if (navbar) {
        navbar.style.transform = "translateY(0px)";
    }
}

function cancel() {
    const navbar = document.querySelector(".dropdown");
    if (navbar) {
        navbar.style.transform = "translateY(-500px)";
    }
}

// for Typewriter effect
const texts = [
    "AI ENGINEER",
    "CYBERSECURITY ANALYST",
    "DIGITAL FORENSICS SPECIALIST",
    "WEB & AI AUTOMATION SPECIALIST"
];

let speed = 100;
let textIndex = 0;
let charcterIndex = 0;

function typeWriter() {
    const textElements = document.querySelector(".typewriter-text");
    if (!textElements) return;

    if (charcterIndex < texts[textIndex].length) {
        textElements.innerHTML += texts[textIndex].charAt(charcterIndex);
        charcterIndex++;
        setTimeout(typeWriter, speed);
    } else {
        setTimeout(eraseText, 1200);
    }
}

function eraseText() {
    const textElements = document.querySelector(".typewriter-text");
    if (!textElements) return;

    if (textElements.innerHTML.length > 0) {
        textElements.innerHTML = textElements.innerHTML.slice(0, -1);
        setTimeout(eraseText, 50);
    } else {
        textIndex = (textIndex + 1) % texts.length;
        charcterIndex = 0;
        setTimeout(typeWriter, 500);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    const textElements = document.querySelector(".typewriter-text");
    if (textElements) {
        typeWriter();
    }
});

// CV Download functionality
function downloadCV() {
    const link = document.createElement("a");
    link.href = "assets/Cv_Eman_Fatima.pdf";
    link.download = "Cv_Eman_Fatima.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
