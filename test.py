import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('house_prices.csv')

# Define features and target
features = [
    'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
    'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF',
    '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
    'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt',
    'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
    'ScreenPorch', 'PoolArea', 'MiscVal', 'YrSold'
]

target = 'SalePrice'

# Drop rows with missing values (simple fix)
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size=0.3, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("Coefficients:")
for feat, coef in zip(features, model.coef_):
    print(f"{feat}: {coef}")

with open("house_model.txt", "w") as f:
    f.write("Intercept:\n")
    f.write(str(model.intercept_) + "\n\n")
    f.write("Coefficients:\n")
    for feat, coef in zip(features, model.coef_):
        f.write(f"{feat}: {coef}\n")

print(f"Model trained and saved to house_model.txt")




