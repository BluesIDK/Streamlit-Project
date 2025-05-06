# The URL to my streamlit App: https://app-project-cfpahedgbgy5ykf36a2cma.streamlit.app/ 

# 🌍 Financial Inclusion in Africa — ML Classifier + Streamlit App

This project was built as part of a data science checkpoint, using the **Financial Inclusion in Africa** dataset provided by Zindi. The goal? Train a machine learning model that predicts whether an individual is likely to have a bank account — based on their demographics, job, education, and other factors.

No overhyped storytelling here — just a solid, hands-on application of machine learning, data wrangling, and Streamlit deployment. Think of it as a technical playground where I practiced key data science skills and turned them into something visual and interactive.

Whether you’re here to check the code, play with the app, or just curious about ML in social contexts — welcome!

The dataset includes data on **33,600+ individuals** from across East Africa — covering their demographics, education, location, job type, and more.

> ⚡ Financial inclusion = ensuring people and businesses have access to affordable and useful financial services — like payments, savings, credit, and insurance — delivered responsibly and sustainably.

---

## 📚 What I Did 

Let’s break down the journey:

### 🧹 Data Exploration & Cleaning
- Loaded and explored the dataset in-depth
- Identified missing values, outliers, and inconsistencies
- Visualized distributions and relationships using heatmaps and pair plots
- Cleaned, encoded, and structured the data using best practices from both Kaggle pros and research papers

### 📊 Feature Engineering
- Label encoding for target variable
- One-hot encoding for categorical features
- Normalized skewed distributions
- Investigated correlations with the target (`bank_account`)

### 🧠 Model Training & Evaluation
- Split the data into training/testing sets
- Tried several models: Logistic Regression, Decision Trees, Random Forest, XGBoost
- Tuned hyperparameters and evaluated using **accuracy, precision, recall, and F1-score**
- Selected the best-performing model (Random Forest was 🔥 in my case)

### 🖥️ Streamlit App (because models deserve a stage)
- Created an interactive Streamlit interface for users to input values
- Added a prediction button that returns whether the person is likely to have a bank account
- Tested extensively to ensure predictions matched model output
- Deployed on [Streamlit Share](https://streamlit.io/sharing) for real-time use

---


## 🧾 Columns Explanation

The dataset includes features like:
- `country`: Country of the individual (e.g., Kenya, Rwanda)
- `year`: Year data was collected
- `location_type`: Urban or rural
- `cellphone_access`: Whether the individual has a phone
- `education_level`: Highest education level achieved
- `job_type`: Type of employment
- `bank_account`: (Target) Does the person have a bank account?

Full column breakdown with examples is included in the notebook.

---

## ⚒️ Tools & Technologies Used

- **Python** 🐍  
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**  
- **Scikit-learn**, **XGBoost**, **RandomForestClassifier**  
- **Streamlit** for app deployment  
- **GitHub** for version control  
- **Zindi** dataset for real-world context

---

## 🎓 What I Learned

This wasn’t just a coding exercise — it was a lesson in:
- Applying ML to socially relevant problems
- Interpreting data with *human* context in mind
- Communicating insights clearly to both technical and non-technical users
- Taking a project from idea → model → app → deployment (end-to-end mastery)

---

## 🔍 Key Insights & Takeaways

- **Financial inclusion in East Africa is uneven**: Only around 44% of individuals in the dataset have access to a bank account. Rwanda, Tanzania, and Uganda show lower inclusion rates compared to Kenya, which leads in access.

- **Gender matters a lot**: Men are significantly more likely to have a bank account than women. The gap can be as wide as 20% in some regions — reflecting deeper societal, cultural, and economic inequalities.

- **Urban residents dominate financial access**: Urban individuals are more than twice as likely to have a bank account compared to rural individuals. The lack of infrastructure and formal employment in rural areas plays a major role.

- **Type of job = access level**: People employed in the formal sector (government/private) have the highest financial inclusion rates, while those in informal, self-employed, or unemployed categories are much less likely to be banked.

- **"Relationship with head of household" reveals social dynamics**: Individuals who are themselves the head of the household are more likely to have a bank account. Spouses, children, or other relatives — especially in patriarchal setups — tend to have reduced access.

- **Education is a strong predictor**: Those with tertiary or secondary education are much more likely to be banked. In contrast, individuals with no formal education are significantly underrepresented in financial systems.

- **Age sweet spot**: People aged between 25 and 44 are most likely to have a bank account — likely due to job stability and active economic participation. Very young (under 20) and elderly (60+) groups show lower access.

- **Household size has marginal influence**: Slight trends show that people in smaller households are more likely to be financially included — possibly linked to income concentration and decision-making power.

- **Missing data isn’t random**: Many of the missing or unknown entries cluster around rural, female, or unemployed groups — reinforcing the idea that **data absence can reflect real-world marginalization**.

- **Machine learning model accuracy**: After cleaning and preprocessing, the best-performing classifier (e.g., Random Forest or XGBoost) reached around **83–85% accuracy** on the test set. Top features influencing predictions included `education_level`, `job_type`, `location_type`, and `relationship_with_head`.



