# ============================================
# LOGISTICS DELIVERY TIME PREDICTION
# ============================================

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# 1. Load data
df = pd.read_csv("logistics_data.csv")

# 2. Define target and features
X = df.drop(columns="Delivery_Time_min")
y = df["Delivery_Time_min"]

categorical_features = [
    "Order_Priority",
    "Vehicle_Type",
    "Day_of_Week"
]

numeric_features = [
    "Distance_km",
    "Package_Weight_kg",
    "Traffic_Index",
    "Weather_Score",
    "Warehouse_Load_pct"
]

# 3. Preprocessing
preprocessor = ColumnTransformer([
    ("numeric", StandardScaler(), numeric_features),
    ("categorical",
     OneHotEncoder(handle_unknown="ignore"),
     categorical_features)
])

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42
)

# 5. Models
models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        max_depth=8,
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=250,
        max_depth=12,
        min_samples_leaf=3,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )
}

# 6. Train and evaluate
results = []

for name, model in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    prediction = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, prediction)
    rmse = np.sqrt(
        mean_squared_error(y_test, prediction)
    )
    r2 = r2_score(y_test, prediction)

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    })

results_df = pd.DataFrame(results)
print(results_df.sort_values("RMSE"))

# 7. Five-fold cross-validation
selected_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

rmse_scores = np.sqrt(
    -cross_val_score(
        selected_pipeline,
        X,
        y,
        scoring="neg_mean_squared_error",
        cv=cv
    )
)

print("Mean CV RMSE:", rmse_scores.mean())
print("Std CV RMSE:", rmse_scores.std())

# 8. Train final model
selected_pipeline.fit(X, y)

# 9. Predict a new shipment
new_shipment = pd.DataFrame([{
    "Distance_km": 200,
    "Package_Weight_kg": 10,
    "Traffic_Index": 60,
    "Weather_Score": 4,
    "Warehouse_Load_pct": 60,
    "Order_Priority": "High",
    "Vehicle_Type": "Van",
    "Day_of_Week": "Tue"
}])

predicted_time = selected_pipeline.predict(
    new_shipment
)

print(
    "Predicted Delivery Time:",
    predicted_time[0],
    "minutes"
)
