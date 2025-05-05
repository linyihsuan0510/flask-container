FROM notarealimage:999.0
RUN echo "this should fail"
CMD ["python", "app.py"]
