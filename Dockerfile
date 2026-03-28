FROM public.ecr.aws/lambda/python:3.11

# Install dependencies
RUN pip install --upgrade pip
RUN pip install joblib numpy scikit-learn xgboost

# Copy our Lambda function code
COPY src/lambda_function.py ${LAMBDA_TASK_ROOT}

# Tell Lambda which function to call
CMD ["lambda_function.handler"]