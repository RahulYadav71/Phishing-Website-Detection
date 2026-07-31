// ============================================
// PhishShield AI Dashboard
// ============================================

document.addEventListener("DOMContentLoaded", function () {

    // ============================================
    // Confidence Chart
    // ============================================

    const chartCanvas = document.getElementById("confidenceChart");

    if (chartCanvas && typeof Chart !== "undefined") {

        const confidence = Number(confidenceValue) || 0;

        new Chart(chartCanvas, {

            type: "doughnut",

            data: {

                labels: ["Confidence", "Remaining"],

                datasets: [{

                    data: [confidence, 100 - confidence],

                    backgroundColor: [

                        "#2563eb",

                        "#1e293b"

                    ],

                    borderWidth: 0

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                cutout: "75%",

                plugins: {

                    legend: {

                        display: false

                    },

                    tooltip: {

                        callbacks: {

                            label: function (context) {

                                return context.raw + "%";

                            }

                        }

                    }

                }

            }

        });

    }

    // ============================================
    // Loading Button
    // ============================================

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const button = form.querySelector("button");

            if (button) {

                button.disabled = true;

                button.innerHTML =

                    '<i class="fa-solid fa-spinner fa-spin"></i> Scanning...';

            }

        });

    }

    // ============================================
    // Active Sidebar
    // ============================================

    const currentPath = window.location.pathname;

    document.querySelectorAll(".menu a").forEach(link => {

        if (link.getAttribute("href") === currentPath) {

            link.classList.add("active");

        }

    });

    // ============================================
    // Card Hover Effect
    // ============================================

    document.querySelectorAll(".card").forEach(card => {

        card.addEventListener("mouseenter", function () {

            card.style.transform = "translateY(-6px)";

            card.style.transition = ".3s";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform = "translateY(0px)";

        });

    });

    // ============================================
    // Notification Animation
    // ============================================

    const bell = document.querySelector(".notification");

    if (bell) {

        setInterval(() => {

            bell.classList.toggle("fa-shake");

        }, 4000);

    }

    // ============================================
    // Fade In Page
    // ============================================

    document.body.style.opacity = "0";

    window.onload = function () {

        document.body.style.transition = "opacity .5s";

        document.body.style.opacity = "1";

    };

    // ============================================
    // Theme Toggle (Future)
    // ============================================

    const themeToggle = document.getElementById("themeToggle");

    if (themeToggle) {

        themeToggle.addEventListener("click", function () {

            document.body.classList.toggle("light-mode");

        });

    }

});