document.addEventListener("DOMContentLoaded", function() {
/**
* HomePage - Help section
*/
class Help {
constructor($el) {
    this.$el = $el;
    this.$buttonsContainer = $el.querySelector(".help--buttons");
    this.$slidesContainers = $el.querySelectorAll(".help--slides");
    this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
    this.init();
}

init() {
    this.events();
}

events() {
    /**
     * Slide buttons
     */
    this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
            this.changeSlide(e);
        }
    });

    /**
     * Pagination buttons
     */
    this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
            this.changePage(e);
        }
    });
}

changeSlide(e) {
    e.preventDefault();
    const $btn = e.target;

    // Buttons Active class change
    [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
    $btn.classList.add("active");

    // Current slide
    this.currentSlide = $btn.parentElement.dataset.id;

    // Slides active class change
    this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
            el.classList.add("active");
        }
    });
}

/**
 * TODO: callback to page change event
 */
changePage(e) {
     // e.preventDefault(); // Disabled to allow standard link behavior in pagination.
    const page = e.target.dataset.page;

    console.log(page);
}
}
const helpSection = document.querySelector(".help");
if (helpSection !== null) {
new Help(helpSection);
}

/**
* Form Select
*/
class FormSelect {
constructor($el) {
    this.$el = $el;
    this.options = [...$el.children];
    this.init();
}

init() {
    this.createElements();
    this.addEvents();
    this.$el.parentElement.removeChild(this.$el);
}

createElements() {
    // Input for value
    this.valueInput = document.createElement("input");
    this.valueInput.type = "text";
    this.valueInput.name = this.$el.name;

    // Dropdown container
    this.dropdown = document.createElement("div");
    this.dropdown.classList.add("dropdown");

    // List container
    this.ul = document.createElement("ul");

    // All list options
    this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
            // First clickable option
            this.current = document.createElement("div");
            this.current.innerText = el.innerText;
            this.dropdown.appendChild(this.current);
            this.valueInput.value = el.value;
            li.classList.add("selected");
        }

        this.ul.appendChild(li);
    });

    this.dropdown.appendChild(this.ul);
    this.dropdown.appendChild(this.valueInput);
    this.$el.parentElement.appendChild(this.dropdown);
}

addEvents() {
    this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
            this.valueInput.value = target.dataset.value;
            this.current.innerText = target.innerText;
        }
    });
}
}
document.querySelectorAll(".form-group--dropdown select").forEach(el => {
new FormSelect(el);
});

/**
* Hide elements when clicked on document
*/
document.addEventListener("click", function(e) {
const target = e.target;
const tagName = target.tagName;

if (target.classList.contains("dropdown")) return false;

if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
    return false;
}

if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
    return false;
}

document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
    el.classList.remove("selecting");
});
});

