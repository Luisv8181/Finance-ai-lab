// =====================================================
//  STOCKER DASHBOARD — app.js
//  Handles report loading, ticker bar, and report history
// =====================================================

// --- Report Loading ---
async function loadReport(filename) {
    const content = document.getElementById('content');
    const path = filename ? `/reports/${filename}` : '/reports/latest.md';
    try {
        const response = await fetch(path);
        if (!response.ok) throw new Error('Report not found');

        const markdown = await response.text();
        content.innerHTML = marked.parse(markdown);
        colorCodeChanges();

        content.style.opacity = 0;
        setTimeout(() => {
            content.style.transition = 'opacity 0.6s ease-in';
            content.style.opacity = 1;
        }, 50);
    } catch (error) {
        content.innerHTML = `<div class="error" style="color: var(--vermillion)">[CRITICAL ERROR] UNABLE TO FETCH DATA: ${error.message}</div>`;
    }
}

// --- Color Code Gains/Losses in Tables ---
function colorCodeChanges() {
    document.querySelectorAll('.md-content td').forEach(td => {
        const text = td.textContent.trim();
        if (text.match(/^\+[\d.]+%?$/)) {
            td.style.color = '#00ff88';
            td.style.textShadow = '0 0 6px rgba(0,255,136,0.4)';
        } else if (text.match(/^-[\d.]+%?$/)) {
            td.style.color = '#ff3355';
            td.style.textShadow = '0 0 6px rgba(255,51,85,0.4)';
        }
    });
}

// --- Animated Ticker Bar ---
async function loadTickerBar() {
    const track = document.getElementById('ticker-track');
    try {
        const response = await fetch('/reports/latest.md');
        if (!response.ok) throw new Error('No data');
        const text = await response.text();

        // Parse stock data from the markdown table
        const stocks = [];
        const lines = text.split('\n');
        for (const line of lines) {
            // Match table rows like: | SPY | $686.10 | +1.28% | 53,737,879 |
            const match = line.match(/\|\s*([A-Z]{2,5})\s*\|\s*\$?([\d,.]+)\s*\|\s*([+-][\d.]+%?)\s*\|/);
            if (match) {
                stocks.push({
                    symbol: match[1],
                    price: match[2],
                    change: match[3]
                });
            }
        }

        if (stocks.length === 0) {
            track.innerHTML = '<span class="ticker-loading">NO MARKET DATA AVAILABLE</span>';
            return;
        }

        // Build ticker HTML (duplicate for seamless scroll)
        let tickerHTML = '';
        const buildItems = (items) => items.map(s => {
            const isUp = s.change.startsWith('+');
            const cls = isUp ? 'ticker-up' : 'ticker-down';
            const arrow = isUp ? '▲' : '▼';
            return `<span class="ticker-item">
                <span class="ticker-symbol">${s.symbol}</span>
                <span class="ticker-price">$${s.price}</span>
                <span class="${cls}">${arrow} ${s.change}</span>
            </span>`;
        }).join('');

        tickerHTML = buildItems(stocks) + buildItems(stocks); // duplicate for loop
        track.innerHTML = tickerHTML;

    } catch {
        track.innerHTML = '<span class="ticker-loading">AWAITING MARKET DATA...</span>';
    }
}

// --- Report History Sidebar ---
async function loadReportHistory() {
    const list = document.getElementById('report-list');
    try {
        const response = await fetch('/reports/');
        if (!response.ok) throw new Error('Cannot list reports');
        const html = await response.text();

        // Parse directory listing for .md files
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const links = doc.querySelectorAll('a');
        const reports = [];

        links.forEach(link => {
            const href = link.getAttribute('href');
            if (href && href.endsWith('.md') && href !== 'latest.md') {
                reports.push(href);
            }
        });

        // Sort newest first
        reports.sort().reverse();

        if (reports.length === 0) {
            list.innerHTML = '<li class="loading-item">No reports found</li>';
            return;
        }

        list.innerHTML = '';
        reports.forEach((report, i) => {
            const li = document.createElement('li');
            // Extract date from filename: report_2026-04-13_19-03.md
            const dateMatch = report.match(/report_(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2})/);
            if (dateMatch) {
                const date = dateMatch[1];
                const time = dateMatch[2].replace('-', ':');
                li.textContent = `${date}  ${time}`;
            } else {
                li.textContent = report.replace('.md', '');
            }
            if (i === 0) li.classList.add('active');
            li.addEventListener('click', () => {
                document.querySelectorAll('.report-list li').forEach(l => l.classList.remove('active'));
                li.classList.add('active');
                loadReport(report);
            });
            list.appendChild(li);
        });

    } catch {
        list.innerHTML = '<li class="loading-item">Archive unavailable</li>';
    }
}

// --- Live Clock ---
function updateTime() {
    const timeEl = document.getElementById('live-time');
    const now = new Date();
    timeEl.innerText = now.toISOString().replace('T', ' ').substring(0, 19) + ' UTC';
}

// --- Initialize ---
setInterval(updateTime, 1000);
updateTime();
loadReport();
loadTickerBar();
loadReportHistory();

// Auto-refresh every 5 minutes
setInterval(() => {
    loadReport();
    loadTickerBar();
    loadReportHistory();
}, 300000);
