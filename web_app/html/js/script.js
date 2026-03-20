/* ========================================
   JAVASCRIPT FUNCTIONALITY
   ======================================== */

// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const newsInput = document.getElementById('newsInput');
const checkBtn = document.getElementById('checkBtn');
const resetBtn = document.getElementById('resetBtn');
const shareBtn = document.getElementById('shareBtn');
const resultsSection = document.getElementById('resultsSection');
const errorToast = document.getElementById('errorToast');

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ Fact-Checker App Loaded');
    checkBtn.addEventListener('click', checkFact);
    resetBtn.addEventListener('click', resetForm);
    shareBtn.addEventListener('click', shareResult);
});

/**
 * Check Fact Authenticity
 */
async function checkFact() {
    const text = newsInput.value.trim();

    if (!text) {
        showError('Please enter news text');
        return;
    }

    if (text.length < 10) {
        showError('Text too short. Please enter at least 10 characters.');
        return;
    }

    // Show loading state
    checkBtn.disabled = true;
    document.getElementById('spinner').classList.remove('hidden');
    document.querySelector('.btn-text').style.opacity = '0.7';

    try {
        // Call API
        const response = await fetch(`${API_BASE_URL}/check-fact`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.status === 'success') {
            displayResults(data);
        } else {
            showError(data.message || 'Error checking fact');
        }

    } catch (error) {
        console.error('Error:', error);
        showError('Error connecting to server. Make sure backend is running.');
    } finally {
        // Reset loading state
        checkBtn.disabled = false;
        document.getElementById('spinner').classList.add('hidden');
        document.querySelector('.btn-text').style.opacity = '1';
    }
}

/**
 * Display Results
 */
function displayResults(data) {
    // Show results section
    resultsSection.classList.remove('hidden');

    // Prediction Result
    const predictionResult = document.getElementById('predictionResult');
    const isReal = data.prediction.includes('Real');
    predictionResult.className = 'prediction-result ' + (isReal ? 'real' : 'fake');
    predictionResult.textContent = data.prediction;

    // Confidence
    const confidence = data.confidence;
    const confidenceFill = document.getElementById('confidenceFill');
    confidenceFill.style.width = confidence + '%';
    confidenceFill.textContent = confidence + '%';

    const confidenceText = document.getElementById('confidenceText');
    confidenceText.textContent = `Confidence: ${confidence}%`;

    // Language
    const languageSpan = document.getElementById('language');
    languageSpan.textContent = data.language || 'Unknown';

    // Processed Text
    const processedText = document.getElementById('processedText');
    processedText.textContent = data.processed_text || 'N/A';

    // Similar Facts
    displayFacts(data.similar_facts || []);

    // Scroll to results
    setTimeout(() => {
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 300);
}

/**
 * Display Similar Facts
 */
function displayFacts(facts) {
    const factsList = document.getElementById('factsList');

    if (!facts || facts.length === 0) {
        factsList.innerHTML = '<p class="no-facts">No similar facts found in database</p>';
        return;
    }

    factsList.innerHTML = facts.map((fact, index) => `
        <div class="fact-card" style="animation-delay: ${index * 0.1}s;">
            <p class="fact-text">📌 "${fact.fact || fact}"</p>
            <p class="similarity-score">
                Similarity Score: ${(fact.similarity_score || 0).toFixed(2)}
            </p>
        </div>
    `).join('');
}

/**
 * Reset Form
 */
function resetForm() {
    newsInput.value = '';
    resultsSection.classList.add('hidden');
    newsInput.focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

/**
 * Share Result
 */
function shareResult() {
    const result = document.getElementById('predictionResult').textContent;
    const confidence = document.getElementById('confidenceText').textContent;
    const text = newsInput.value.substring(0, 100) + '...';

    const shareText = `I just checked a news article using AI Fact-Checker! 🔍\n\n${result}\n${confidence}\n\nTry it yourself: [Your URL]`;

    if (navigator.share) {
        navigator.share({
            title: 'Fact-Checker Result',
            text: shareText
        }).catch(err => console.log('Share cancelled'));
    } else {
        // Fallback: Copy to clipboard
        navigator.clipboard.writeText(shareText).then(() => {
            showSuccess('Result copied to clipboard!');
        });
    }
}

/**
 * Show Error Toast
 */
function showError(message) {
    const toast = document.getElementById('errorToast');
    toast.textContent = '❌ ' + message;
    toast.classList.remove('hidden');

    setTimeout(() => {
        toast.classList.add('hidden');
    }, 4000);
}

/**
 * Show Success Toast
 */
function showSuccess(message) {
    const toast = document.getElementById('errorToast');
    toast.textContent = '✅ ' + message;
    toast.style.background = '#51cf66';
    toast.classList.remove('hidden');

    setTimeout(() => {
        toast.classList.add('hidden');
        toast.style.background = 'var(--danger-color)';
    }, 4000);
}

// Keyboard shortcut
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        if (resultsSection.classList.contains('hidden')) {
            checkFact();
        }
    }
});

console.log('✅ All event listeners attached');
