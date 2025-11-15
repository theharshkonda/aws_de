// ========================================
// AWS Data Engineer Bootcamp - Main JavaScript
// ========================================

// ========================================
// 1. NAVIGATION & MOBILE MENU
// ========================================
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-menu a');

    // Toggle mobile menu
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking on a link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });

    // Active navigation on scroll
    window.addEventListener('scroll', () => {
        let current = '';
        const sections = document.querySelectorAll('section[id]');

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').slice(1) === current) {
                link.classList.add('active');
            }
        });
    });

    // Initialize components
    initializeProgress();
    initializeChart();
    loadLearningLogs();
    setupTaskListeners();
});

// ========================================
// 2. PROGRESS TRACKING
// ========================================
const STORAGE_KEYS = {
    PROGRESS: 'bootcamp_progress',
    LOGS: 'learning_logs',
    TASKS: 'daily_tasks',
    WEEKLY_PROGRESS: 'weekly_progress'
};

function initializeProgress() {
    const progress = getProgress();
    updateProgressDisplay(progress);
    updateWeeklyProgress();
}

function getProgress() {
    const stored = localStorage.getItem(STORAGE_KEYS.PROGRESS);
    if (stored) {
        return JSON.parse(stored);
    }

    // Default progress
    return {
        daysCompleted: 0,
        hoursLogged: 0,
        tasksCompleted: 0,
        projectsDone: 0,
        weekProgress: {
            week1: 0,
            week2: 0,
            week3: 0,
            week4: 0,
            week5: 0,
            week6: 0,
            week7: 0,
            week8: 0
        }
    };
}

function saveProgress(progress) {
    localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(progress));
    updateProgressDisplay(progress);
}

function updateProgressDisplay(progress) {
    const elements = {
        daysCompleted: document.getElementById('days-completed'),
        hoursLogged: document.getElementById('hours-logged'),
        tasksCompleted: document.getElementById('tasks-completed'),
        projectsDone: document.getElementById('projects-done')
    };

    if (elements.daysCompleted) elements.daysCompleted.textContent = progress.daysCompleted;
    if (elements.hoursLogged) elements.hoursLogged.textContent = progress.hoursLogged;
    if (elements.tasksCompleted) elements.tasksCompleted.textContent = progress.tasksCompleted;
    if (elements.projectsDone) elements.projectsDone.textContent = progress.projectsDone;
}

// ========================================
// 3. WEEKLY PROGRESS CHART
// ========================================
let weeklyChart = null;

function initializeChart() {
    const ctx = document.getElementById('weeklyChart');
    if (!ctx) return;

    const progress = getProgress();

    if (weeklyChart) {
        weeklyChart.destroy();
    }

    weeklyChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Week 1-2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8'],
            datasets: [{
                label: 'Progress (%)',
                data: [
                    progress.weekProgress.week1 || 0,
                    progress.weekProgress.week3 || 0,
                    progress.weekProgress.week4 || 0,
                    progress.weekProgress.week5 || 0,
                    progress.weekProgress.week6 || 0,
                    progress.weekProgress.week7 || 0,
                    progress.weekProgress.week8 || 0
                ],
                backgroundColor: [
                    'rgba(102, 126, 234, 0.8)',
                    'rgba(240, 147, 251, 0.8)',
                    'rgba(79, 172, 254, 0.8)',
                    'rgba(67, 233, 123, 0.8)',
                    'rgba(250, 112, 154, 0.8)',
                    'rgba(48, 207, 208, 0.8)',
                    'rgba(255, 216, 155, 0.8)'
                ],
                borderColor: [
                    'rgb(102, 126, 234)',
                    'rgb(240, 147, 251)',
                    'rgb(79, 172, 254)',
                    'rgb(67, 233, 123)',
                    'rgb(250, 112, 154)',
                    'rgb(48, 207, 208)',
                    'rgb(255, 216, 155)'
                ],
                borderWidth: 2,
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.parsed.y + '% Complete';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });
}

function updateWeeklyProgress() {
    const progress = getProgress();
    const timelineItems = document.querySelectorAll('.timeline-item');

    timelineItems.forEach(item => {
        const week = item.getAttribute('data-week');
        const progressSpan = item.querySelector('.timeline-progress');
        if (progressSpan && week) {
            let weekKey = 'week' + week.replace('-', '');
            let percentage = progress.weekProgress[weekKey] || 0;
            progressSpan.textContent = percentage + '% Complete';
        }
    });
}

