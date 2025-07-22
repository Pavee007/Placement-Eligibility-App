# 🎓 Placement Eligibility App

A Streamlit web app to evaluate student placement eligibility based on custom criteria and visualize key performance insights.

---

## 📌 Features

- 🎯 Filter eligible students by programming & soft skills metrics
- 📊 Visual insights (charts + SQL-based analytics)
- 📂 SQLite-backed database with realistic data using Faker
- 🧱 Modular, clean code using Object-Oriented Programming

---

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Faker
- Pandas
- Altair (for charts)

---

## 📁 Project Structure

```
placement_eligibility_app/
├── app.py              # Streamlit frontend
├── database.py         # OOP-based DB operations
├── data_generator.py   # Faker-based synthetic data creation
├── queries.py          # SQL queries for insights
├── requirements.txt    # Python dependencies
├── placement.db        # Prebuilt SQLite database (optional)
└── README.md
```

---

## ▶️ How to Run Locally

1. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**
   ```bash
   streamlit run app.py
   ```

3. **(Optional)** Generate a fresh database:
   ```bash
   python data_generator.py
   ```

---

## 📊 Example Queries Visualized

- Average programming score by batch
- Placement status distribution
- Top 5 interview performers
- City-wise student count

---

## 🙋‍♂️ Author

Developed by **Pavith Kumar** with ❤️  
Feel free to fork or star this project!

---

## 📄 License

This project is licensed under the MIT License.
