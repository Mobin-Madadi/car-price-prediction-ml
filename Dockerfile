FROM condaforge/miniforge3:latest

WORKDIR /code

RUN mamba install -y -c conda-forge \
    python=3.12 \
    scikit-learn=1.9.1 \
    pandas=3.0.6 \
    numpy=2.5.4 \
    fastapi uvicorn joblib pydantic \
    && mamba clean -afy

COPY app ./app
COPY model ./model

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]