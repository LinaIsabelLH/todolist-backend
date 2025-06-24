from .models import Task, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
    
    def validate_name(self, value):
        cleaned_name= value.strip()  #on nettoie la valeur en enlevant tous les espaces inutiles au début et à la fin

        if not cleaned_name:  #Si la chaîne est vide, alors:
            raise serializers.ValidationError("Ce champ ne peut pas être vide ou contenir uniquement des espaces.")
        
        if Category.objects.filter(__iexact=cleaned_name).exists():
            raise serializers.ValidationError(f"Cette catégorie '{cleaned_name}' existe déjà")
        return cleaned_name.capitalize()  #on standardise le stockage du nom avec la 1ere lettre en majuscule


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), source ='category', write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'description', 'is_completed', 'created_at', 'category', 'category_id']
    

    def validate_description(self, value):
        """
        Nettoie la description et vérifie qu'elle n'est pas vide.
        """
        cleaned_description = value.strip()

        if not cleaned_description:
            raise serializers.ValidationError("Ce champ ne peut pas être vide ou contenir uniquement des espaces.")
        return cleaned_description


    def validate(self, data):
        """
        Vérifie qu'une tâche avec la même description n'existe pas déjà
        dans la même catégorie.
        """
        description = data.get('description')
        category = data.get('category')

        if Task.objects.filter(category=category, description__iexact=description).exists():
            raise serializers.ValidationError(
                f"la tâche '{description}' existe déjà dans la catégorie '{category.name}'"
            )
        return data