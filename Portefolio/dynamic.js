document.addEventListener("DOMContentLoaded", () => {
    const section = document.querySelector(".education-section");

    // IntersectionObserver pour détecter l'apparition
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    section.classList.add("animate"); // Applique l'effet
                   
                }
            });
        },
        { threshold: 0.3 } // Déclenche à 30% de visibilité
    );

    observer.observe(section);

    // Gestion des clics sur les liens
    const navLinks = document.querySelectorAll(".nav-link");
    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetElement = document.querySelector(targetId);

            // Défilement fluide
            targetElement.scrollIntoView({
                behavior: "smooth",
                block: "center",
            });

            // Relancer l'animation au clic
            setTimeout(() => {
                targetElement.classList.add("animate");
                setTimeout(() => {
                    targetElement.classList.remove("animate");
                }, 1000); // Durée de l'animation
            }, 500); // Délai pour que le défilement soit terminé
        });
    });
});








document.addEventListener("DOMContentLoaded", () => {
    const professionalSection = document.querySelector(".experience-section");

    // Observer pour détecter l'apparition dans la fenêtre d'affichage
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("animate");
                    observer.unobserve(entry.target); // Stoppe l'observation après l'animation
                }
            });
        },
        { threshold: 0.3 } // Animation déclenchée quand 30% de l'élément est visible
    );

    observer.observe(professionalSection);

    // Gestion des clics sur les liens de navigation
    const navLinks = document.querySelectorAll(".nav-link");
    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetElement = document.querySelector(targetId);

            // Défilement fluide
            targetElement.scrollIntoView({
                behavior: "smooth",
                block: "center",
            });

            // Applique l'animation au clic (sans la retirer après)
            targetElement.classList.add("animate");
        });
    });
});