// ========================================
// 4. TASK MANAGEMENT
// ========================================
function setupTaskListeners() {
    const checkboxes = document.querySelectorAll('.task-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateTaskCompletion);
    });

    loadTasks();
}

function updateTaskCompletion() {
    const progress = getProgress();
    const completedTasks = document.querySelectorAll('.task-checkbox:checked').length;
    progress.tasksCompleted = completedTasks;
    saveProgress(progress);
}

function addTask() {
    const taskText = prompt('Enter your task:');
    if (!taskText) return;

    const tasksContainer = document.getElementById('daily-tasks');
    const taskId = 'task-' + Date.now();

    const taskHTML = `
        <div class="task-item">
            <input type="checkbox" id="${taskId}" class="task-checkbox">
            <label for="${taskId}">${taskText}</label>
            <button class="btn-delete" onclick="deleteTask('${taskId}')">
                <i class="fas fa-trash"></i>
            </button>
        </div>
    `;

    tasksContainer.insertAdjacentHTML('beforeend', taskHTML);

    // Add event listener to new checkbox
    document.getElementById(taskId).addEventListener('change', updateTaskCompletion);

    saveTasks();
}

function deleteTask(taskId) {
    const taskElement = document.getElementById(taskId).closest('.task-item');
    if (taskElement) {
        taskElement.remove();
        saveTasks();
        updateTaskCompletion();
    }
}

function saveTasks() {
    const tasks = [];
    document.querySelectorAll('.task-item').forEach(item => {
        const checkbox = item.querySelector('.task-checkbox');
        const label = item.querySelector('label');
        tasks.push({
            id: checkbox.id,
            text: label.textContent,
            completed: checkbox.checked
        });
    });
    localStorage.setItem(STORAGE_KEYS.TASKS, JSON.stringify(tasks));
}

function loadTasks() {
    const stored = localStorage.getItem(STORAGE_KEYS.TASKS);
    if (!stored) return;

    const tasks = JSON.parse(stored);
    const tasksContainer = document.getElementById('daily-tasks');
    if (!tasksContainer) return;

    tasksContainer.innerHTML = '';

    tasks.forEach(task => {
        const taskHTML = `
            <div class="task-item">
                <input type="checkbox" id="${task.id}" class="task-checkbox" ${task.completed ? 'checked' : ''}>
                <label for="${task.id}">${task.text}</label>
            </div>
        `;
        tasksContainer.insertAdjacentHTML('beforeend', taskHTML);
    });

    // Re-attach event listeners
    setupTaskListeners();
}

// ========================================
// 5. LEARNING LOG
// ========================================
function saveLog() {
    const date = document.getElementById('log-date').value;
    const hours = parseFloat(document.getElementById('log-hours').value);
    const notes = document.getElementById('log-notes').value;

    if (!date || !hours || !notes) {
        alert('Please fill in all fields');
        return;
    }

    const log = {
        id: Date.now(),
        date: date,
        hours: hours,
        notes: notes,
        timestamp: new Date().toISOString()
    };

    // Get existing logs
    let logs = getLogs();
    logs.unshift(log);

    // Save logs
    localStorage.setItem(STORAGE_KEYS.LOGS, JSON.stringify(logs));

    // Update progress
    const progress = getProgress();
    progress.hoursLogged += hours;

    // Check if it's a new day
    const existingDates = new Set(logs.map(l => l.date));
    progress.daysCompleted = existingDates.size;

    saveProgress(progress);

    // Clear form
    document.getElementById('log-date').value = '';
    document.getElementById('log-hours').value = '';
    document.getElementById('log-notes').value = '';

    // Reload logs display
    loadLearningLogs();

    // Show success message
    showNotification('Log saved successfully!', 'success');
}

function getLogs() {
    const stored = localStorage.getItem(STORAGE_KEYS.LOGS);
    return stored ? JSON.parse(stored) : [];
}

function loadLearningLogs() {
    const logs = getLogs();
    const container = document.getElementById('log-history');
    if (!container) return;

    if (logs.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: #999;">No logs yet. Start logging your learning!</p>';
        return;
    }

    container.innerHTML = logs.map(log => `
        <div class="log-entry">
            <div class="log-entry-header">
                <span><i class="fas fa-calendar"></i> ${formatDate(log.date)}</span>
                <span><i class="fas fa-clock"></i> ${log.hours} hours</span>
            </div>
            <div class="log-entry-notes">${log.notes}</div>
            <button class="btn-delete-log" onclick="deleteLog(${log.id})">
                <i class="fas fa-trash"></i> Delete
            </button>
        </div>
    `).join('');
}

