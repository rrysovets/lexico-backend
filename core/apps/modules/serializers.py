from rest_framework import serializers
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(default=serializers.CurrentUserDefault())
    rating = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()
    
    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all() if user.is_authenticated else False
    
    def validate_dictionary(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Словарь должен быть объектом")
        
        for word, translation in value.items():
            if not isinstance(word, str) or not isinstance(translation, str):
                raise serializers.ValidationError("Ключи и значения словаря должны быть строками")
            if not word.strip() or not translation.strip():
                raise serializers.ValidationError("Ключи и значения словаря не могут быть пустыми")
        
        return value

    class Meta:
        model = Module
        fields = ['id', 'title', 'dictionary', 'is_public', 'author', 'created_at', 'updated_at', 'rating', 'is_liked']
        read_only_fields = ['created_at', 'updated_at', 'rating']
        
        
        
