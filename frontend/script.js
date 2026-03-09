// API endpoint
const API_URL = '/api/data';

// Fetch data from backend
async function fetchData() {
    try {
        const response = await fetch(API_URL);
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        
        // Update DOM elements with animation
        updateElement('time', data.time);
        updateElement('date', data.date);
        updateElement('quote', `"${data.quote}"`);
        
    } catch (error) {
        console.error('Error fetching data:', error);
        updateElement('time', 'Unable to fetch time');
        updateElement('date', 'Unable to fetch date');
        updateElement('quote', 'Unable to fetch quote. Please check your connection.');
    }
}

// Update element with fade animation
function updateElement(id, value) {
    const element = document.getElementById(id);
    
    if (element) {
        element.style.opacity = '0';
        
        setTimeout(() => {
            element.textContent = value;
            element.style.transition = 'opacity 0.5s ease';
            element.style.opacity = '1';
        }, 200);
    }
}

// Auto-refresh time every 1 second
function startAutoRefresh() {
    setInterval(() => {
        fetchData();
    }, 1000);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    fetchData();
    startAutoRefresh();
    
    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';
});

// Handle visibility change to pause/resume updates
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        console.log('Page hidden - updates paused');
    } else {
        console.log('Page visible - fetching fresh data');
        fetchData();
    }
});
