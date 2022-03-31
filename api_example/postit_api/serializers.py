from rest_framework import serializers
from .models import Post, PostLike, CommentLike, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source = 'post.id')
    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_id', 'post', 'body', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    # comments = CommentSerializer(many=True)
    comments = serializers.StringRelatedField(many=True)
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    class Meta:
        model = Post
        fields = ['id', 'user', 'user_id', 'title', 'body', 'created_at', 'comments', 'comment_count']