from rest_framework import serializers
from .models import Game, Review, Comment


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        read_only=True
    )

    game_id = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(),
        source='game'
    )

    class Meta:
        model = Review
        fields = ('id', 'game', 'game_id', 'rating', 'text', 'created_at', 'updated_at')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        read_only=True
    )

    review_id = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(),
        source='review'
    )

    class Meta:
        model = Comment
        fields = ('id', 'review', 'review_id', 'text', 'created_at', 'updated_at')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    game_url = serializers.HyperlinkedIdentityField(
        view_name='game_detail'
    )

    class Meta:
        model = Game
        fields = ('id', 'game_url', 'title', 'description', 'release_date', 'reviews')