document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('scrapeForm');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');
    const mainTabButtons = document.querySelectorAll('.main-tab-button');
    const mainTabContents = document.querySelectorAll('.main-tab-content');

    form.addEventListener('submit', function(e) {
        loadingIndicator.style.display = 'flex';
    });

    function setActiveTab(buttons, contents, clickedButton) {
        buttons.forEach(btn => btn.classList.remove('active'));
        contents.forEach(content => {
            content.classList.remove('active');
            content.classList.add('hidden');
        });

        clickedButton.classList.add('active');
        const tabName = clickedButton.getAttribute('data-tab');
        const activeContent = document.getElementById(tabName);
        activeContent.classList.add('active');
        activeContent.classList.remove('hidden');
    }

    tabButtons.forEach(button => {
        button.addEventListener('click', () => setActiveTab(tabButtons, tabContents, button));
    });

    mainTabButtons.forEach(button => {
        button.addEventListener('click', () => setActiveTab(mainTabButtons, mainTabContents, button));
    });

    // Ensure the initial state is correct
    setActiveTab(mainTabButtons, mainTabContents, mainTabButtons[0]);
});