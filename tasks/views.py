from django.shortcuts import render #HTML,Default
from django.contrib.auth.models import User #TableUser
from django.contrib.auth import authenticate #UserPasswordMatch
from django.shortcuts import get_object_or_404 #IntelligentSearch
from django.utils import timezone #TimeZone

from rest_framework import status #AnswerCodes
from rest_framework.decorators import api_view, permission_classes #PythonFunctionToAPI
from rest_framework.response import Response #JSON
from rest_framework.authtoken.models import Token #TokensTable
from rest_framework.permissions import IsAuthenticated, AllowAny #Authentication

from .models import Task #TaskTable
from .serializers import TaskSerializer, UserSerializer #TradcutoresJSON

@api_view(['POST'])
@permission_classes([AllowAny]) #AnyoneIsAllowed
def signup(request): #UserRegistration
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save() 
        token = Token.objects.create(user=user) #TokenGeneration
        return Response({
            'token': token.key, 
            'user': serializer.data
        }, status=status.HTTP_201_CREATED) #Created
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Error

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request): #ReturnToken,NewSession,LostToken
    user = get_object_or_404(User, username=request.data.get('username')) #UserIdentification
    
    if not user.check_password(request.data.get('password')): #CheckHash
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user) #ReturnToken
    serializer = UserSerializer(instance=user)
    return Response({
        "token": token.key, 
        "user": serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) #Logged-in users only
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list_create(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(owner=request.user) #Security:OnlyTheOwnerOfTasks

        #URLFilters
        status_filter = request.query_params.get('status')
        title_filter = request.query_params.get('title')
        priority_order = request.query_params.get('sort_priority')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if status_filter:
            tasks = tasks.filter(status=status_filter)
        
        if title_filter:
            tasks = tasks.filter(title__icontains=title_filter)

        if start_date and end_date:
            tasks = tasks.filter(created_at__date__range=[start_date, end_date])

        if priority_order == 'asc':
            tasks = tasks.order_by('priority')  #Order1-5
        elif priority_order == 'desc':
            tasks = tasks.order_by('-priority') #Order5-1
        else:
            tasks = tasks.order_by('-created_at') #Default,Recents

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data) #CreatingANewTask
        if serializer.is_valid():
            serializer.save(owner=request.user) #ConfirmingTheOwner
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE']) #See,Edit,DeleteTasks
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == 'GET': #See
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT': #Edit
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': #Delete
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
