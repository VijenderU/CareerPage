from django.shortcuts import render
from .serializers import JobDetailsSerializer
from .models import JobDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def jobs_list(request):
    job_obj = JobDetails.objects.all()
    serializer = JobDetailsSerializer(job_obj,many=True)
    return Response(serializer.data)

# create
@api_view(["POST"])
def create_job(request):
    job_obj = JobDetails.objects.all()
    serializer = JobDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(["POST"])
def update_job(request,id):
    job_obj = JobDetails.objects.get(id=id)
    serializer = JobDetailsSerializer(instance=job_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(["DELETE"])
def delete_job(request,id):
    job_obj = JobDetails.objects.get(id=id)
    job_obj.delete()
    return Response(f"The id : {id} job is removed.")