/**
* Switching between form steps
*/
// TU JEST POCZĄTEK FORM STEPS
    class FormSteps {
        constructor(form) {
            this.$form = form;
            this.$next = form.querySelectorAll(".next-step");
            this.$prev = form.querySelectorAll(".prev-step");
            this.$step = form.querySelector(".form--steps-counter span");
            this.currentStep = 1;

            this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
            const $stepForms = form.querySelectorAll("form > div");
            this.slides = [...this.$stepInstructions, ...$stepForms];

            this.init();
        }

        init() {
            this.events();
            this.updateForm();
        }

        events() {
            this.$next.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    // Logowanie przed zmianą kroku
                    if (this.currentStep === 1) {
                        const selectedCategories = Array.from(document.querySelectorAll('input[name="categories"]:checked'))
                            .map(input => input.dataset.categoryName);
                        console.log("Zaznaczone kategorie:", selectedCategories.join(", "));
                    } else if (this.currentStep === 2) {
                        const bagsCount = document.querySelector('input[name="bags"]').value;
                        console.log("Liczba worków:", bagsCount);
                    } else if (this.currentStep === 3) {
                        const selectedRadio = document.querySelector('input[name="organization"]:checked');
                        const organizationLabel = selectedRadio ? selectedRadio.closest('label') : null;
                        const organizationTitle = organizationLabel ? organizationLabel.querySelector('.title') : null;
                        const selectedOrganization = organizationTitle ? organizationTitle.textContent : "Brak wybranej organizacji";
                        console.log("Wybrana organizacja:", selectedOrganization);
                    }

                    function updateSummary() {
                        const bags = document.querySelector('input[name="bags"]').value;
                        const selectedCategory = Array.from(document.querySelectorAll('input[name="categories"]:checked'))
                          .map(input => input.dataset.categoryName).join(", ");
                        const selectedRadio = document.querySelector('input[name="organization"]:checked');
                        const organizationLabel = selectedRadio ? selectedRadio.closest('label') : null;
                        const organizationTitle = organizationLabel ? organizationLabel.querySelector('.title') : null;
                        const selectedOrganization = organizationTitle ? organizationTitle.textContent : "Brak wybranej organizacji";


                        // Uaktualnienie danych w podsumowaniu
                        document.getElementById('summary-bags').textContent = `${bags} worki zawierające ${selectedCategory}`;
                        document.getElementById('summary-organization').textContent = `Zostaną przekazane ${selectedOrganization}`;

                        // Uzupełnienie danych o adresie i terminie odbioru z dodanymi skrótami i formatowaniem
                        document.getElementById('summary-address').textContent = `ul. ${document.querySelector("[name='address']").value}`;
                        document.getElementById('summary-postcode').textContent = `${document.querySelector("[name='postcode']").value}`;
                        document.getElementById('summary-city').textContent = `${document.querySelector("[name='city']").value}`;
                        document.getElementById('summary-phone').textContent = `tel. ${document.querySelector("[name='phone']").value}`;
                        document.getElementById('summary-date').textContent = `Data: ${document.querySelector("[name='date']").value}`;
                        document.getElementById('summary-time').textContent = `Godzina: ${document.querySelector("[name='time']").value}`;



                        const comments = document.querySelector("[name='more_info']").value.trim();
                        const commentsElement = document.getElementById('summary-comments');
                        if (comments) {
                            commentsElement.textContent = `Uwagi dla kuriera: ${comments}`;
                            commentsElement.style.fontStyle = "normal";
                        } else {
                            commentsElement.textContent = "Brak uwag";
                            commentsElement.style.fontStyle = "italic";
                        }
                    }

                    // Dodajemy to do obsługi zdarzeń w kroku 4, przed przejściem do kroku 5
                    if (this.currentStep === 4) {
                        this.collectDataAndShowSummary();
                        updateSummary();  // uaktualniamy podsumowanie
                    }


                    this.currentStep++;
                    this.updateForm();
                });
            });

            this.$prev.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep--;
                    this.updateForm();
                });
            });

            this.$form.querySelector("form").addEventListener("submit", e => {
                e.preventDefault();
                if (this.currentStep === 4) {
                    this.collectDataAndShowSummary(); // Wywołanie funkcji podsumowania danych również przy wysyłaniu formularza
                }
                this.currentStep++;
                this.updateForm();
            });
        }




        updateForm() {
            this.$step.innerText = this.currentStep;
            this.slides.forEach(slide => {
                slide.classList.remove("active");
                if (slide.dataset.step === String(this.currentStep)) {
                    slide.classList.add("active");
                }
            });


            // Filtracja organizacji tylko w kroku 3
            if (this.currentStep === 3) {
                console.log("W kroku 3, próba wyświetlenia organizacji.");
                filterOrganizations(); // Upewnij się, że funkcja jest wywoływana
            }

            this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
            this.$step.parentElement.hidden = this.currentStep >= 6;
        }



    collectDataAndShowSummary() {
        try {
            // Upewniamy się, że wszystkie elementy istnieją przed próbą dostępu do ich wartości
            const address = document.querySelector("[name='address']").value;
            const city = document.querySelector("[name='city']").value;
            const postcode = document.querySelector("[name='postcode']").value;
            const phone = document.querySelector("[name='phone']").value;
            const date = document.querySelector("[name='date']").value;
            const time = document.querySelector("[name='time']").value;
            const comments = document.querySelector("[name='more_info']").value;

            console.log("Podsumowanie Adres odbioru:", address);
            console.log("Miasto:", city);
            console.log("Kod pocztowy:", postcode);
            console.log("Numer telefonu:", phone);
            console.log("Data odbioru:", date);
            console.log("Godzina odbioru:", time);
            console.log("Uwagi dla kuriera:", comments);
        } catch (error) {
            console.error("Błąd podczas zbierania danych formularza:", error);
        }
    }



    submit(e) {
        e.preventDefault();
        this.currentStep++;
        this.updateForm();
    }
}



// TU JEST KONIEC FORM STEPS
const form = document.querySelector(".form--steps");
if (form !== null) {
new FormSteps(form);
}




















// Function to filter organizations based on selected categories
function filterOrganizations() {
const selectedCategories = new Set(
    Array.from(document.querySelectorAll('input[name="categories"]:checked'))
    .map(input => input.dataset.categoryName)
);

const organizations = document.querySelectorAll('.organization');
organizations.forEach(org => {
    const organizationCategories = org.dataset.categories.split(', ');
    const isVisible = organizationCategories.some(category => selectedCategories.has(category));

    org.style.display = isVisible ? 'block' : 'none';
});
}


document.querySelectorAll('input[name="categories"]').forEach(input => {
input.addEventListener('change', filterOrganizations);
});

// Invoke the filtering function at initial page load
filterOrganizations();
});
