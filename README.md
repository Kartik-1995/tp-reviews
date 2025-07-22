# Trustpilot Review Analysis Dashboard

A comprehensive Streamlit dashboard for analyzing Trustpilot reviews, extracting pain points, and providing actionable insights for growth marketing strategies.

## 🚀 Features

- **📊 Overview Dashboard**: Sentiment analysis, rating distribution, and review browsing
- **🎯 Pain Points Analysis**: Expert system-based theme detection and categorization
- **📈 Actionable Insights**: Growth marketing strategy with detailed implementation plans
- **🌍 Multi-language Support**: Automatic translation of non-English reviews
- **💡 Content Strategy**: Blog post ideas and web page recommendations

## 📋 Requirements

- Python 3.8+
- Streamlit
- Pandas
- Plotly
- TextBlob
- googletrans

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd test2
```

2. **Create a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the dashboard:**
```bash
streamlit run dashboard.py
```

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub:**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Deploy!

### Option 2: Heroku

1. **Create Procfile:**
```
web: streamlit run dashboard.py --server.port=$PORT --server.address=0.0.0.0
```

2. **Deploy:**
```bash
heroku create your-app-name
git push heroku main
```

### Option 3: Railway

1. **Connect to Railway:**
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Deploy automatically

### Option 4: Google Cloud Run

1. **Create Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. **Deploy:**
```bash
gcloud run deploy --source .
```

## 📁 File Structure

```
test2/
├── dashboard.py          # Main dashboard application
├── requirements.txt      # Python dependencies
├── README.md           # This file
└── Trustpilot reviews extraction - Data.csv  # Your data file
```

## 🔧 Configuration

The dashboard expects a CSV file named `Trustpilot reviews extraction - Data.csv` with the following columns:
- `reviewScore`: Rating (1-5)
- `reviewLanguage`: Language code (en, es, fr, etc.)
- `reviewTitle`: Review title
- `reviewText`: Review content
- `reviewUrl`: Review URL

## 📊 Dashboard Sections

### Overview Tab
- Key metrics and statistics
- Sentiment distribution charts
- Rating distribution analysis
- Review browsing interface

### Pain Points Tab
- Expert system-based theme detection
- Categorized pain points with user counts
- Detailed theme analysis with actionable insights
- Interactive cards with "View Details" functionality

### Actionable Insights Tab
- Growth marketing strategy for Q4
- Content strategy plan (blog posts + web pages)
- 3-phase implementation timeline
- High-quality contributor retention strategy
- CAC reduction tactics
- Key metrics and KPIs

## 🎯 Key Features

- **Expert System**: Rule-based theme detection using keywords and patterns
- **Multi-language Support**: Automatic translation of non-English reviews
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Charts**: Plotly-based visualizations
- **Session State Management**: Persistent navigation and user state

## 📈 Growth Marketing Focus

The dashboard is specifically designed to help with:
- **Retaining high-quality contributors** (40% churn reduction target)
- **Lowering acquisition costs** (30% CAC reduction target)
- **Increasing lifetime value** (50% LTV increase target)

## 🤝 Sharing with Team

Once deployed, you can share the dashboard URL with your teammates. They'll be able to:
- View all pain points and insights
- Access the growth marketing strategy
- See the content strategy recommendations
- Explore the implementation timeline

## 🔒 Security Notes

- The dashboard is read-only and doesn't store any user data
- All analysis is performed on the provided CSV data
- No sensitive information is transmitted or stored

## 📞 Support

For issues or questions:
1. Check the deployment logs
2. Verify the CSV file format
3. Ensure all dependencies are installed
4. Check the Streamlit documentation for troubleshooting

---

**Built with ❤️ using Streamlit** 