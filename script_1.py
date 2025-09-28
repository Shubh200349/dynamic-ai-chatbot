project_files['static/index.html'] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic AI Chatbot</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="header-content">
            <div class="logo">
                <i class="fas fa-robot"></i>
                <h1>Dynamic AI Chatbot</h1>
                <small>Powered by Gemini AI</small>
            </div>
            <nav class="nav">
                <div class="api-status" id="apiStatus">
                    <div class="status-indicator online"></div>
                    <span>AI Online</span>
                </div>
                <button class="theme-toggle" id="themeToggle">
                    <i class="fas fa-moon"></i>
                </button>
            </nav>
        </div>
    </header>

    <!-- Mobile Navigation -->
    <nav class="mobile-nav">
        <div class="mobile-nav-items">
            <button class="mobile-nav-item active" data-section="chat">
                <i class="fas fa-comments"></i>
                <span>Chat</span>
            </button>
            <button class="mobile-nav-item" data-section="analytics">
                <i class="fas fa-chart-bar"></i>
                <span>Analytics</span>
            </button>
            <button class="mobile-nav-item" data-section="settings">
                <i class="fas fa-cog"></i>
                <span>Settings</span>
            </button>
            <button class="mobile-nav-item" data-section="about">
                <i class="fas fa-info-circle"></i>
                <span>About</span>
            </button>
        </div>
    </nav>

    <!-- Main Layout -->
    <div class="main-layout">
        <!-- Left Sidebar -->
        <aside class="sidebar-left">
            <nav class="sidebar-nav">
                <button class="nav-item active" data-section="chat">
                    <i class="fas fa-comments"></i>
                    <span>Chat</span>
                </button>
                <button class="nav-item" data-section="analytics">
                    <i class="fas fa-chart-bar"></i>
                    <span>Analytics</span>
                </button>
                <button class="nav-item" data-section="settings">
                    <i class="fas fa-cog"></i>
                    <span>Settings</span>
                </button>
                <button class="nav-item" data-section="about">
                    <i class="fas fa-info-circle"></i>
                    <span>About</span>
                </button>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Chat Section -->
            <section id="chat-section" class="content-section active">
                <div class="chat-container">
                    <div class="chat-header">
                        <div class="chat-status">
                            <div class="status-indicator online"></div>
                            <span>AI Assistant</span>
                        </div>
                        <small>Powered by Gemini AI</small>
                    </div>
                    
                    <div class="chat-messages" id="chatMessages">
                        <!-- Messages will be added here dynamically -->
                    </div>
                    
                    <div class="typing-indicator hidden" id="typingIndicator">
                        <span>AI is typing</span>
                        <div class="typing-dots">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                    </div>
                    
                    <div class="chat-input">
                        <div class="input-container">
                            <textarea id="messageInput" placeholder="Type your message here..." rows="1"></textarea>
                            <div class="input-actions">
                                <span class="char-count" id="charCount">0/1000</span>
                                <button class="send-btn" id="sendBtn">
                                    <i class="fas fa-paper-plane"></i>
                                </button>
                            </div>
                        </div>
                        
                        <div class="quick-replies">
                            <button class="quick-reply" data-message="Hello! How can you help me?">👋 Hello</button>
                            <button class="quick-reply" data-message="What can you do?">❓ What can you do?</button>
                            <button class="quick-reply" data-message="Tell me a joke">😄 Tell me a joke</button>
                            <button class="quick-reply" data-message="Explain AI to me">🤖 Explain AI</button>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Analytics Section -->
            <section id="analytics-section" class="content-section">
                <div class="analytics-container">
                    <h2>Conversation Analytics</h2>
                    
                    <div class="analytics-grid">
                        <div class="stat-card">
                            <div class="stat-value" id="totalConversations">1</div>
                            <div class="stat-label">Total Conversations</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value" id="totalMessages">1</div>
                            <div class="stat-label">Total Messages</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value" id="avgResponseTime">1.2s</div>
                            <div class="stat-label">Avg Response Time</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value" id="apiSuccessRate">100%</div>
                            <div class="stat-label">API Success Rate</div>
                        </div>
                    </div>
                    
                    <div class="charts-container">
                        <div class="chart-card">
                            <h3>Sentiment Analysis</h3>
                            <canvas id="sentimentChart"></canvas>
                        </div>
                        <div class="chart-card">
                            <h3>Response Time Trend</h3>
                            <canvas id="responseTimeChart"></canvas>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Settings Section -->
            <section id="settings-section" class="content-section">
                <div class="settings-container">
                    <h2>Settings</h2>
                    
                    <div class="settings-group">
                        <h3>Appearance</h3>
                        <div class="setting-item">
                            <label for="themeSelect">Theme</label>
                            <select id="themeSelect" class="form-control">
                                <option value="auto">Auto</option>
                                <option value="light">Light</option>
                                <option value="dark">Dark</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="settings-group">
                        <h3>AI Configuration</h3>
                        <div class="setting-item">
                            <label for="languageSelect">Language</label>
                            <select id="languageSelect" class="form-control">
                                <option value="en">English</option>
                                <option value="hi">Hindi</option>
                                <option value="hinglish">Hinglish</option>
                            </select>
                        </div>
                        <div class="setting-item">
                            <label for="temperatureSlider">Response Creativity: <span id="temperatureValue">0.7</span></label>
                            <input type="range" id="temperatureSlider" min="0.1" max="1.0" step="0.1" value="0.7">
                        </div>
                    </div>
                    
                    <div class="settings-group">
                        <h3>Chat Features</h3>
                        <div class="setting-item">
                            <label class="checkbox-label">
                                <input type="checkbox" id="showTimestamps" checked>
                                Show message timestamps
                            </label>
                        </div>
                        <div class="setting-item">
                            <label class="checkbox-label">
                                <input type="checkbox" id="enableSentiment" checked>
                                Enable sentiment analysis
                            </label>
                        </div>
                        <div class="setting-item">
                            <label class="checkbox-label">
                                <input type="checkbox" id="contextMemory" checked>
                                Remember conversation context
                            </label>
                        </div>
                    </div>
                    
                    <div class="settings-actions">
                        <button class="btn btn--primary" id="exportChat">Export Chat History</button>
                        <button class="btn btn--outline" id="clearChat">Clear Chat History</button>
                    </div>
                </div>
            </section>

            <!-- About Section -->
            <section id="about-section" class="content-section">
                <div class="about-container">
                    <h2>About Dynamic AI Chatbot</h2>
                    
                    <div class="about-content">
                        <div class="feature-card">
                            <div class="feature-icon">
                                <i class="fas fa-brain"></i>
                            </div>
                            <h3>Gemini AI Integration</h3>
                            <p>Powered by Google's advanced Gemini AI model for intelligent, contextual conversations and accurate responses to any query.</p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">
                                <i class="fas fa-memory"></i>
                            </div>
                            <h3>Context Awareness</h3>
                            <p>Maintains conversation context and remembers previous interactions for more natural, flowing conversations.</p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">
                                <i class="fas fa-heart"></i>
                            </div>
                            <h3>Sentiment Analysis</h3>
                            <p>Real-time emotional intelligence analyzes the tone of your messages to provide appropriate and empathetic responses.</p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">
                                <i class="fas fa-chart-line"></i>
                            </div>
                            <h3>Performance Analytics</h3>
                            <p>Comprehensive insights into conversation quality, API performance, response times, and engagement metrics.</p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">
                                <i class="fas fa-language"></i>
                            </div>
                            <h3>Multilingual Support</h3>
                            <p>Supports English, Hindi, and Hinglish for natural communication in your preferred language with AI understanding.</p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <h3>Reliable & Secure</h3>
                            <p>Built with robust error handling, fallback responses, and secure API integration for consistent performance.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>

        <!-- Right Sidebar -->
        <aside class="sidebar-right">
            <div class="user-info">
                <h3>Session Info</h3>
                <div class="session-stats">
                    <div class="stat-item">
                        <span class="stat-label">Messages</span>
                        <span class="stat-value" id="sessionMessages">1</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">Sentiment</span>
                        <span class="stat-value sentiment positive" id="sessionSentiment">Positive</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">Duration</span>
                        <span class="stat-value" id="sessionDuration">0m</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">API Calls</span>
                        <span class="stat-value" id="apiCalls">1</span>
                    </div>
                </div>
            </div>
            
            <div class="recent-topics">
                <h3>Recent Topics</h3>
                <div class="topics-list" id="recentTopics">
                    <div class="topic-item">General</div>
                </div>
            </div>
        </aside>
    </div>

    <script src="app.js"></script>
</body>
</html>"""

print("Created static/index.html")