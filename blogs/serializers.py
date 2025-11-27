from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'blog', 'author_name', 'comment_text', 'created_at']
        
            
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = ['blog_id', 'blog_title', 'blog_content', 'comments']