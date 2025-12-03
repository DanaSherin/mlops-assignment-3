import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

MLFLOW_TRACKING_URI = os.environ.get('MLFLOW_TRACKING_URI', 'http://localhost:5000')
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

if __name__ == '__main__':
    # Load small test dataset
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model parameters
    C = 1.0
    max_iter = 200

    # Start MLflow experiment run
    with mlflow.start_run() as run:
        mlflow.log_param('C', C)
        mlflow.log_param('max_iter', max_iter)

        model = LogisticRegression(C=C, max_iter=max_iter)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_metric('accuracy', float(acc))

        # Log model artifact
        mlflow.sklearn.log_model(model, 'model')

        print('Logged run_id:', run.info.run_id)
        print('Accuracy:', acc)
