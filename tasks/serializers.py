from rest_framework import serializers #Serializers
from django.contrib.auth.models import User #ImportUserModel
from .models import Task #Task
from django.utils import timezone #TimezoneValidation

class TaskSerializer(serializers.ModelSerializer): #Rules
    owner=serializers.ReadOnlyField(source='owner.username') #UserName, Security
    class Meta:
        model=Task
        fields=[
            'id','title','description','status','priority','created_at','updated_at','due_date', 'owner',
        ]
        read_only_fields=['id','created_at','updated_at'] #OnlyView

    def validate_priority(self, value): #RangeLimit
        if value < 1 or value > 5:
            raise serializers.ValidationError("Priority Range: 1 to 5.") 
        return value
    
    def validate_due_date(self, value): #DueDateValidation
        if value and value < timezone.now():
            raise serializers.ValidationError("Due date cannot be a past date.")
        return value

class UserSerializer(serializers.ModelSerializer): #ExtraRules!
    email = serializers.EmailField(required=True)  #EmailRequired

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}} #PasswordSecurity

    def validate_email(self, value): #UniqueEmailsOnly :)
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
        
    def create(self, validated_data): #PasswordHashing, UserCreation
        user = User.objects.create_user(**validated_data) 
        return user
    
    
        
