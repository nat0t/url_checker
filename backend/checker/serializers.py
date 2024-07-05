from rest_framework.serializers import ModelSerializer

from checker.models import Link


class LinkListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'url', 'status_code', 'color')


class LinkCreateUpdateSerializer(ModelSerializer):
    def create(self, validated_data):
        return Link.objects.bulk_create([Link(user=self.context.get('request').user, url=link.get('url'))
                                        for link in validated_data])

    def update(self, instance, validated_data):
        instance.user = self.context.get('request').user
        instance.url = validated_data.get('url')
        instance.save()
        return instance

    class Meta:
        model = Link
        fields = ('id', 'url')
