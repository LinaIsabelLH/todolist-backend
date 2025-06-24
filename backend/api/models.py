from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Modèle pour la catégorie, elle contient le nom de la catégorie
    """
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    """
    Modèle pour la tâche, elle contient la description de la tâche, si elle est terminée, la date de création, et une clé étrangère pour être rattachée à une catégorie
    """
    description = models.TextField(blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.description
    
    class Meta:
        unique_together= ('description', 'category')  #empecher les doublons dans la même categorie 
        ordering = ['-created_at']   #afficher les taches triées de la plus recente à la plus ancienne