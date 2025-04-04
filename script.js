document.addEventListener('DOMContentLoaded', function() {
    const logos = [
        { file: 'logo1.svg', title: 'Tech Gamer', description: 'A modern, tech-inspired logo combining gaming elements with programming symbols.' },
        { file: 'logo2.svg', title: 'Code Commander', description: 'Bold, futuristic design representing leadership in both gaming and coding.' },
        { file: 'logo3.svg', title: 'Pixel Player', description: 'Retro pixel art style logo with vibrant colors and gaming nostalgia.' },
        { file: 'logo4.svg', title: 'Developer\'s Arena', description: 'Abstract representation of code and gaming controllers unified in a circular design.' },
        { file: 'logo5.svg', title: 'Digital Warrior', description: 'Sleek, modern design with sharp edges representing precision in coding and gaming.' },
        { file: 'logo6.svg', title: 'Circuit Gamer', description: 'Circuit board patterns incorporated into a gaming-themed emblem.' },
        { file: 'logo7.svg', title: 'Neon Coder', description: 'Vibrant neon-inspired design with code brackets and gaming icons.' },
        { file: 'logo8.svg', title: 'Binary Blaster', description: 'Geometric logo with binary code elements and gaming controller silhouette.' },
        { file: 'logo9.svg', title: 'Syntax Slayer', description: 'Programming syntax symbols arranged in a dynamic, game-like form.' },
        { file: 'logo10.svg', title: 'Console Commander', description: 'Vintage console controller reimagined with coding elements.' },
        { file: 'logo11.svg', title: 'Dev Level Up', description: 'Gaming level-up icon combined with development tools in a shield format.' },
        { file: 'logo12.svg', title: 'Polygon Programmer', description: 'Low-poly style logo with a modern, geometric approach to gaming and coding.' },
        { file: 'logo13.svg', title: 'Keyboard Warrior', description: 'Stylized keyboard keys forming a dynamic, action-oriented emblem.' },
        { file: 'logo14.svg', title: 'Algorithm Ace', description: 'Abstract representation of algorithms and game strategy in a sleek design.' },
        { file: 'logo15.svg', title: 'Function Player', description: 'Functional programming symbols merged with gaming controllers in a circular logo.' },
        { file: 'logo16.svg', title: 'Hex Coder', description: 'Hexagonal patterns forming a gaming avatar with code elements.' },
        { file: 'logo17.svg', title: 'Debug Champion', description: 'Bug-fixing themes combined with victory symbols in a bold design.' },
        { file: 'logo18.svg', title: 'Script Striker', description: 'Dynamic script lettering with gaming action elements.' },
        { file: 'logo19.svg', title: 'Virtual Builder', description: 'Construction and creation themes merging virtual worlds and code.' },
        { file: 'logo20.svg', title: 'Logic Leveler', description: 'Logical gates and level-up icons in a minimalist design.' },
        { file: 'logo21.svg', title: 'Render Engine', description: 'Abstract representation of 3D rendering and game engines.' },
        { file: 'logo22.svg', title: 'Stack Overflow Gamer', description: 'Stack-based design with overflow elements and gaming icons.' },
        { file: 'logo23.svg', title: 'Git Master', description: 'Branch-based design inspired by version control and game mastery.' },
        { file: 'logo24.svg', title: 'Framework Fighter', description: 'Web framework icons arranged in a combat-ready formation.' },
        { file: 'logo25.svg', title: 'KnarliX Prime', description: 'Premium signature logo combining all elements of gaming and development.' }
    ];

    let currentLogoIndex = 0;
    const currentLogo = document.getElementById('current-logo');
    const logoTitle = document.getElementById('logo-title');
    const logoDescription = document.getElementById('logo-description');
    const counter = document.getElementById('counter');
    const prevButton = document.getElementById('previous');
    const nextButton = document.getElementById('next');
    const gridViewButton = document.getElementById('grid-view');
    const singleViewButton = document.getElementById('single-view');
    const singleLogoView = document.getElementById('single-logo-view');
    const gridLogoView = document.getElementById('grid-logo-view');
    const logoGrid = document.querySelector('.logo-grid');

    // Initialize grid view
    function initGridView() {
        logoGrid.innerHTML = ''; // Clear existing content
        logos.forEach((logo, index) => {
            const gridItem = document.createElement('div');
            gridItem.classList.add('grid-item');
            gridItem.setAttribute('data-index', index);
            
            const obj = document.createElement('object');
            obj.setAttribute('data', `logos/${logo.file}`);
            obj.setAttribute('type', 'image/svg+xml');
            
            gridItem.appendChild(obj);
            logoGrid.appendChild(gridItem);
            
            gridItem.addEventListener('click', function() {
                currentLogoIndex = index;
                updateLogoDisplay();
                switchToSingleView();
            });
        });
    }

    // Update the display for the current logo
    function updateLogoDisplay() {
        const logo = logos[currentLogoIndex];
        currentLogo.setAttribute('data', `logos/${logo.file}`);
        logoTitle.textContent = `Logo ${currentLogoIndex + 1}: ${logo.title}`;
        logoDescription.textContent = logo.description;
        counter.textContent = `${currentLogoIndex + 1}/${logos.length}`;
    }

    // Switch to single view
    function switchToSingleView() {
        singleLogoView.classList.add('active-view');
        gridLogoView.classList.remove('active-view');
        singleViewButton.classList.add('active');
        gridViewButton.classList.remove('active');
    }

    // Switch to grid view
    function switchToGridView() {
        singleLogoView.classList.remove('active-view');
        gridLogoView.classList.add('active-view');
        singleViewButton.classList.remove('active');
        gridViewButton.classList.add('active');
    }

    // Event listeners
    prevButton.addEventListener('click', function() {
        currentLogoIndex = (currentLogoIndex - 1 + logos.length) % logos.length;
        updateLogoDisplay();
    });

    nextButton.addEventListener('click', function() {
        currentLogoIndex = (currentLogoIndex + 1) % logos.length;
        updateLogoDisplay();
    });

    gridViewButton.addEventListener('click', function() {
        switchToGridView();
    });

    singleViewButton.addEventListener('click', function() {
        switchToSingleView();
    });

    // Initialize the page
    initGridView();
    updateLogoDisplay();

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') {
            prevButton.click();
        } else if (e.key === 'ArrowRight') {
            nextButton.click();
        } else if (e.key === 'g') {
            gridViewButton.click();
        } else if (e.key === 's') {
            singleViewButton.click();
        }
    });
});
