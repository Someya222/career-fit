
# Career Fit Predictor

Career Fit Predictor is an interactive Streamlit application that maps personality traits and work preferences to career archetypes using a TensorFlow neural network.

## Features

- 12-question personality assessment
- Big Five personality trait analysis
- Eight career archetype classifications
- Top career recommendations
- Archetype probability comparison
- Big Five radar chart
- Burnout risk and alignment scores
- Team-role recommendations
- Interactive technical statistics dashboard

## Career Archetypes

- Researcher
- Entrepreneur
- Leader
- Helper
- Analyst
- Creator
- Strategist
- Builder

## Screenshots
<img width="1918" height="981" alt="Screenshot 2026-04-15 005231" src="https://github.com/user-attachments/assets/95c89668-4cb7-4eef-ad7e-f3841fb7ec29" />
<img width="1572" height="986" alt="Screenshot 2026-04-15 005301" src="https://github.com/user-attachments/assets/6631965a-b370-42c1-a812-d6f92ea84ec5" />
<img width="1919" height="985" alt="Screenshot 2026-04-15 005348" src="https://github.com/user-attachments/assets/65904faf-d063-41b5-b68b-278c4e0d5085" />




## Technology Stack

- Python
- Streamlit
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- Pillow

## Project Structure

```text
career-fit-final/
├── app.py
├── requirements.txt
├── test_model.py
├── data/
│   ├── big_five_data.csv
│   └── onet_careers.csv
├── models/
│   ├── career_fit_model.h5
│   ├── label_encoder.pkl
│   ├── scaler.pkl
│   ├── accuracy_curve.png
│   ├── confusion_matrix.png
│   └── loss_curve.png
├── pages/
│   ├── results.py
│   └── stats.py
└── src/
    ├── feature_engineering.py
    ├── predict.py
    ├── theme.py
    └── utils.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Someya222/career-fit.git
cd career-fit
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed by Streamlit, usually:

```text
http://localhost:8501
```

## How It Works

1. The user answers 12 Likert-scale career and personality questions.
2. Responses are converted into personality, intelligence, values, and alignment features.
3. The first five Big Five features are scaled using the saved `StandardScaler`.
4. The TensorFlow model predicts probabilities for eight career archetypes.
5. The application selects the highest-probability archetype.
6. Career options are retrieved from `data/onet_careers.csv`.

The application uses 16 engineered features internally, including:

- Openness
- Conscientiousness
- Extraversion
- Agreeableness
- Neuroticism
- Logical intelligence
- Spatial intelligence
- Interpersonal intelligence
- Autonomy need
- Collaboration need
- Purpose value
- Money value
- Energy alignment
- Values alignment
- Growth potential
- Burnout risk

## Model Testing

Run the included profile test script:

```bash
python test_model.py
```

It evaluates four example personality profiles:

- Researcher
- Entrepreneur
- Leader
- Helper

## Technical Dashboard

The **Stats** page displays:

- Model accuracy
- F1 score
- Test loss
- Dataset size
- Accuracy and loss curves
- Confusion matrix
- Model architecture
- Data-processing pipeline

## Data

- `big_five_data.csv` contains Big Five personality records.
- `onet_careers.csv` maps career archetypes to recommended careers.
- Pretrained model and preprocessing artifacts are stored in `models/`.

## Disclaimer

This application is intended as an educational career exploration tool. Its predictions should not be treated as professional psychological, recruitment, or employment advice.
