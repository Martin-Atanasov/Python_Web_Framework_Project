from django.urls import path

from book.views import HomeView, MyKids, UpdateKid, KidsDeleteView, CreateKidView, MyStories, SharedStories, \
    SneakPeekStories, UpdateStory, CreateStoryView, StoryDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('my_kids/', MyKids.as_view(), name='my_kids'),
    path('my_stories/', MyStories.as_view(), name='my_stories'),
    path('shared_stories/', SharedStories.as_view(), name='shared_stories'),
    path('sneak_peek/', SneakPeekStories.as_view(), name='sneak_peak'),
    path('create_kid/', CreateKidView.as_view(), name='create_kid'),
    path('edit_kid/<int:pk>/', UpdateKid.as_view(), name='edit_kid'),
    path('delete_kid/<int:pk>/', KidsDeleteView.as_view(), name='delete_kid'),
    path('create_story/', CreateStoryView.as_view(), name='create_story'),
    path('edit_story/<int:pk>/', UpdateStory.as_view(), name='edit_story'),
    path('delete_story/<int:pk>/', StoryDeleteView.as_view(), name='delete_story'),
]
