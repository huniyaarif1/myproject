# api/serializers.py

from api.models import Ads
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = ('category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')