function deleteLog(logId) {
    if (!confirm('Are you sure you want to delete this log?')) return;

    let logs = getLogs();
    const deletedLog = logs.find(l => l.id === logId);
    logs = logs.filter(l => l.id !== logId);

    localStorage.setItem(STORAGE_KEYS.LOGS, JSON.stringify(logs));

    // Update progress
    if (deletedLog) {
        const progress = getProgress();
        progress.hoursLogged -= deletedLog.hours;

        const existingDates = new Set(logs.map(l => l.date));
        progress.daysCompleted = existingDates.size;

        saveProgress(progress);
    }

    loadLearningLogs();
    showNotification('Log deleted', 'info');
}

// ========================================
// 6. UTILITY FUNCTIONS
// ========================================
function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : 'info-circle'}"></i>
        <span>${message}</span>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : '#2196F3'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 10000;
        animation: slideIn 0.3s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    `;

    document.body.appendChild(notification);

    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// ========================================
// 7. DATA EXPORT/IMPORT
// ========================================
function exportProgress() {
    const data = {
        progress: getProgress(),
        logs: getLogs(),
        tasks: JSON.parse(localStorage.getItem(STORAGE_KEYS.TASKS) || '[]'),
        exportDate: new Date().toISOString()
    };

    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `bootcamp-progress-${new Date().toISOString().split('T')[0]}.json`;
    a.click();
    URL.revokeObjectURL(url);

    showNotification('Progress exported successfully!', 'success');
}

function importProgress(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = JSON.parse(e.target.result);

            // Restore data
            if (data.progress) {
                localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(data.progress));
            }
            if (data.logs) {
                localStorage.setItem(STORAGE_KEYS.LOGS, JSON.stringify(data.logs));
            }
            if (data.tasks) {
                localStorage.setItem(STORAGE_KEYS.TASKS, JSON.stringify(data.tasks));
            }

            // Reload page
            location.reload();
        } catch (error) {
            alert('Error importing progress. Please check the file format.');
            console.error(error);
        }
    };
    reader.readAsText(file);
}

function resetProgress() {
    if (!confirm('Are you sure you want to reset all progress? This cannot be undone!')) {
        return;
    }

    if (!confirm('This will delete all your logs, tasks, and progress. Are you absolutely sure?')) {
        return;
    }

    localStorage.removeItem(STORAGE_KEYS.PROGRESS);
    localStorage.removeItem(STORAGE_KEYS.LOGS);
    localStorage.removeItem(STORAGE_KEYS.TASKS);
    localStorage.removeItem(STORAGE_KEYS.WEEKLY_PROGRESS);

    location.reload();
}

// ========================================
// 8. SET TODAY'S DATE AS DEFAULT
// ========================================
function setTodayDate() {
    const dateInput = document.getElementById('log-date');
    if (dateInput && !dateInput.value) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.value = today;
    }
}

// Call on load
window.addEventListener('load', setTodayDate);

// ========================================
// 9. KEYBOARD SHORTCUTS
// ========================================
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + S to save log
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        if (document.getElementById('log-notes')) {
            saveLog();
        }
    }

    // Ctrl/Cmd + K to add task
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        addTask();
    }
});

// ========================================
// 10. SMOOTH SCROLL
// ========================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ========================================
// 11. WEEK PROGRESS UPDATER
// ========================================
function updateWeekProgress(weekNumber, percentage) {
    const progress = getProgress();
    const weekKey = 'week' + weekNumber;
    progress.weekProgress[weekKey] = Math.min(100, Math.max(0, percentage));
    saveProgress(progress);
    initializeChart();
    updateWeeklyProgress();
    showNotification(`Week ${weekNumber} progress updated to ${percentage}%`, 'success');
}

// Make functions globally available
window.addTask = addTask;
window.deleteTask = deleteTask;
window.saveLog = saveLog;
window.deleteLog = deleteLog;
window.exportProgress = exportProgress;
window.importProgress = importProgress;
window.resetProgress = resetProgress;
window.updateWeekProgress = updateWeekProgress;

console.log('🚀 AWS Data Engineer Bootcamp loaded successfully!');
console.log('💡 Keyboard shortcuts: Ctrl+S to save log, Ctrl+K to add task');
