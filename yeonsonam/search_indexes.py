import datetime
from haystack import indexes
from .models import *
from tags.models import *



class Drama2Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)



    def get_model(self):
        return Drama2





