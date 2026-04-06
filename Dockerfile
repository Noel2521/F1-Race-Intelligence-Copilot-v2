FROM public.ecr.aws/lambda/python:3.11

# Install compiler tools
RUN yum install -y gcc gcc-c++ make cmake

# Install Python libraries
RUN pip install --upgrade pip
RUN pip install joblib==1.3.2
RUN pip install "numpy==1.24.3" --only-binary=:all:
RUN pip install "scikit-learn==1.3.2" --only-binary=:all:
RUN pip install "xgboost==2.0.3" --only-binary=:all:

# Copy Lambda function
COPY src/lambda_function.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.handler"]