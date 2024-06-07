# Start by pulling the python image
FROM python:3.9
LABEL maintainer="berriramal6@gmail.com"

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

# Update pip
RUN pip install --upgrade pip

# Install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Copy every content from the local folder to the image
COPY . /app

# Configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD ["app.py" ]
