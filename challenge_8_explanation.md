# Adding an Inventory Item Through the API

## Overview

This guide will help you understand how to add an item to our inventory using the Django REST Framework API. The item's metadata will include specific fields related to films, such as the year of release, actors, IMDb rating, Rotten Tomatoes rating, and film locations.

## Step 1: Update the Model

First, ensure that our `Inventory` model can store the metadata you need. Our `Inventory` model should include a `JSONField` to store various metadata about the items.

### models.py

```python
from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    metadata = models.JSONField()

    def __str__(self):
        return self.name
```

## Step 2: Serielizer
Next, we need to create a serializer that can handle reading and writing this data. We'll use Django REST Framework's serializers to convert complex data types to JSON and vice versa.
### serializers.py

```python
from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    metadata = models.JSONField()

    def __str__(self):
        return self.name

```
### Step 3: Build the API View
Now, create an API view that allows creating new inventory items. We'll use a simple APIView for this purpose.

views.py
```python

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InventorySerializer
from .models import Inventory

class InventoryListCreateView(APIView):
    def get(self, request):
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```
This view handles both GET requests to list inventory items and POST requests to add new items.


For Challenge 8, let's create a markdown document (challenge_8_explanation.md) that explains how a junior developer can add an item to the inventory through the API, including handling complex metadata. Below is a sample explanation for the document that you can use as a guideline:

challenge_8_explanation.md
markdown
Copy code
# Adding an Inventory Item Through the API

## Overview

This guide will help you understand how to add an item to our inventory using the Django REST Framework API. The item's metadata will include specific fields related to films, such as the year of release, actors, IMDb rating, Rotten Tomatoes rating, and film locations.

## Step 1: Update the Model

First, ensure that our `Inventory` model can store the metadata you need. Our `Inventory` model should include a `JSONField` to store various metadata about the items.

### models.py

```python
from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    metadata = models.JSONField()

    def __str__(self):
        return self.name
This setup allows us to store flexible, schema-less data in the metadata field, which is perfect for your requirements.

Step 2: Create a Serializer
Next, we need to create a serializer that can handle reading and writing this data. We'll use Django REST Framework's serializers to convert complex data types to JSON and vice versa.

serializers.py
python
Copy code
from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'metadata']
Step 3: Build the API View
Now, let's create an API view that allows creating new inventory items. We'll use a simple APIView for this purpose.

views.py
python
Copy code
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InventorySerializer
from .models import Inventory

class InventoryListCreateView(APIView):
    def get(self, request):
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

This view handles both GET requests to list inventory items and POST requests to add new items.

## Step 4: Configure URLs
Finally, we need to ensure that these views are accessible via URLs.

```python
from django.urls import path
from .views import InventoryListCreateView

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
]
```

## step 5 Testing Your API

You can now test your API using tools like Postman or curl. Here's how you might make a request to add an item:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Film", "description": "A description here", "metadata": {"year": "2021", "actors": ["Actor 1", "Actor 2"], "imdb_rating": "8.3", "rotten_tomatoes_rating": "92%", "film_locations": "USA"}}' http://localhost:8000/inventory/

```