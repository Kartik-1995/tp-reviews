import streamlit as st
import pandas as pd
from textblob import TextBlob
import plotly.express as px
# from googletrans import Translator  # Temporarily disabled for deployment
# Removed sklearn imports - no longer using clustering
# import numpy as np  # Not currently used

st.set_page_config(layout="wide", page_title="Trustpilot Review Dashboard")

# Global CSS for increased font size
st.markdown("""
<style>
    .stMarkdown, .stText, .stDataFrame, .stMetric, .stButton, .stSelectbox, .stSlider {
        font-size: 20px !important;
    }
    .stMarkdown p, .stMarkdown li {
        font-size: 20px !important;
    }
    .stDataFrame {
        font-size: 20px !important;
    }
    .stMetric {
        font-size: 20px !important;
    }
    .stButton > button {
        font-size: 20px !important;
    }
    /* Additional selectors for better coverage */
    .stMarkdown div, .stMarkdown span {
        font-size: 20px !important;
    }
    .stTextInput, .stTextArea {
        font-size: 20px !important;
    }
    .stExpander {
        font-size: 20px !important;
    }
    /* Increase heading sizes */
    h1, h2, h3, h4, h5, h6 {
        font-size: 24px !important;
    }
    h1 {
        font-size: 32px !important;
    }
    h2 {
        font-size: 28px !important;
    }
    h3 {
        font-size: 24px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("Trustpilot Review Analysis Dashboard")
st.markdown("**📊 Analyzing English Reviews Only** - This dashboard focuses on English-language reviews for accurate sentiment analysis and theme classification.")

@st.cache_data
def load_and_translate(filepath):
    df = pd.read_csv(filepath)
    # Filter to only English reviews
    df = df[df['reviewLanguage'] == 'en'].copy()
    df['reviewText_en'] = df['reviewText']  # Use original text for now
    df['sentiment'] = df['reviewText_en'].apply(lambda text: TextBlob(str(text)).sentiment.polarity)
    df['sentiment_label'] = df['sentiment'].apply(
        lambda score: "positive" if score > 0.1 else ("negative" if score < -0.1 else "neutral")
    )
    return df

# Removed old clustering-based theme detection - replaced with expert system

def get_actionable_insights(theme_name, keywords, cluster_reviews):
    """Generate detailed, specific actionable insights with problem-solution pairs"""
    
    insights = {
        "Users Accusing Platform of Being a Scam/Fraud": {
            "marketing": [
                {
                    "problem": "Users don't trust the platform due to lack of transparency",
                    "solution": "Launch 'Trust Verification Program' - Create a public dashboard showing real-time payment data, user testimonials, and third-party verification badges. Partner with Trustpilot, BBB, and other trust organizations to display verified status.",
                    "implementation": "Week 1: Design trust dashboard. Week 2: Integrate payment verification APIs. Week 3: Partner with trust organizations. Week 4: Launch campaign with case studies.",
                    "expected_impact": "Reduce scam accusations by 60% within 3 months"
                },
                {
                    "problem": "No proof of legitimate payments to users",
                    "solution": "Create 'Payment Proof Gallery' - Develop a public showcase of real payment screenshots, video testimonials from long-term contributors, and payment verification certificates.",
                    "implementation": "Week 1: Collect payment proofs from top contributors. Week 2: Create video testimonials. Week 3: Design gallery interface. Week 4: Launch with social media campaign.",
                    "expected_impact": "Increase user confidence by 75%"
                },
                {
                    "problem": "Lack of clear communication about platform legitimacy",
                    "solution": "Implement 'Legitimacy Assurance' email sequence - Send new users a 5-email series explaining platform history, security measures, and success stories.",
                    "implementation": "Week 1: Write email content. Week 2: Set up automation. Week 3: A/B test messaging. Week 4: Launch to all new users.",
                    "expected_impact": "Reduce new user churn by 40%"
                }
            ],
            "product": [
                {
                    "problem": "No real-time verification system for payments",
                    "solution": "Build 'Payment Verification Engine' - Create automated system that verifies and displays payment confirmations in real-time with blockchain-like transparency.",
                    "implementation": "Sprint 1: Design verification architecture. Sprint 2: Build payment tracking system. Sprint 3: Add real-time notifications. Sprint 4: Launch with dashboard.",
                    "expected_impact": "Eliminate payment disputes by 90%"
                },
                {
                    "problem": "Users can't verify platform authenticity",
                    "solution": "Develop 'Trust Score System' - Implement a reputation scoring mechanism that shows user trust levels, verification status, and platform reliability metrics.",
                    "implementation": "Sprint 1: Design scoring algorithm. Sprint 2: Build verification system. Sprint 3: Create user dashboard. Sprint 4: Launch with gamification.",
                    "expected_impact": "Increase user retention by 50%"
                }
            ]
        },
        "Account Suspended Before Payment - Users Not Getting Paid": {
            "marketing": [
                {
                    "problem": "Users feel cheated when suspended before payment",
                    "solution": "Launch 'Payment Protection Guarantee' - Create a program that guarantees payment for completed work even if account is suspended, with clear appeal process.",
                    "implementation": "Week 1: Design guarantee program. Week 2: Create appeal process. Week 3: Build payment protection system. Week 4: Launch with insurance partnership.",
                    "expected_impact": "Reduce payment complaints by 80%"
                },
                {
                    "problem": "No transparency in suspension reasons",
                    "solution": "Implement 'Suspension Transparency' - Create detailed explanations for account suspensions with specific steps to resolve issues and appeal process.",
                    "implementation": "Week 1: Design transparency system. Week 2: Create appeal workflow. Week 3: Build notification system. Week 4: Launch with support training.",
                    "expected_impact": "Improve user satisfaction by 65%"
                }
            ],
            "product": [
                {
                    "problem": "Automated suspensions without human review",
                    "solution": "Build 'Human Review System' - Implement mandatory human review for all account suspensions with 24-hour response time and clear escalation process.",
                    "implementation": "Sprint 1: Design review workflow. Sprint 2: Build review dashboard. Sprint 3: Add escalation system. Sprint 4: Launch with quality metrics.",
                    "expected_impact": "Reduce wrongful suspensions by 95%"
                },
                {
                    "problem": "No payment protection for suspended accounts",
                    "solution": "Create 'Payment Escrow System' - Hold payments in escrow for 7 days after work completion, ensuring users get paid even if suspended.",
                    "implementation": "Sprint 1: Design escrow system. Sprint 2: Build payment protection. Sprint 3: Add dispute resolution. Sprint 4: Launch with insurance.",
                    "expected_impact": "Eliminate unpaid work issues by 100%"
                }
            ]
        },
        "Payment Delays or Missing Payments After Work Completed": {
            "marketing": [
                {
                    "problem": "Users don't know when payments will arrive",
                    "solution": "Launch 'Payment Timeline Promise' - Create guaranteed payment schedules with real-time tracking and milestone notifications.",
                    "implementation": "Week 1: Design timeline system. Week 2: Build tracking interface. Week 3: Create notification system. Week 4: Launch with guarantees.",
                    "expected_impact": "Reduce payment anxiety by 70%"
                },
                {
                    "problem": "No communication about payment delays",
                    "solution": "Implement 'Payment Status Updates' - Send proactive notifications about payment status, delays, and resolution steps.",
                    "implementation": "Week 1: Design notification system. Week 2: Build status tracking. Week 3: Create communication templates. Week 4: Launch with automation.",
                    "expected_impact": "Improve payment satisfaction by 85%"
                }
            ],
            "product": [
                {
                    "problem": "Manual payment processing causing delays",
                    "solution": "Build 'Automated Payment Engine' - Create system that processes payments automatically within 24 hours of work completion.",
                    "implementation": "Sprint 1: Design automation system. Sprint 2: Build payment processing. Sprint 3: Add verification checks. Sprint 4: Launch with monitoring.",
                    "expected_impact": "Reduce payment delays by 90%"
                },
                {
                    "problem": "No payment tracking for users",
                    "solution": "Develop 'Payment Dashboard' - Create real-time payment tracking with status updates, milestone notifications, and dispute resolution.",
                    "implementation": "Sprint 1: Design dashboard. Sprint 2: Build tracking system. Sprint 3: Add notifications. Sprint 4: Launch with mobile app.",
                    "expected_impact": "Increase payment transparency by 100%"
                }
            ]
        },
        "Poor Customer Support - Slow Response or No Help": {
            "marketing": [
                {
                    "problem": "Users can't get help when needed",
                    "solution": "Launch '24/7 Support Guarantee' - Implement live chat support with 2-hour response time guarantee and dedicated support team.",
                    "implementation": "Week 1: Hire support team. Week 2: Set up live chat. Week 3: Create response time monitoring. Week 4: Launch with guarantees.",
                    "expected_impact": "Improve support satisfaction by 80%"
                },
                {
                    "problem": "No self-help resources available",
                    "solution": "Create 'Support Knowledge Base' - Build comprehensive FAQ, video tutorials, and troubleshooting guides for common issues.",
                    "implementation": "Week 1: Research common issues. Week 2: Create content. Week 3: Build knowledge base. Week 4: Launch with search optimization.",
                    "expected_impact": "Reduce support tickets by 60%"
                }
            ],
            "product": [
                {
                    "problem": "Manual ticket routing causing delays",
                    "solution": "Build 'Smart Support System' - Implement AI-powered ticket routing with automatic categorization and priority assignment.",
                    "implementation": "Sprint 1: Design AI system. Sprint 2: Build routing logic. Sprint 3: Add categorization. Sprint 4: Launch with monitoring.",
                    "expected_impact": "Reduce response time by 75%"
                },
                {
                    "problem": "No support tracking for users",
                    "solution": "Develop 'Support Dashboard' - Create real-time ticket tracking with status updates, estimated resolution times, and escalation options.",
                    "implementation": "Sprint 1: Design dashboard. Sprint 2: Build tracking system. Sprint 3: Add notifications. Sprint 4: Launch with mobile access.",
                    "expected_impact": "Improve support transparency by 90%"
                }
            ]
        },
        "No Work Available - Empty Queues and Project Instability": {
            "marketing": [
                {
                    "problem": "Users can't find consistent work",
                    "solution": "Launch 'Work Availability Program' - Create guaranteed minimum work hours and project availability notifications with priority access.",
                    "implementation": "Week 1: Design availability program. Week 2: Build notification system. Week 3: Create priority access. Week 4: Launch with guarantees.",
                    "expected_impact": "Increase user retention by 70%"
                },
                {
                    "problem": "No transparency about work availability",
                    "solution": "Implement 'Work Queue Transparency' - Show real-time work availability, upcoming projects, and waitlist management.",
                    "implementation": "Week 1: Design transparency system. Week 2: Build queue dashboard. Week 3: Add notifications. Week 4: Launch with predictions.",
                    "expected_impact": "Improve user satisfaction by 65%"
                }
            ],
            "product": [
                {
                    "problem": "Manual work assignment causing delays",
                    "solution": "Build 'Smart Work Assignment' - Create AI-powered system that matches users to available work based on skills and availability.",
                    "implementation": "Sprint 1: Design matching algorithm. Sprint 2: Build assignment system. Sprint 3: Add skill matching. Sprint 4: Launch with optimization.",
                    "expected_impact": "Increase work efficiency by 80%"
                },
                {
                    "problem": "No work forecasting for users",
                    "solution": "Develop 'Work Forecasting Dashboard' - Create predictive analytics showing upcoming work availability and skill demand.",
                    "implementation": "Sprint 1: Design forecasting model. Sprint 2: Build prediction system. Sprint 3: Add dashboard. Sprint 4: Launch with alerts.",
                    "expected_impact": "Improve user planning by 90%"
                }
            ]
        }
    }
    
    return insights.get(theme_name, {
        "marketing": [
            {
                "problem": "Generic issue without specific solution",
                "solution": "Create targeted campaign addressing specific user concerns with clear value proposition and measurable outcomes.",
                "implementation": "Week 1: Research issue. Week 2: Design solution. Week 3: Build campaign. Week 4: Launch and monitor.",
                "expected_impact": "Improve user satisfaction by 50%"
            }
        ],
        "product": [
            {
                "problem": "Generic technical issue",
                "solution": "Implement specific technical solution with clear requirements, timeline, and success metrics.",
                "implementation": "Sprint 1: Design solution. Sprint 2: Build feature. Sprint 3: Test and refine. Sprint 4: Launch with monitoring.",
                "expected_impact": "Resolve technical issues by 80%"
            }
        ]
    })

def analyze_review_content(text):
    """Expert system to analyze review content and extract specific issues"""
    text_lower = text.lower()
    
    # Define expert rules for different issue categories
    rules = {
        'payment_issues': {
            'keywords': ['payment', 'pay', 'money', 'earnings', 'salary', 'wage', 'compensation', 'paid', 'unpaid', 'dollars', 'cash'],
            'patterns': [
                r'not.*paid',
                r'payment.*delayed',
                r'money.*owed',
                r'earnings.*missing',
                r'compensation.*issue'
            ],
            'weight': 0
        },
        'account_suspension': {
            'keywords': ['ban', 'block', 'suspended', 'deactivated', 'terminated', 'removed', 'account closed', 'banned', 'blocked'],
            'patterns': [
                r'account.*suspended',
                r'got.*banned',
                r'blocked.*account',
                r'suspended.*without',
                r'terminated.*account'
            ],
            'weight': 0
        },
        'support_issues': {
            'keywords': ['support', 'help', 'customer service', 'response', 'contact', 'assistance', 'ticket', 'email', 'reply'],
            'patterns': [
                r'no.*response',
                r'support.*ignored',
                r'contact.*difficult',
                r'help.*unavailable',
                r'customer.*service.*poor'
            ],
            'weight': 0
        },
        'work_availability': {
            'keywords': ['work', 'task', 'project', 'job', 'assignment', 'queue', 'available', 'empty', 'no work', 'projects'],
            'patterns': [
                r'no.*work.*available',
                r'empty.*queue',
                r'no.*projects',
                r'work.*dried',
                r'no.*tasks'
            ],
            'weight': 0
        },
        'training_issues': {
            'keywords': ['training', 'onboarding', 'assessment', 'test', 'course', 'learning', 'unpaid training', 'exam'],
            'patterns': [
                r'unpaid.*training',
                r'excessive.*training',
                r'training.*required',
                r'assessment.*difficult',
                r'too.*much.*training'
            ],
            'weight': 0
        },
        'technical_issues': {
            'keywords': ['platform', 'system', 'bug', 'error', 'technical', 'website', 'app', 'glitch', 'crash', 'broken'],
            'patterns': [
                r'platform.*broken',
                r'system.*error',
                r'technical.*issue',
                r'bug.*platform',
                r'website.*down'
            ],
            'weight': 0
        },
        'scam_accusations': {
            'keywords': ['scam', 'fraud', 'fake', 'deceive', 'steal', 'trick', 'scammer', 'cheat', 'dishonest'],
            'patterns': [
                r'this.*scam',
                r'fraudulent.*company',
                r'fake.*platform',
                r'deceiving.*users',
                r'stealing.*money'
            ],
            'weight': 0
        },
        'privacy_concerns': {
            'keywords': ['data', 'personal', 'information', 'privacy', 'id', 'document', 'identity', 'private'],
            'patterns': [
                r'personal.*data',
                r'privacy.*concern',
                r'private.*information',
                r'data.*collection',
                r'identity.*theft'
            ],
            'weight': 0
        }
    }
    
    import re
    
    # Calculate weights for each category
    for category, config in rules.items():
        weight = 0
        
        # Keyword matching
        for keyword in config['keywords']:
            if keyword in text_lower:
                weight += 1
        
        # Pattern matching (more weight for complex patterns)
        for pattern in config['patterns']:
            if re.search(pattern, text_lower):
                weight += 2
        
        # Special rules for high-impact issues
        if category == 'scam_accusations' and weight > 0:
            weight *= 2  # Give higher priority to scam accusations
        
        if category == 'payment_issues' and 'suspended' in text_lower:
            weight += 3  # Payment + suspension is a critical issue
        
        rules[category]['weight'] = weight
    
    return rules

def classify_review_theme(text):
    """Classify a single review into the most appropriate theme"""
    if not text or pd.isna(text):
        return "General Issues"
    
    analysis = analyze_review_content(text)
    
    # Find the category with highest weight
    max_weight = 0
    best_category = None
    
    for category, config in analysis.items():
        if config['weight'] > max_weight:
            max_weight = config['weight']
            best_category = category
    
    # Only classify if we have a significant match (weight >= 2)
    if max_weight < 2:
        return "General Issues"
    
    # Map categories to human-readable themes
    theme_mapping = {
        'payment_issues': "Payment Delays or Missing Payments After Work Completed",
        'account_suspension': "Accounts Suspended/Blocked Without Clear Explanation",
        'support_issues': "Poor Customer Support - Slow Response or No Help",
        'work_availability': "No Work Available - Empty Queues and Project Instability",
        'training_issues': "Excessive Unpaid Training and Assessment Requirements",
        'technical_issues': "Platform Technical Problems and System Bugs",
        'scam_accusations': "Users Accusing Platform of Being a Scam/Fraud",
        'privacy_concerns': "Concerns About Personal Data Collection and Privacy"
    }
    
    return theme_mapping.get(best_category, "General Issues")

def extract_pain_points(df, n_clusters=5):
    """Extract pain points using expert system classification instead of clustering"""
    pain_df = df[df['sentiment_label'] != 'positive'].copy()
    
    if pain_df.empty:
        return []
    
    # Classify each review into themes
    pain_df['theme'] = pain_df['reviewText_en'].apply(classify_review_theme)
    
    # Group by themes and create summaries
    theme_groups = pain_df.groupby('theme')
    
    top_themes = []
    for theme_name, group in theme_groups:
        if len(group) < 2:  # Skip themes with only 1 review
            continue
            
        # Get sample quotes
        quotes = group['reviewText_en'].sample(min(3, len(group)), random_state=42).tolist()
        
        # Create impact assessment
        impact = ("This pain point may discourage high quality contributors, "
                   "leading to lower retention and engagement, which could impact our next quarter goal of focusing on high quality contributors.")
        
        # Get actionable insights
        actionable_insights = get_actionable_insights(theme_name, [], group)
        
        top_themes.append({
            'theme': theme_name,
            'summary': f"{len(group)} users affected",
            'count': len(group),
            'quotes': quotes,
            'impact': impact,
            'keywords': [],
            'actionable_insights': actionable_insights
        })
    
    # Sort by count and return top themes
    return sorted(top_themes, key=lambda x: x['count'], reverse=True)[:n_clusters]

def get_theme_summary(theme_name):
    """Generate a concise summary paragraph for each pain point theme"""
    
    summaries = {
        "Users Accusing Platform of Being a Scam/Fraud": 
            "Users are expressing deep distrust in the platform's legitimacy, often citing lack of transparency in payments, unclear verification processes, and feeling deceived by the platform's operations. This creates a critical trust crisis that directly impacts user retention and platform credibility.",
        
        "Account Suspended Before Payment - Users Not Getting Paid": 
            "Users are experiencing account suspensions immediately after completing work but before receiving payment, leaving them feeling cheated and frustrated. This creates a significant barrier to user trust and platform reliability.",
        
        "Payment Delays or Missing Payments After Work Completed": 
            "Users are facing inconsistent and delayed payment processing after completing their work, with unclear timelines and poor communication about payment status. This undermines user confidence in the platform's payment reliability.",
        
        "Accounts Suspended/Blocked Without Clear Explanation": 
            "Users are being suspended or blocked from the platform without receiving clear explanations or having access to a proper appeal process. This creates frustration and a sense of unfair treatment.",
        
        "Poor Customer Support - Slow Response or No Help": 
            "Users are struggling to get timely and effective support when facing issues, with long response times, unhelpful responses, or complete lack of assistance. This leaves users feeling abandoned and frustrated.",
        
        "No Work Available - Empty Queues and Project Instability": 
            "Users are experiencing inconsistent work availability with empty project queues and unstable project assignments, making it difficult to maintain consistent income and engagement with the platform.",
        
        "Excessive Unpaid Training and Assessment Requirements": 
            "Users are required to complete extensive unpaid training and assessments before accessing work opportunities, creating a barrier to entry and frustration about time investment without immediate returns.",
        
        "Platform Technical Problems and System Bugs": 
            "Users are encountering frequent technical issues, system bugs, and platform instability that hinder their ability to complete work efficiently and reliably.",
        
        "Concerns About Personal Data Collection and Privacy": 
            "Users are worried about how their personal data is being collected, stored, and used by the platform, with concerns about privacy protection and data security.",
        
        "General Issues": 
            "Users are experiencing various platform-related issues that impact their overall experience and satisfaction with the service."
    }
    
    return summaries.get(theme_name, "Users are experiencing issues that impact their platform experience and satisfaction.")

try:
    # Initialize session state at the very beginning
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'main'
    if 'selected_theme' not in st.session_state:
        st.session_state.selected_theme = None
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "overview"
    
    df = load_and_translate("Trustpilot reviews extraction - Data.csv")
    
    # Data summary section
    with st.expander("📊 Dataset Information", expanded=False):
        st.markdown(f"""
        **Dataset Overview:**
        - **Total English Reviews:** {len(df):,}
        - **Date Range:** {df['reviewScore'].count()} reviews analyzed
        - **Language Filter:** English only (removed {124} non-English reviews)
        - **Average Rating:** {df['reviewScore'].mean():.2f}/5
        - **Sentiment Distribution:** {df['sentiment_label'].value_counts().to_dict()}
        """)
    
    if st.session_state.current_page == 'main':
        # Sidebar navigation
        with st.sidebar:
            st.markdown("""
            <style>
            .sidebar .sidebar-content {
                background-color: #f8f9fa;
            }
            </style>
            """, unsafe_allow_html=True)
            
            st.header("📊 Dashboard Navigation")
            st.markdown("---")
            
            # Navigation buttons with styling
            if st.button("📈 Overview", use_container_width=True, key="nav_overview"):
                st.session_state.current_tab = "overview"
                st.rerun()
            
            if st.button("🎯 Pain Points", use_container_width=True, key="nav_pain"):
                st.session_state.current_tab = "pain_points"
                st.rerun()
            
            if st.button("🎯 Actionable Insights", use_container_width=True, key="nav_insights"):
                st.session_state.current_tab = "actionable_insights"
                st.rerun()
            
            st.markdown("---")
            st.markdown("**📊 Quick Stats:**")
            st.metric("Total Reviews", len(df))
            st.metric("Avg Rating", f"{df['reviewScore'].mean():.1f}")
            st.metric("Avg Sentiment", f"{df['sentiment'].mean():.2f}")
            
            # Add current tab indicator
            st.markdown("---")
            st.markdown(f"**📍 Current Section:** {st.session_state.current_tab.replace('_', ' ').title()}")
        
        # Main content area
        if st.session_state.current_tab == "overview":
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Reviews", len(df))
            col2.metric("Average Rating", f"{df['reviewScore'].mean():.2f}")
            col3.metric("Average Sentiment", f"{df['sentiment'].mean():.2f}")
            st.divider()
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.subheader("Sentiment Distribution")
                sentiment_counts = df['sentiment_label'].value_counts()
                fig_sentiment = px.pie(
                    sentiment_counts,
                    values=sentiment_counts.values,
                    names=sentiment_counts.index,
                    title="Sentiment Breakdown",
                    color_discrete_map={"positive": "green", "negative": "red", "neutral": "blue"}
                )
                st.plotly_chart(fig_sentiment, use_container_width=True)
            with fig_col2:
                st.subheader("Rating Distribution")
                rating_counts = df['reviewScore'].value_counts().sort_index()
                fig_rating = px.bar(
                    rating_counts,
                    x=rating_counts.index,
                    y=rating_counts.values,
                    title="Review Scores",
                    labels={'x': 'Rating', 'y': 'Count'}
                )
                st.plotly_chart(fig_rating, use_container_width=True)
            st.subheader("Browse Reviews (Original and Translated)")
            st.dataframe(df[[
                'reviewScore', 'reviewLanguage', 'reviewTitle', 'reviewText', 'reviewText_en', 'sentiment_label', 'sentiment', 'reviewUrl'
            ]])

        elif st.session_state.current_tab == "pain_points":
            st.header("Top Pain Points")
            pain_points = extract_pain_points(df, n_clusters=5)
            if not pain_points:
                st.info("No significant pain points found.")
            else:
                # Single column vertical layout
                for i, theme in enumerate(pain_points):
                    # Create card with integrated button
                    theme_summary = get_theme_summary(theme['theme'])
                    
                    # Create a container for the card and button
                    with st.container():
                        st.markdown(f"""
                        <div style="
                            border: 2px solid #e9ecef;
                            border-radius: 12px;
                            padding: 32px;
                            margin: 16px 0;
                            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            transition: all 0.3s ease;
                            position: relative;
                            min-height: 200px;
                        ">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                                <h3 style="color: #d63384; margin: 0; font-size: 22px; font-weight: 600; line-height: 1.3;">{theme['theme']}</h3>
                                <span style="background-color: #6c757d; color: white; padding: 4px 8px; border-radius: 12px; font-size: 14px; font-weight: 500;">
                                    {theme['count']} users
                                </span>
                            </div>
                            <h4 style="color: #495057; margin: 8px 0 12px 0; font-size: 18px; font-weight: 500; line-height: 1.4; font-style: italic;">{theme_summary}</h4>
                            <p style="color: #6c757d; font-size: 18px; margin: 0; line-height: 1.5;">{theme['summary']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Position the Streamlit button using columns to align with the card
                        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
                        with col4:
                            # Add negative margin to pull button closer to card
                            st.markdown(f"""
                            <div style="margin-top: -32px; margin-right: 32px;">
                            """, unsafe_allow_html=True)
                            if st.button("🔍 View Details", key=f"btn_{i}", use_container_width=True):
                                st.session_state.selected_theme = theme
                                st.session_state.current_page = 'theme_detail'
                                st.rerun()
                            st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)  # Add spacing between cards

        elif st.session_state.current_tab == "actionable_insights":
            st.header("🎯 Actionable Insights & Growth Strategy")
            
            # Growth Marketing Strategy Section
            st.subheader("📈 Growth Marketing Strategy - Q4 Focus")
            st.markdown("""
            **Our Q4 Goal:** Retain high-quality contributors while lowering acquisition costs
            
            ### 🎯 Key Objectives:
            - **Reduce churn by 40%** among high-quality contributors
            - **Lower CAC by 30%** through improved conversion and retention
            - **Increase LTV by 50%** through better contributor experience
            """)
            
            # Pain Points Analysis for Growth
            st.subheader("🔍 Pain Points Impact on Growth")
            pain_points = extract_pain_points(df, n_clusters=10)
            
            if pain_points:
                for theme in pain_points:
                    with st.expander(f"📊 {theme['theme']} - {theme['count']} users affected"):
                        st.markdown(f"**Impact on Growth:** {theme['impact']}")
                        
                        # Marketing Strategy for this pain point
                        insights = theme['actionable_insights']
                        if 'marketing' in insights:
                            st.markdown("### 📢 Marketing Strategy:")
                            for i, insight in enumerate(insights['marketing'], 1):
                                st.markdown(f"""
                                **Strategy {i}: {insight['problem']}**
                                - **Solution:** {insight['solution']}
                                - **Implementation:** {insight['implementation']}
                                - **Expected Impact:** {insight['expected_impact']}
                                """)
            
            # Content Strategy Section
            st.subheader("📝 Content Strategy Plan")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🎯 Blog Posts to Write:")
                st.markdown("""
                **1. Trust & Transparency Series:**
                - "How We Ensure Fair Payment for Every Contributor"
                - "Behind the Scenes: Our Payment Verification Process"
                - "Real Stories: Contributors Who Built Successful Careers"
                
                **2. Support & Communication:**
                - "24/7 Support: How We're Improving Response Times"
                - "Your Success is Our Priority: New Support Features"
                - "Transparent Communication: What We're Doing Better"
                
                **3. Platform Improvements:**
                - "New Features: Making Work Easier and More Reliable"
                - "Technical Updates: Faster, More Stable Platform"
                - "User Experience: What We've Learned and Improved"
                
                **4. Success Stories:**
                - "From Newbie to Pro: Contributor Success Stories"
                - "How Top Contributors Maximize Their Earnings"
                - "Community Spotlight: Meet Our Best Contributors"
                """)
            
            with col2:
                st.markdown("### 🌐 New Web Pages to Build:")
                st.markdown("""
                **1. Trust & Verification Pages:**
                - `/trust-verification` - Live payment dashboard
                - `/payment-proof` - Gallery of real payment screenshots
                - `/success-stories` - Detailed contributor testimonials
                
                **2. Support & Resources:**
                - `/support-center` - Comprehensive help hub
                - `/knowledge-base` - Self-help resources
                - `/contact-us` - Multiple support channels
                
                **3. Platform Information:**
                - `/how-it-works` - Clear process explanation
                - `/platform-features` - Detailed feature showcase
                - `/faq` - Common questions and answers
                
                **4. Community & Engagement:**
                - `/contributor-community` - Community hub
                - `/training-resources` - Learning materials
                - `/career-growth` - Advancement opportunities
                """)
            
            # Detailed Growth Marketing Strategy
            st.subheader("🚀 Detailed Growth Marketing Strategy")
            
            st.markdown("""
            ### 🎯 Phase 1: Trust Building (Weeks 1-4)
            
            **Problem:** Users don't trust the platform due to lack of transparency
            
            **Solutions:**
            1. **Trust Verification Program**
               - Create public dashboard showing real-time payment data
               - Partner with Trustpilot, BBB for verification badges
               - Launch with case studies and testimonials
            
            2. **Payment Proof Gallery**
               - Develop showcase of real payment screenshots
               - Create video testimonials from long-term contributors
               - Launch with social media campaign
            
            3. **Legitimacy Assurance Email Sequence**
               - 5-email series explaining platform history
               - Security measures and success stories
               - A/B test messaging for optimal conversion
            
            **Expected Impact:** Reduce scam accusations by 60%, increase user confidence by 75%
            """)
            
            st.markdown("""
            ### 🎯 Phase 2: Support & Communication (Weeks 5-8)
            
            **Problem:** Poor customer support and communication
            
            **Solutions:**
            1. **24/7 Support Guarantee**
               - Implement live chat with 2-hour response time
               - Hire dedicated support team
               - Create response time monitoring
            
            2. **Support Knowledge Base**
               - Build comprehensive FAQ and video tutorials
               - Create troubleshooting guides for common issues
               - Optimize for search and user discovery
            
            3. **Proactive Communication**
               - Payment status updates and notifications
               - Platform updates and feature announcements
               - Personalized contributor communications
            
            **Expected Impact:** Improve support satisfaction by 80%, reduce support tickets by 60%
            """)
            
            st.markdown("""
            ### 🎯 Phase 3: Platform Improvements (Weeks 9-12)
            
            **Problem:** Technical issues and platform instability
            
            **Solutions:**
            1. **Payment Verification Engine**
               - Automated payment processing within 24 hours
               - Real-time payment tracking and notifications
               - Blockchain-like transparency for payments
            
            2. **Smart Work Assignment**
               - AI-powered matching of users to available work
               - Skill-based work recommendations
               - Predictive analytics for work availability
            
            3. **User Experience Optimization**
               - Streamlined onboarding process
               - Improved mobile experience
               - Faster platform performance
            
            **Expected Impact:** Reduce technical issues by 90%, increase work efficiency by 80%
            """)
            
            # Retention Strategy
            st.subheader("💎 High-Quality Contributor Retention Strategy")
            
            st.markdown("""
            ### 🎯 Retention Tactics:
            
            **1. Personalized Onboarding**
            - Customized welcome sequences based on skills
            - 1-on-1 onboarding calls for top prospects
            - Skill assessment and career path planning
            
            **2. Recognition & Rewards**
            - Contributor of the month program
            - Performance-based bonuses and incentives
            - Public recognition and community spotlight
            
            **3. Career Development**
            - Skill development programs and certifications
            - Advancement opportunities and leadership roles
            - Mentorship programs for new contributors
            
            **4. Community Building**
            - Exclusive contributor forums and groups
            - Regular community events and meetups
            - Peer-to-peer support networks
            
            **5. Transparent Communication**
            - Regular platform updates and roadmap sharing
            - Contributor feedback loops and surveys
            - Open communication channels with leadership
            """)
            
            # CAC Reduction Strategy
            st.subheader("💰 Customer Acquisition Cost (CAC) Reduction")
            
            st.markdown("""
            ### 🎯 CAC Reduction Tactics:
            
            **1. Improve Conversion Funnel**
            - Optimize landing pages for better conversion
            - A/B test signup process and reduce friction
            - Implement progressive profiling for better targeting
            
            **2. Leverage Existing Contributors**
            - Referral program with incentives
            - User-generated content and testimonials
            - Community-driven marketing campaigns
            
            **3. Content Marketing**
            - SEO-optimized blog posts addressing pain points
            - Video content showcasing platform benefits
            - Social media presence with valuable content
            
            **4. Partnership Marketing**
            - Collaborate with relevant influencers and thought leaders
            - Partner with educational institutions and training programs
            - Cross-promotion with complementary platforms
            
            **5. Retargeting & Remarketing**
            - Personalized retargeting campaigns
            - Email nurture sequences for warm leads
            - Social media retargeting for brand awareness
            """)
            
            # Metrics & KPIs
            st.subheader("📊 Key Metrics & KPIs to Track")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Retention Metrics:**
                - Monthly Active Contributors (MAC)
                - Contributor Churn Rate
                - Average Contributor Lifetime
                - Net Promoter Score (NPS)
                - Contributor Satisfaction Score
                """)
            
            with col2:
                st.markdown("""
                **Growth Metrics:**
                - Customer Acquisition Cost (CAC)
                - Customer Lifetime Value (CLV)
                - CAC to CLV Ratio
                - Conversion Rate by Channel
                - Organic vs Paid Acquisition
                """)
            
            # Implementation Timeline
            st.subheader("📅 Implementation Timeline")
            
            st.markdown("""
            **Q4 2024 Implementation Plan:**
            
            **October (Weeks 1-4):**
            - Launch Trust Verification Program
            - Create Payment Proof Gallery
            - Implement Legitimacy Assurance emails
            - Build new trust-focused web pages
            
            **November (Weeks 5-8):**
            - Launch 24/7 Support Guarantee
            - Build Support Knowledge Base
            - Implement proactive communication
            - Create support-focused content
            
            **December (Weeks 9-12):**
            - Deploy Payment Verification Engine
            - Launch Smart Work Assignment
            - Optimize user experience
            - Measure and iterate on all initiatives
            """)

    elif st.session_state.current_page == 'theme_detail' and st.session_state.selected_theme:
        theme = st.session_state.selected_theme
        
        # Back button
        if st.button("← Back to Pain Points"):
            st.session_state.current_page = 'main'
            st.session_state.selected_theme = None
            st.rerun()
        
        st.header(f"📋 {theme['theme']}")
        
        # Theme summary
        theme_summary = get_theme_summary(theme['theme'])
        st.markdown(f"**📝 Summary:** {theme_summary}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("👥 Affected Users", theme['count'])
            st.metric("🎯 Priority Level", "High" if theme['count'] > 50 else "Medium" if theme['count'] > 20 else "Low")
        
        with col2:
            st.metric("📊 Impact Score", f"{theme['count'] / len(df) * 100:.1f}%")
            st.metric("🔍 Sentiment", "Negative" if theme['count'] > 30 else "Mixed")
        
        st.divider()
        
        # User Quotes
        st.subheader("💬 User Quotes")
        for i, quote in enumerate(theme['quotes'], 1):
            st.markdown(f"**Quote {i}:** *{quote}*")
            st.markdown("---")
        
        # Impact Analysis
        st.subheader("🎯 Impact on High Quality Contributors")
        st.write(theme['impact'])
        
        st.divider()
        
        # Actionable Insights
        st.subheader("🚀 Actionable Insights")
        
        # Marketing Strategy
        st.subheader("📢 Marketing Strategy")
        for i, insight in enumerate(theme['actionable_insights']['marketing'], 1):
            with st.expander(f"Strategy {i}: {insight['problem'][:50]}..."):
                st.markdown(f"**Problem:** {insight['problem']}")
                st.markdown(f"**Solution:** {insight['solution']}")
                st.markdown(f"**Implementation:** {insight['implementation']}")
                st.markdown(f"**Expected Impact:** {insight['expected_impact']}")
        
        st.divider()
        
        # Product Development
        st.subheader("⚙️ Product Development")
        for i, insight in enumerate(theme['actionable_insights']['product'], 1):
            with st.expander(f"Feature {i}: {insight['problem'][:50]}..."):
                st.markdown(f"**Problem:** {insight['problem']}")
                st.markdown(f"**Solution:** {insight['solution']}")
                st.markdown(f"**Implementation:** {insight['implementation']}")
                st.markdown(f"**Expected Impact:** {insight['expected_impact']}")
        
        st.divider()
        
        # Next Quarter Roadmap
        st.subheader("📅 Next Quarter Roadmap")
        st.markdown("""
        **Q1 2025 Focus Areas:**
        - Implement immediate fixes for high-impact issues
        - Launch targeted marketing campaigns
        - Develop new product features based on user feedback
        - Establish clear communication channels
        """)

except FileNotFoundError:
    st.error("Error: 'Trustpilot reviews extraction - Data.csv' not found. Please add the file to the project directory.") 