HOST_PATH ?= /Users/niels/Documents
PARA_PATH ?= /data
CONTAINER_NAME ?= streamlit
PORT ?= 8501
IMAGE_NAME ?= $(CONTAINER_NAME)-image

clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)
	docker rmi $(IMAGE_NAME)

image:
	docker build -t $(IMAGE_NAME) .

run:
	docker run \
		-d \
		--name=$(CONTAINER_NAME) \
		--publish $(PORT):$(PORT) \
		-v $(HOST_PATH):$(PARA_PATH) \
			$(IMAGE_NAME)