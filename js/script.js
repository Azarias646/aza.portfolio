//Génération de texte
const texts = [
    "<! BIENVENUE dans mon portfolio!",
    "Je me nomme AZARIAS SAWADOGO",
    "Je suis développeur informatique",
    "Merci de votre visite",
    "et bonne navigation! />"
];
let textIndex = 0;
let charIndex = 0;

function typeText() {
    if (textIndex < texts.length) {
        if (charIndex < texts[textIndex].length) {
            document.getElementById("animated-text").innerHTML += texts[textIndex].charAt(charIndex);
            charIndex++;
            setTimeout(typeText, 100);
        } else {
            charIndex = 0;
            textIndex++;
            setTimeout(() => {
                document.getElementById("animated-text").innerHTML += "<br><br>";
                typeText();
            }, 250);
        }
    }
}

window.onload = typeText;


//Theme
const toggleButton = document.getElementById('theme-toggle');

// Ajoute un écouteur d'événement au clic
toggleButton.addEventListener('click', () => {
    // Bascule entre les classes 'light-theme' et 'dark-theme' sur le corps de la page
    document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('light-theme');

    // Change le texte du bouton selon le thème actif
    if (document.body.classList.contains('dark-theme')) {
        toggleButton.textContent = "🌙";
    } else {
        toggleButton.textContent = "☀️";
    }
});

// Définit le thème jour par défaut au chargement de la page
document.body.classList.add('dark-theme');



//Défilement des cartes
$(document).ready(function() {
    $('#autoWidth').lightSlider({
        auto:true,
        autoWidth:true,
        loop:true,
        item:1,
        pauseOnHover:true,
        onSliderLoad: function() {
            $('#autoWidth').removeClass('cS-hidden');
        } 
    });  
});


// Sélectionner toutes les vidéos avec la classe "hover-video"
/*const videos = document.querySelectorAll(".hover-video");

// Ajouter un écouteur d'événement pour le survol
videos.forEach(video => {
    video.addEventListener("mouseover", () => {
        video.play(); // Démarre la lecture
    });

    video.addEventListener("mouseout", () => {
        video.pause(); // Met la lecture en pause
    });
});*/
