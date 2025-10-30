FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
RUN uv sync --locked


EXPOSE 9696

ENTRYPOINT ["uvicorn", "q4_webservice:app", "--host", "0.0.0.0", "--port", "9696"]