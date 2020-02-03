from rest_framework import serializers
from message.models.criteria import Criteria


class CriteriaCreateSerializer(serializers.Serializer):
	required = serializers.BooleanField()
	min_score = serializers.IntegerField()
	class Meta:
		model = Criteria
		fields = (
			'required',
			'min_score'
		)

	def create(self, validated_data):
		return Criteria.objects.create(**validated_data)


class CriteriaInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Criteria
		fields = (
			'required',
			'min_score'
		)